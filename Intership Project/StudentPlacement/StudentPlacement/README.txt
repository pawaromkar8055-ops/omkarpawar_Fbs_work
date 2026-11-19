STUDENT PLACEMENT MODULE - FLASK + MYSQL

1. Install Python and MySQL Server. Create/import database by running database.sql in MySQL Workbench.
2. Open terminal in this project folder:
   python -m venv venv
   venv\Scripts\activate (Windows)
   pip install -r requirements.txt
3. Set database connection environment variables if needed:
   Windows cmd: set DB_USER=root ; set DB_PASSWORD=your_mysql_password
   PowerShell: $env:DB_USER='root'; $env:DB_PASSWORD='your_mysql_password'
   Defaults are localhost, root, blank password, database placement_system.
4. Configure admin login (development defaults are admin / change-me; change them):
   Windows cmd: set ADMIN_USER=admin ; set ADMIN_PASSWORD=your_strong_password
   PowerShell: $env:ADMIN_USER='admin'; $env:ADMIN_PASSWORD='your_strong_password'
   Set SECRET_KEY to a long random secret before deployment.
5. Run: python app.py
6. Visit http://127.0.0.1:5000/register
7. Admin portal: http://127.0.0.1:5000/admin/login
8. Admin approves student. Student login: http://127.0.0.1:5000/login
9. Add job rows in MySQL manually for initial testing. See sample SQL below.

SAMPLE JOB INSERT:
USE placement_system;
INSERT INTO jobs (job_code,company_name,vacancy,location,package,must_have_skills,good_to_have_skills,job_description,responsibilities,industry_type,department,role,employment_type)
VALUES ('JOB001','Demo Tech',3,'Pune','4 LPA','python,sql','flask','Junior Python role','Develop and test features','IT','Engineering','Python Developer','Full-time');

NOTES:
- This is an educational starter project, not production-ready.
- Admin credentials are configured via environment variables; defaults are for local development only.
- Basic must-have skill matching is a simple substring check and may need improved normalization.
- PDF resume uploads only; max 3MB. Add malware scanning and safer storage for production.
- For production, disable Flask debug mode, use HTTPS, stronger secret key, CSRF protection, secure cookies, rate limits, robust validation, and review permissions.
- Admin approval and rejection currently update student status; rejected students cannot log in because only Approved accounts can access.
