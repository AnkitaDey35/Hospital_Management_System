from datetime import datetime
import mysql.connector
conn = mysql.connector.connect(
    host="localhost",
    user="root",       
    password="",
    database="Crud_App",

)

cursor = conn.cursor()

def create_Patient(First_Name, Last_Name,age, Gender, Address, Phone_Number, Medical_History):
    query = "INSERT INTO Patient (First_Name, Last_Name,age, Gender, Address, Phone_Number, Medical_History) VALUES (%s, %s, %s,%s, %s, %s, %s)"
    cursor.execute(query, (First_Name, Last_Name,age, Gender, Address, Phone_Number, Medical_History))
    conn.commit()
    print("User created successfully.")

def read_Patient():
    cursor.execute("SELECT * FROM Patient")
    for (Patient_id, First_Name, Last_Name,age, Gender, Address, Phone_Number, Medical_History) in cursor.fetchall():
        print(f"ID: {Patient_id}, First Name: {First_Name}, Last_Name:{Last_Name}, Age: {age} Gender: {Gender}, Address: {Address}, Phone Number: {Phone_Number}, Medical History: {Medical_History}   ")

def update_Patient(Patient_id, First_Name, Last_Name,age, Gender, Address, Phone_Number, Medical_History):
    query = "UPDATE Patient SET First_Name=%s,Last_Name=%s, age=%s, Gender=%s, Address=%s, Phone_Number=%s, Medical_History=%s WHERE Patient_ID=%s"
    cursor.execute(query, (First_Name, Last_Name,age, Gender, Address, Phone_Number, Medical_History, Patient_id))
    conn.commit()
    print("Patient updated successfully.")

def delete_Patient(Patient_id):
    query = "DELETE FROM users WHERE id=%s"
    cursor.execute(query, (Patient_id,))
    conn.commit()
    print("Patient deleted successfully.")

def create_Doctor(First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years):
    query = "INSERT INTO Doctor (First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years))
    conn.commit()
    print("Doctor created successfully.")

def read_Doctor():
    cursor.execute("SELECT * FROM Doctor")
    for (Doctor_ID, First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years) in cursor.fetchall():
        print(f"ID: {Doctor_ID}, Name: Dr. {First_Name} {Last_Name}, Specialization: {Specialization}, Phone: {Phone_Number}, Email: {Email}, Qualification: {Qualification}, Experience: {Experience_Years} years")

def update_Doctor(Doctor_ID, First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years):
    query = "UPDATE Doctor SET First_Name=%s, Last_Name=%s, Specialization=%s, Phone_Number=%s, Email=%s, Qualification=%s, Experience_Years=%s WHERE Doctor_ID=%s"
    cursor.execute(query, (First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years, Doctor_ID))
    conn.commit()
    print("Doctor updated successfully.")

def delete_Doctor(Doctor_ID):
    query = "DELETE FROM Doctor WHERE Doctor_ID=%s"
    cursor.execute(query, (Doctor_ID,))
    conn.commit()
    print("Doctor deleted successfully.")

def create_Appointment(Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Reason):
    query = "INSERT INTO Appointment (Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Reason) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Reason))
    conn.commit()
    print("Appointment created successfully.")

def read_Appointment():
    query = """
    SELECT a.Appointment_ID, p.First_Name, p.Last_Name, d.First_Name, d.Last_Name, 
           a.Appointment_Date, a.Appointment_Time, a.Status, a.Reason 
    FROM Appointment a
    JOIN Patient p ON a.Patient_ID = p.Patient_id
    JOIN Doctor d ON a.Doctor_ID = d.Doctor_ID
    """
    cursor.execute(query)
    for (Appointment_ID, pat_fname, pat_lname, doc_fname, doc_lname, date, time, status, reason) in cursor.fetchall():
        print(f"Appointment ID: {Appointment_ID}, Patient: {pat_fname} {pat_lname}, Doctor: Dr. {doc_fname} {doc_lname}, Date: {date}, Time: {time}, Status: {status}, Reason: {reason}")

def update_Appointment_Status(Appointment_ID, Status):
    query = "UPDATE Appointment SET Status=%s WHERE Appointment_ID=%s"
    cursor.execute(query, (Status, Appointment_ID))
    conn.commit()
    print("Appointment status updated successfully.")

def create_Bill(Patient_ID, Appointment_ID, Total_Amount, Payment_Method):
    bill_date = datetime.now().date()
    query = "INSERT INTO Billing (Patient_ID, Appointment_ID, Bill_Date, Total_Amount, Payment_Method) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(query, (Patient_ID, Appointment_ID, bill_date, Total_Amount, Payment_Method))
    conn.commit()
    print("Bill created successfully.")

