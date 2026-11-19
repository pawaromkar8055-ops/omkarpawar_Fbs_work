import os
from functools import wraps
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import mysql.connector

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'replace-this-development-secret')
UPLOAD_FOLDER = os.path.join(app.root_path, 'uploads')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 3 * 1024 * 1024
ALLOWED = {'pdf'}

# Set these environment variables before running, or edit the defaults for local learning.
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'pass123',
    'database': 'placement_system'
}

def db():
    return mysql.connector.connect(**DB_CONFIG)

def student_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if 'student_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return wrapped

def admin_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if not session.get('admin'):
            return redirect(url_for('admin_login'))
        return f(*args, **kwargs)
    return wrapped

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED

@app.route('/')
def home():
    return redirect(url_for('register'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        fields = ['registration_no','first_name','last_name','dob','location','education','experience','skills','technical_skills','soft_skills','hobbies','interests','desired_positions','job_location','email','contact']
        data = {k: request.form.get(k, '').strip() for k in fields}
        password = request.form.get('password', '')
        if not data['registration_no'] or not data['first_name'] or not data['last_name'] or not data['email'] or len(password) < 8:
            flash('Please fill required fields. Password must be at least 8 characters.', 'danger')
            return render_template('register.html', data=data)
        conn = db(); cur = conn.cursor()
        try:
            cur.execute('SELECT id FROM students WHERE email=%s OR registration_no=%s', (data['email'], data['registration_no']))
            if cur.fetchone():
                flash('Email or registration number already exists.', 'danger')
                return render_template('register.html', data=data)
            cols = ','.join(fields) + ',password_hash'
            placeholders = ','.join(['%s'] * (len(fields)+1))
            cur.execute(f'INSERT INTO students ({cols}) VALUES ({placeholders})', tuple(data[k] for k in fields) + (generate_password_hash(password),))
            conn.commit(); flash('Registration submitted. Wait for admin approval.', 'success')
            return redirect(url_for('login'))
        except mysql.connector.Error as e:
            conn.rollback(); flash(f'Database error: {e}', 'danger')
        finally:
            cur.close(); conn.close()
    return render_template('register.html', data={})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email','').strip(); password = request.form.get('password','')
        conn = db(); cur = conn.cursor(dictionary=True)
        cur.execute('SELECT * FROM students WHERE email=%s', (email,)); student = cur.fetchone()
        cur.close(); conn.close()
        if student and check_password_hash(student['password_hash'], password):
            if student['status'] != 'Approved':
                flash('Your account is not approved yet.', 'warning')
            else:
                session.clear(); session['student_id'] = student['id']; session['student_name'] = student['first_name']
                return redirect(url_for('dashboard'))
        else: flash('Invalid email or password.', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear(); return redirect(url_for('login'))

@app.route('/dashboard')
@student_required
def dashboard():
    conn=db(); cur=conn.cursor(dictionary=True); sid=session['student_id']
    cur.execute('SELECT * FROM students WHERE id=%s',(sid,)); student=cur.fetchone()
    cur.execute('SELECT COUNT(*) AS n FROM jobs WHERE active=1'); job_count=cur.fetchone()['n']
    cur.execute('SELECT COUNT(DISTINCT job_id) AS n FROM applications WHERE student_id=%s',(sid,)); applied=cur.fetchone()['n']
    # Completion score based on a set of fields (including resume); empty values are not counted.
    profile_fields=[student.get('education'),student.get('location'),student.get('skills'),student.get('technical_skills'),student.get('soft_skills'),student.get('desired_positions'),student.get('job_location'),student.get('contact'),student.get('resume')]
    percent=int(sum(bool(x) for x in profile_fields)/len(profile_fields)*100)
    cur.close(); conn.close()
    return render_template('dashboard.html', student=student, job_count=job_count, applied=applied, percent=percent)

@app.route('/profile', methods=['GET','POST'])
@student_required
def profile():
    sid=session['student_id']; conn=db(); cur=conn.cursor(dictionary=True)
    if request.method=='POST':
        keys=['location','education','experience','skills','technical_skills','soft_skills','hobbies','interests','desired_positions','job_location','contact']
        vals=[request.form.get(k,'').strip() for k in keys]
        resume=request.files.get('resume'); resume_name=None
        if resume and resume.filename:
            if not allowed_file(resume.filename):
                flash('Only PDF resumes are accepted.', 'danger'); cur.execute('SELECT * FROM students WHERE id=%s',(sid,)); student=cur.fetchone(); cur.close(); conn.close(); return render_template('profile.html',student=student)
            resume_name=secure_filename(resume.filename)
            resume_name=f'{sid}_{resume_name}'
            resume.save(os.path.join(app.config['UPLOAD_FOLDER'],resume_name))
        assignments=', '.join(f'{k}=%s' for k in keys)
        sql=f'UPDATE students SET {assignments}' + (', resume=%s' if resume_name else '') + ' WHERE id=%s'
        params=vals + ([resume_name] if resume_name else []) + [sid]
        cur.execute(sql,params); conn.commit(); flash('Profile updated.', 'success')
    cur.execute('SELECT * FROM students WHERE id=%s',(sid,)); student=cur.fetchone(); cur.close(); conn.close()
    return render_template('profile.html',student=student)

@app.route('/jobs')
@student_required
def jobs():
    conn=db(); cur=conn.cursor(dictionary=True); cur.execute('SELECT * FROM jobs WHERE active=1 ORDER BY id DESC'); rows=cur.fetchall(); cur.close(); conn.close()
    return render_template('jobs.html',jobs=rows)

@app.route('/jobs/<int:job_id>')
@student_required
def job_detail(job_id):
    conn=db(); cur=conn.cursor(dictionary=True); cur.execute('SELECT * FROM jobs WHERE id=%s AND active=1',(job_id,)); job=cur.fetchone(); cur.close(); conn.close()
    if not job: flash('Job not found.','danger'); return redirect(url_for('jobs'))
    return render_template('job_detail.html',job=job)

@app.route('/jobs/<int:job_id>/apply', methods=['POST'])
@student_required
def apply(job_id):
    sid=session['student_id']; conn=db(); cur=conn.cursor(dictionary=True)
    cur.execute('SELECT * FROM jobs WHERE id=%s AND active=1',(job_id,)); job=cur.fetchone()
    cur.execute('SELECT * FROM students WHERE id=%s',(sid,)); student=cur.fetchone()
    if not job: flash('Job not found.','danger'); cur.close(); conn.close(); return redirect(url_for('jobs'))
    # Basic skills check: each must-have skill must appear in student's combined skills text.
    must=[x.strip().lower() for x in (job.get('must_have_skills') or '').split(',') if x.strip()]
    student_skills=' '.join([student.get('skills') or '', student.get('technical_skills') or '']).lower()
    missing=[x for x in must if x not in student_skills]
    if missing:
        flash('Eligibility check failed. Missing skills: '+', '.join(missing),'danger'); cur.close(); conn.close(); return redirect(url_for('job_detail',job_id=job_id))
    if not student.get('resume'):
        flash('Please upload a PDF resume in your profile before applying.','warning'); cur.close(); conn.close(); return redirect(url_for('profile'))
    try:
        cur.execute('INSERT INTO applications (student_id,job_id,experience_type,relocate,work_description) VALUES (%s,%s,%s,%s,%s)',(sid,job_id,request.form.get('experience_type'),request.form.get('relocate'),request.form.get('work_description')))
        conn.commit(); flash('Application submitted successfully.','success')
    except mysql.connector.IntegrityError:
        conn.rollback(); flash('You have already applied for this job.','warning')
    finally: cur.close(); conn.close()
    return redirect(url_for('applications'))

@app.route('/applications')
@student_required
def applications():
    conn=db(); cur=conn.cursor(dictionary=True)
    cur.execute('SELECT a.*,j.job_code,j.company_name,j.role,j.location FROM applications a JOIN jobs j ON a.job_id=j.id WHERE a.student_id=%s ORDER BY a.applied_at DESC',(session['student_id'],)); rows=cur.fetchall()
    cur.close(); conn.close(); return render_template('applications.html',applications=rows)

@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    if request.method=='POST':
        # Configure ADMIN_USER and ADMIN_PASSWORD in environment variables.
        if request.form.get('username')==os.getenv('ADMIN_USER','admin') and request.form.get('password')==os.getenv('ADMIN_PASSWORD','change-me'):
            session.clear(); session['admin']=True; return redirect(url_for('admin'))
        flash('Invalid admin credentials.','danger')
    return render_template('login.html', admin_mode=True)

@app.route('/admin')
@admin_required
def admin():
    conn=db(); cur=conn.cursor(dictionary=True); cur.execute("SELECT * FROM students WHERE status='Pending' ORDER BY created_at"); students=cur.fetchall(); cur.close(); conn.close()
    return render_template('admin.html',students=students)

@app.route('/admin/student/<int:sid>/<action>', methods=['POST'])
@admin_required
def admin_action(sid,action):
    if action not in ('approve','reject'): return redirect(url_for('admin'))
    status='Approved' if action=='approve' else 'Rejected'
    conn=db(); cur=conn.cursor(); cur.execute('UPDATE students SET status=%s WHERE id=%s',(status,sid)); conn.commit(); cur.close(); conn.close()
    flash(f'Student {status.lower()}.','success'); return redirect(url_for('admin'))

@app.route('/admin/logout')
def admin_logout(): session.clear(); return redirect(url_for('admin_login'))

if __name__=='__main__':
    app.run(debug=True)
