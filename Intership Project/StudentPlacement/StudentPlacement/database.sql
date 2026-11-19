CREATE DATABASE IF NOT EXISTS placement_system;
USE placement_system;
CREATE TABLE IF NOT EXISTS students (
 id INT AUTO_INCREMENT PRIMARY KEY, registration_no VARCHAR(50) UNIQUE NOT NULL,
 first_name VARCHAR(100) NOT NULL, last_name VARCHAR(100) NOT NULL, dob DATE,
 location VARCHAR(100), education VARCHAR(255), experience VARCHAR(100), skills TEXT,
 technical_skills TEXT, soft_skills TEXT, hobbies TEXT, interests TEXT,
 desired_positions TEXT, job_location VARCHAR(100), email VARCHAR(255) UNIQUE NOT NULL,
 contact VARCHAR(20), password_hash VARCHAR(255) NOT NULL, resume VARCHAR(255),
 status VARCHAR(20) DEFAULT 'Pending', created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS jobs (
 id INT AUTO_INCREMENT PRIMARY KEY, job_code VARCHAR(50) UNIQUE NOT NULL,
 company_name VARCHAR(255) NOT NULL, vacancy INT DEFAULT 1, location VARCHAR(255), package VARCHAR(100),
 must_have_skills TEXT, good_to_have_skills TEXT, job_description TEXT, required_skills TEXT,
 responsibilities TEXT, industry_type VARCHAR(100), department VARCHAR(100), role VARCHAR(100),
 employment_type VARCHAR(100), active BOOLEAN DEFAULT TRUE
);
CREATE TABLE IF NOT EXISTS applications (
 id INT AUTO_INCREMENT PRIMARY KEY, student_id INT NOT NULL, job_id INT NOT NULL,
 experience_type VARCHAR(100), relocate VARCHAR(20), work_description TEXT,
 status VARCHAR(30) DEFAULT 'Pending', applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
 UNIQUE(student_id, job_id), FOREIGN KEY (student_id) REFERENCES students(id),
 FOREIGN KEY (job_id) REFERENCES jobs(id)
);