def read_Billing():
    query = """
    SELECT b.Bill_ID, p.First_Name, p.Last_Name, b.Bill_Date, b.Total_Amount, 
           b.Payment_Status, b.Payment_Method 
    FROM Billing b
    JOIN Patient p ON b.Patient_ID = p.Patient_id
    """
    cursor.execute(query)
    for (Bill_ID, first_name, last_name, bill_date, total_amount, payment_status, payment_method) in cursor.fetchall():
        print(f"Bill ID: {Bill_ID}, Patient: {first_name} {last_name}, Date: {bill_date}, Amount: ${total_amount}, Status: {payment_status}, Method: {payment_method}")

def update_Payment_Status(Bill_ID, Payment_Status):
    query = "UPDATE Billing SET Payment_Status=%s WHERE Bill_ID=%s"
    cursor.execute(query, (Payment_Status, Bill_ID))
    conn.commit()
    print("Payment status updated successfully.")

def create_Room(Room_Number, Room_Type, Price_Per_Day):
    query = "INSERT INTO Room (Room_Number, Room_Type, Price_Per_Day) VALUES (%s, %s, %s)"
    cursor.execute(query, (Room_Number, Room_Type, Price_Per_Day))
    conn.commit()
    print("Room created successfully.")

def read_Room():
    cursor.execute("SELECT * FROM Room")
    for (Room_ID, Room_Number, Room_Type, Status, Price_Per_Day) in cursor.fetchall():
        print(f"Room ID: {Room_ID}, Number: {Room_Number}, Type: {Room_Type}, Status: {Status}, Price/Day: ${Price_Per_Day}")

def update_Room_Status(Room_ID, Status):
    query = "UPDATE Room SET Status=%s WHERE Room_ID=%s"
    cursor.execute(query, (Status, Room_ID))
    conn.commit()
    print("Room status updated successfully.")

def create_Admission(Patient_ID, Room_ID, Reason):
    admission_date = datetime.now().date()
    query = "INSERT INTO Admission (Patient_ID, Room_ID, Admission_Date, Reason) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (Patient_ID, Room_ID, admission_date, Reason))
    update_Room_Status(Room_ID, "Occupied")
    conn.commit()
    print("Patient admitted successfully.")

def discharge_Patient(Admission_ID):
    discharge_date = datetime.now().date()
    query = "SELECT Room_ID FROM Admission WHERE Admission_ID=%s"
    cursor.execute(query, (Admission_ID,))
    room_id = cursor.fetchone()[0]
    
    query = "UPDATE Admission SET Discharge_Date=%s, Status='Discharged' WHERE Admission_ID=%s"
    cursor.execute(query, (discharge_date, Admission_ID))
    update_Room_Status(room_id, "Available")
    conn.commit()
    print("Patient discharged successfully.")

def read_Admission():
    query = """
    SELECT a.Admission_ID, p.First_Name, p.Last_Name, r.Room_Number, 
           a.Admission_Date, a.Discharge_Date, a.Status, a.Reason 
    FROM Admission a
    JOIN Patient p ON a.Patient_ID = p.Patient_id
    JOIN Room r ON a.Room_ID = r.Room_ID
    """
    cursor.execute(query)
    for (Admission_ID, first_name, last_name, room_number, admission_date, discharge_date, status, reason) in cursor.fetchall():
        print(f"Admission ID: {Admission_ID}, Patient: {first_name} {last_name}, Room: {room_number}, Admission: {admission_date}, Discharge: {discharge_date}, Status: {status}, Reason: {reason}")


