#EMPLOYEE DETAIL MANAGEMENT

import os

filename = r"D:\PROJECTS\employee management\Employee details.txt"      # File path 
Employees = {}      # Dictionary to store employee data in memory

def load_from_file(filename):       # Load employee data from file when progtam start
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(None, 7)
                if len(parts) == 8:
                    emp_id = int(parts[0])
                    Employees[emp_id] = {
                        "Name": parts[1],
                        "DOB": parts[2],
                        "Department": parts[3],
                        "Salary": float(parts[4]),
                        "Contact Number": int(parts[5]),
                        "E-Mail": parts[6],
                        "Address": parts[7]
                    }
        print("\nPrevious employee data loaded successfully!\n")
    except FileNotFoundError:
        print("\nNo existing file found. Starting fresh.\n")
    except Exception as e:
        print(f"Error loading data: {e}")


def save_to_file(filename):     # Save employee data to file
    try:
        with open(filename, "w") as file:
            for emp_id, details in Employees.items():
                file.write("{:<10} {:<15} {:<12} {:<15} {:<10} {:<15} {:<25} {:<20}\n".format(
                    emp_id,
                    details['Name'],
                    details['DOB'],
                    details['Department'],
                    details['Salary'],
                    details['Contact Number'],
                    details['E-Mail'],
                    details['Address']
                ))
        print("\nEmployee data saved successfully!\n")
    except Exception as e:
        print(f"Error: {e}")


def add_employee(emp_id, name, DOB, department, salary, contact_number, email, address):        # Add a new employee
    global Employees
    Employees[emp_id] = {
        "Name": name,
        "DOB": DOB,
        "Department": department,
        "Salary": salary,
        "Contact Number": contact_number,
        "E-Mail": email,
        "Address": address
    }
    print(f"\n{name}'s details added successfully\n")


def view_employee():        # View all employees
    if Employees:
        for emp_id, emp_details in Employees.items():
            print(f"ID: {emp_id}, Details: {emp_details}")
    else:
        print("\nNo Employees Added Yet!\n")


def update_employee(emp_id, name=None, DOB=None, department=None, salary=None, contact_number=None, email=None, address=None):      #update employee
  
    try:
        if emp_id in Employees:
            if name:
                Employees[emp_id]["Name"] = name
            if DOB:
                Employees[emp_id]["DOB"] = DOB
            if department:
                Employees[emp_id]["Department"] = department
            if salary:
                Employees[emp_id]["Salary"] = salary
            if contact_number:
                Employees[emp_id]["Contact Number"] = contact_number
            if email:
                Employees[emp_id]["E-Mail"] = email
            if address:
                Employees[emp_id]["Address"] = address
            print(f"\nEmployee {emp_id} Updated Successfully!\n")
        else:
            print(f"\nEmployee with ID {emp_id} Not Found!\n")
    except KeyError as e:
        print(f"Error Updating Employee Details: {e}")


def delete_employee(emp_id):        # Delete an employee
    try:
        emp = Employees.pop(emp_id)
        print(f"\nEmployee with ID {emp_id} Removed Successfully!\n")
    except KeyError:
        print(f"\nEmployee with ID {emp_id} is Not Found!\n")


def menu():     # Main menu
    load_from_file(filename)

    while True:
        print("\nWelcome to The Employee Management System:\n")
        print("1. Add Employee")
        print("2. View Employee")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Save to File")
        print("6. Exit")

        try:
            choice = int(input("\nEnter Your Choice: "))
        except ValueError:
            print("Invalid choice. Please enter a number.")
            continue

        if choice == 1:
            try:
                emp_id = int(input("Enter the Employee ID: "))
                name = input("Enter the Employee Name: ")
                DOB = input("Enter Date of Birth in dd/mm/yyyy Format: ")
                department = input("Enter Department: ")
                salary = float(input("Enter Salary: "))
                contact_number = int(input("Enter Contact Number: "))
                email = input("Enter E-Mail: ")
                address = input("Enter Address: ")
                add_employee(emp_id, name, DOB, department, salary, contact_number, email, address)
            except ValueError:
                print("Invalid input. Please enter valid data.")

        elif choice == 2:
            view_employee()

        elif choice == 3:
            try:
                emp_id = int(input("Enter Employee ID to update: "))
                if emp_id not in Employees:
                    print("Employee ID not found.")
                    continue

                name = input("Enter New Name (Leave blank to skip): ") or None
                DOB = input("Enter New DOB (Leave blank to skip): ") or None
                department = input("Enter New Department (Leave blank to skip): ") or None

                salary_input = input("Enter New Salary (Leave blank to skip): ")
                salary = float(salary_input) if salary_input else None

                contact_input = input("Enter New Contact Number (Leave blank to skip): ")
                contact_number = int(contact_input) if contact_input else None

                email = input("Enter New E-Mail (Leave blank to skip): ") or None
                address = input("Enter New Address (Leave blank to skip): ") or None

                update_employee(emp_id, name, DOB, department, salary, contact_number, email, address)
            except ValueError:
                print("Invalid input. Please enter correct data types.")

        elif choice == 4:
            try:
                emp_id = int(input("Enter Employee ID to Remove: "))
                delete_employee(emp_id)
            except ValueError:
                print("Invalid Employee ID.")

        elif choice == 5:
            save_to_file(filename)

        elif choice == 6:
            save_to_file(filename)
            print("Exiting program..!")
            break

        else:
            print("Invalid choice. Please select from 1 to 6.")


menu()      #to run the program


