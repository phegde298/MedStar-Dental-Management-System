# MedStar-Dental-Management-System
MedStar Dental Management System is a command-line application developed as part of my Grade 12 CBSE Computer Science Project. 
My goal for this project was to demonstrate a practical application of file handling, databases and python programming by building a real-world clinic management system.

The system allows full CRUD operations for both doctors and patients through a simple terminal menu interface.

### FEATURES
- Doctor Management
- View, Add, Edit, Delete Doctors
- Patient Management
- View, Add, Edit, Delete Patients
- Simple login/sign-up flow
- Shows current date and time on homepage
- "About Us" section
- Handles invalid inputs gracefully

### TECH STACK
- Python
- MySQL (via `mysql-connector-python`
- tabulate for formatted console input

### DATABASE SCHEMA
The system requires the MySQL Server to have a database named `dental` and the following tables
<pre> ```CREATE TABLE doctors (
  doctor_id INT PRIMARY KEY,
  DOJ VARCHAR(50),
  name VARCHAR(100),
  salary INT
);

CREATE TABLE patients (
  patient_id INT PRIMARY KEY,
  date VARCHAR(50),
  name VARCHAR(100),
  fee INT
);

CREATE TABLE signup (
  username VARCHAR(100),
  password VARCHAR(100)
);``` </pre>

### TO GET STARTED
- Ensure MySQL server is running
- Update credentials if needed
- Install dependencies
`pip install tabulate mysql-connector-python`
- Run the program
`python MedStar_Dental_Management_System.py`

### NOTES
- The system currently uses my hardcoded credentials, which can be extended to use the `signup` table
- Entirely termninal based, making it portable and lightweight
- Easily extensible to include appointment scheduling or billing features