def main():
    
    
    while True:
        print("\n=== HOSPITAL MANAGEMENT SYSTEM ===")
        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Appointment Management")
        print("4. Billing Management")
        print("5. Room Management")
        print("6. Admission Management")
        print("7. Exit")

        main_choice = input("Enter your choice: ")

        if main_choice == '1':
            
            while True:
                print("\n--- PATIENT MANAGEMENT ---")
                print("1. Create Patient")
                print("2. View Patients")
                print("3. Update Patient")
                print("4. Delete Patient")
                print("5. Back to Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    First_Name = input("Enter Patient's First Name: ")
                    Last_Name = input("Enter Patient's Last Name: ")
                    age = int(input("Enter Patient's age: "))
                    Gender = input("Enter Patient's Gender: ")
                    Address = input("Enter Patient's Address: ")    
                    Phone_Number = input("Enter Patient's Phone Number: ")
                    Medical_History = input("Enter Patient's Medical History: ")
                    create_Patient(First_Name, Last_Name, age, Gender, Address, Phone_Number, Medical_History)
                elif choice == '2':
                    read_Patient()
                elif choice == '3':
                    Patient_id = int(input("Enter Patient ID to update: "))
                    First_Name = input("Enter new First Name: ")
                    Last_Name = input("Enter new Last Name: ")
                    age = int(input("Enter new age: "))
                    Gender = input("Enter new Gender: ")
                    Address = input("Enter new Address: ")
                    Phone_Number = input("Enter new Phone Number: ")
                    Medical_History = input("Enter new Medical History: ")
                    update_Patient(Patient_id, First_Name, Last_Name, age, Gender, Address, Phone_Number, Medical_History)
                elif choice == '4':
                    Patient_id = int(input("Enter Patient ID to delete: "))
                    delete_Patient(Patient_id)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif main_choice == '2':
           
            while True:
                print("\n--- DOCTOR MANAGEMENT ---")
                print("1. Add Doctor")
                print("2. View Doctors")
                print("3. Update Doctor")
                print("4. Delete Doctor")
                print("5. Back to Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    First_Name = input("Enter Doctor's First Name: ")
                    Last_Name = input("Enter Doctor's Last Name: ")
                    Specialization = input("Enter Specialization: ")
                    Phone_Number = input("Enter Phone Number: ")
                    Email = input("Enter Email: ")
                    Qualification = input("Enter Qualification: ")
                    Experience_Years = int(input("Enter Experience Years: "))
                    create_Doctor(First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years)
                elif choice == '2':
                    read_Doctor()
                elif choice == '3':
                    Doctor_ID = int(input("Enter Doctor ID to update: "))
                    First_Name = input("Enter new First Name: ")
                    Last_Name = input("Enter new Last Name: ")
                    Specialization = input("Enter new Specialization: ")
                    Phone_Number = input("Enter new Phone Number: ")
                    Email = input("Enter new Email: ")
                    Qualification = input("Enter new Qualification: ")
                    Experience_Years = int(input("Enter new Experience Years: "))
                    update_Doctor(Doctor_ID, First_Name, Last_Name, Specialization, Phone_Number, Email, Qualification, Experience_Years)
                elif choice == '4':
                    Doctor_ID = int(input("Enter Doctor ID to delete: "))
                    delete_Doctor(Doctor_ID)
                elif choice == '5':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif main_choice == '3':
            
            while True:
                print("\n--- APPOINTMENT MANAGEMENT ---")
                print("1. Schedule Appointment")
                print("2. View Appointments")
                print("3. Update Appointment Status")
                print("4. Back to Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    Patient_ID = int(input("Enter Patient ID: "))
                    Doctor_ID = int(input("Enter Doctor ID: "))
                    Appointment_Date = input("Enter Appointment Date (YYYY-MM-DD): ")
                    Appointment_Time = input("Enter Appointment Time (HH:MM:SS): ")
                    Reason = input("Enter Reason: ")
                    create_Appointment(Patient_ID, Doctor_ID, Appointment_Date, Appointment_Time, Reason)
                elif choice == '2':
                    read_Appointment()
                elif choice == '3':
                    Appointment_ID = int(input("Enter Appointment ID: "))
                    Status = input("Enter new Status (Scheduled/Completed/Cancelled): ")
                    update_Appointment_Status(Appointment_ID, Status)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif main_choice == '4':
            
            while True:
                print("\n--- BILLING MANAGEMENT ---")
                print("1. Create Bill")
                print("2. View Bills")
                print("3. Update Payment Status")
                print("4. Back to Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    Patient_ID = int(input("Enter Patient ID: "))
                    Appointment_ID = int(input("Enter Appointment ID: "))
                    Total_Amount = float(input("Enter Total Amount: "))
                    Payment_Method = input("Enter Payment Method: ")
                    create_Bill(Patient_ID, Appointment_ID, Total_Amount, Payment_Method)
                elif choice == '2':
                    read_Billing()
                elif choice == '3':
                    Bill_ID = int(input("Enter Bill ID: "))
                    Payment_Status = input("Enter Payment Status (Paid/Pending): ")
                    update_Payment_Status(Bill_ID, Payment_Status)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif main_choice == '5':
           
            while True:
                print("\n--- ROOM MANAGEMENT ---")
                print("1. Add Room")
                print("2. View Rooms")
                print("3. Update Room Status")
                print("4. Back to Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    Room_Number = input("Enter Room Number: ")
                    Room_Type = input("Enter Room Type: ")
                    Price_Per_Day = float(input("Enter Price Per Day: "))
                    create_Room(Room_Number, Room_Type, Price_Per_Day)
                elif choice == '2':
                    read_Room()
                elif choice == '3':
                    Room_ID = int(input("Enter Room ID: "))
                    Status = input("Enter new Status (Available/Occupied/Maintenance): ")
                    update_Room_Status(Room_ID, Status)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif main_choice == '6':
            
            while True:
                print("\n--- ADMISSION MANAGEMENT ---")
                print("1. Admit Patient")
                print("2. View Admissions")
                print("3. Discharge Patient")
                print("4. Back to Main Menu")

                choice = input("Enter choice: ")

                if choice == '1':
                    Patient_ID = int(input("Enter Patient ID: "))
                    Room_ID = int(input("Enter Room ID: "))
                    Reason = input("Enter Admission Reason: ")
                    create_Admission(Patient_ID, Room_ID, Reason)
                elif choice == '2':
                    read_Admission()
                elif choice == '3':
                    Admission_ID = int(input("Enter Admission ID: "))
                    discharge_Patient(Admission_ID)
                elif choice == '4':
                    break
                else:
                    print("Invalid choice. Try again.")

        elif main_choice == '7':
            print("Exiting Hospital Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()



