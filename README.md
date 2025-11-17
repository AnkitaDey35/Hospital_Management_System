🏥 Hospital Management System — Full CRUD Application

A Python + MySQL–powered system for managing hospital operations

📌 Overview

This Hospital Management System (HMS) is a fully functional CRUD-based application designed to streamline key hospital operations. Built with Python and MySQL, it offers an efficient interface to manage:

🧑‍⚕️ Patient Records

👨‍⚕️ Doctor Information

📅 Appointment Scheduling

🛏 Room Allocation & Management

💳 Billing & Invoice Generation

This project demonstrates strong back-end development skills, database management expertise, and real-world application design.

🚀 Key Features
👨‍⚕️ Doctor Management

Add, view, update, and delete doctor profiles

Store specialization, availability, and contact details

🧑‍⚕️ Patient Management

Complete CRUD operations for patient data

Medical history tracking

Contact and demographic information

📅 Appointment Management

Schedule appointments between patients and doctors

Update appointment timings

Cancel or reschedule appointments

🛏 Room Management

Assign rooms to admitted patients

Update room availability

Track occupancy status

💳 Billing System

Generate bills for patient services

Include doctor fee, room charges, medicines, and procedures

Store and update billing information

🛠️ Tech Stack
Category	Technology
Language	Python
Database	MySQL
Connector	mysql-connector-python
Paradigm	CRUD Architecture
Deployment	Local Execution
📂 Project Structure
Hospital_Management_System/
│── hospital_management_system.py       
└── README.md

🗄️ Database Schema Overview
1️⃣ Patient Table

Stores patient personal and medical information.

Column	Type
Patient_ID	INT (PK, AUTO)
First_Name	VARCHAR(50)
Last_Name	VARCHAR(50)
Age	INT
Gender	VARCHAR(10)
Address	VARCHAR(120)
Phone_Number	VARCHAR(20)
Medical_History	TEXT
2️⃣ Doctor Table

Stores information about doctors and their specialization.

Column	Type
Doctor_ID	INT (PK, AUTO)
First_Name	VARCHAR(50)
Last_Name	VARCHAR(50)
Specialization	VARCHAR(50)
Phone_Number	VARCHAR(20)
Availability	VARCHAR(50)
3️⃣ Appointment Table

Manages appointments between doctors and patients.

Column	Type
Appointment_ID	INT (PK, AUTO)
Patient_ID	INT (FK)
Doctor_ID	INT (FK)
Appointment_Date	DATE
Appointment_Time	TIME
4️⃣ Room Management Table

Tracks room assignment and occupancy.

Column	Type
Room_ID	INT (PK, AUTO)
Room_Type	VARCHAR(50)
Status	VARCHAR(20)
Assigned_Patient	INT (FK, NULLABLE)
5️⃣ Billing Table

Stores billing and total charges for patients.

Column	Type
Bill_ID	INT (PK, AUTO)
Patient_ID	INT (FK)
Room_Charges	DECIMAL(10,2)
Doctor_Fees	DECIMAL(10,2)
Medicine_Cost	DECIMAL(10,2)
Total_Amount	DECIMAL(10,2)
🔧 Installation & Setup
1️⃣ Install Dependencies
pip install mysql-connector-python

2️⃣ Create Database
CREATE DATABASE HospitalDB;
USE HospitalDB;

3️⃣ Run the Script

Update DB credentials in the script:

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="HospitalDB"
)


Then run:

python hospital_management_system.py

▶️ How It Works

On running the program, the system displays a main menu:

1. Manage Patients
2. Manage Doctors
3. Manage Appointments
4. Manage Rooms
5. Manage Billing
6. Exit
Enter your choice:


Each section contains sub-menus for CRUD operations.

🎯 Learning Outcomes

✔ End-to-end CRUD system design
✔ Real-world relational database design
✔ Python–MySQL integration
✔ Modular architecture for large applications
✔ Problem solving in software development
✔ Backend logic for healthcare systems

📘 Future Enhancements

💡 Add a login system for admin & staff
💡 GUI interface using Tkinter / PyQt
💡 Web version using Flask / Django
💡 Medicine inventory management
💡 PDF invoice generation
💡 Email/SMS appointment reminders
