import pickle  # Importing pickle module to work with binary files
from tkinter import messagebox  # Importing the messagebox class from tkinter for displaying messages
import os  # Importing os module for file operations

class Employee:
    def __init__(self, name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id=None):
        # Constructor method to initialize Employee object with provided attributes
        self.name = name  # employee name
        self.emp_id = emp_id  # employee ID
        self.department = department  # employee department
        self.job_title = job_title  # employee job title
        self.basic_salary = basic_salary  # employee basic salary
        self.age = age  # employee age
        self.dob = dob  # employee date of birth
        self.passport_details = passport_details  # employee passport details
        self.manager_id = manager_id  # employee manager ID, default is None

    @staticmethod
    def add_employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id):
        # Static method to add a new employee to the data file
        new_employee = Employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id)  # Creating a new Employee object
        with open('data1', 'ab') as file:  # Opening the data file in binary append mode
            pickle.dump(new_employee, file)  # Serializing and writing the new employee object to the file
        messagebox.showinfo("Add Employee", "Employee added successfully.")  # Showing success message

    @staticmethod
    def display_employee_by_id(emp_id):
        # Static method to display employee details by ID
        with open('data1', 'rb') as file:  # Opening the data file in binary read mode
            try:
                while True:
                    employee = pickle.load(file)  # Deserializing and loading employee objects one by one
                    if employee.emp_id == emp_id:  # Checking if employee ID matches
                        message = f"Name: {employee.name}\nEmployee ID: {employee.emp_id}\nDepartment: {employee.department}\nJob Title: {employee.job_title}\nBasic Salary: {employee.basic_salary}\nAge: {employee.age}\nDate of Birth: {employee.dob}\nPassport Details: {employee.passport_details}\nManager ID: {employee.manager_id}"
                        messagebox.showinfo("Employee Details", message)  # Displaying employee details
                        break
            except EOFError:
                messagebox.showinfo("Employee Details", "Employee not found.")  # Showing message if employee not found

    @staticmethod
    def delete_employee_by_id(emp_id):
        # Static method to delete employee by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data1', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    employee = pickle.load(file)  # Deserializing and loading employee objects one by one
                    if employee.emp_id != emp_id:  # Checking if employee ID does not match
                        pickle.dump(employee, temp)  # Writing employee object to temporary file
            except EOFError:
                pass

        os.remove('data1')  # Removing original data file
        os.rename(temp_file, 'data1')  # Renaming temporary file to original name
        messagebox.showinfo("Delete Employee", "Employee deleted successfully.")  # Showing success message

    @staticmethod
    def edit_employee_by_id(emp_id, new_employee_data):
        # Static method to edit employee details by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data1', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    employee = pickle.load(file)  # Deserializing and loading employee objects one by one
                    if employee.emp_id == emp_id:  # Checking if employee ID matches
                        # Updating employee attributes with new data
                        employee.name = new_employee_data['name']
                        employee.department = new_employee_data['department']
                        employee.job_title = new_employee_data['job_title']
                        employee.basic_salary = new_employee_data['basic_salary']
                        employee.age = new_employee_data['age']
                        employee.dob = new_employee_data['dob']
                        employee.passport_details = new_employee_data['passport_details']
                        employee.manager_id = new_employee_data['manager_id']
                    pickle.dump(employee, temp)  # Writing employee object to temporary file
            except EOFError:
                pass

        os.remove('data1')  # Removing original data file
        os.rename(temp_file, 'data1')  # Renaming temporary file to original name
        messagebox.showinfo("Edit Employee", "Employee details updated successfully.")  # Showing success message
