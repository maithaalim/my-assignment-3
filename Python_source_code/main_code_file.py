import tkinter as tk  # Importing tkinter library and aliasing it as tk
from tkinter import messagebox  # Importing messagebox from tkinter for displaying messages
from employee_code_file import Employee  # Importing Employee class from employee_code_file
from client_code_file import Client  # Importing Client class from client_code_file
from event_code_file import Event  # Importing Event class from event_code_file
from supplier_code_file import Supplier  # Importing Supplier class from supplier_code_file
from venue_code_file import Venue  # Importing Venue class from venue_code_file
from guest_code_file import Guest  # Importing Guest class from guest_code_file
import pickle  # Importing pickle module for object serialization

def open_employee_form():
    # Function to open a form for managing employees
    
    # Creating a new window for employee management
    employee_window = tk.Toplevel(root)
    employee_window.title("Employee Management")
    employee_window.geometry("400x300")

    def add_employee():
        # Function to open a form for adding a new employee
        
        # Creating a new window for adding an employee
        add_window = tk.Toplevel(root)
        add_window.title("Add Employee")
        add_window.geometry("400x300")

        # Creating labels and entry fields for employee details
        tk.Label(add_window, text="Name:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Employee ID:").pack()
        emp_id_entry = tk.Entry(add_window)
        emp_id_entry.pack()

        tk.Label(add_window, text="Department:").pack()
        department_entry = tk.Entry(add_window)
        department_entry.pack()

        tk.Label(add_window, text="Job Title:").pack()
        job_title_entry = tk.Entry(add_window)
        job_title_entry.pack()

        tk.Label(add_window, text="Basic Salary:").pack()
        basic_salary_entry = tk.Entry(add_window)
        basic_salary_entry.pack()

        tk.Label(add_window, text="Age:").pack()
        age_entry = tk.Entry(add_window)
        age_entry.pack()

        tk.Label(add_window, text="Date of Birth:").pack()
        dob_entry = tk.Entry(add_window)
        dob_entry.pack()

        tk.Label(add_window, text="Passport Details:").pack()
        passport_details_entry = tk.Entry(add_window)
        passport_details_entry.pack()

        tk.Label(add_window, text="Manager ID (Optional):").pack()
        manager_id_entry = tk.Entry(add_window)
        manager_id_entry.pack()

        # Function to get data from entry fields and add the employee
        def add_employee_from_entry():
            # Extracting data from entry fields
            name = name_entry.get()
            emp_id = emp_id_entry.get()
            department = department_entry.get()
            job_title = job_title_entry.get()
            basic_salary = basic_salary_entry.get()
            age = age_entry.get()
            dob = dob_entry.get()
            passport_details = passport_details_entry.get()
            manager_id = manager_id_entry.get() if manager_id_entry.get() else None
            # Adding the employee using the Employee class method
            Employee.add_employee(name, emp_id, department, job_title, basic_salary, age, dob, passport_details, manager_id)
            add_window.destroy()

        # Button to add the employee
        add_btn = tk.Button(add_window, text="Add Employee", command=add_employee_from_entry)
        add_btn.pack(pady=10)
    
    def edit_employee():
        # Function to open a window for editing employee details
        
        # Creating a new window for editing an employee
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Employee")
        edit_window.geometry("400x300")

        # Creating a label and entry field for entering employee ID
        emp_id_label = tk.Label(edit_window, text="Employee ID:")
        emp_id_label.pack()
        emp_id_entry = tk.Entry(edit_window)
        emp_id_entry.pack()

        def fetch_employee_to_edit():
            # Function to fetch employee details for editing
            
            # Retrieving employee ID entered by the user
            emp_id = emp_id_entry.get()
            
            # Opening the data file containing employee information
            with open('data1', 'rb') as file:
                try:
                    while True:
                        # Loading employee objects from the file
                        employee = pickle.load(file)
                        
                        # Checking if the loaded employee's ID matches the entered ID
                        if employee.emp_id == emp_id:
                            fill_edit_form(employee)  # If matched, fill the edit form with employee details
                            break
                except EOFError:
                    messagebox.showinfo("Edit Employee", "Employee not found.")  # Display message if employee is not found

        def fill_edit_form(employee):
            # Create labels and entry fields for employee details
            tk.Label(edit_window, text="Name:").pack()
            name_entry = tk.Entry(edit_window)
            name_entry.insert(0, employee.name)
            name_entry.pack()

            tk.Label(edit_window, text="Employee ID:").pack()
            emp_id_entry = tk.Entry(edit_window)
            emp_id_entry.insert(0, employee.emp_id)
            emp_id_entry.pack()

            tk.Label(edit_window, text="Department:").pack()
            department_entry = tk.Entry(edit_window)
            department_entry.insert(0, employee.department)
            department_entry.pack()

            tk.Label(edit_window, text="Job Title:").pack()
            job_title_entry = tk.Entry(edit_window)
            job_title_entry.insert(0, employee.job_title)
            job_title_entry.pack()

            tk.Label(edit_window, text="Basic Salary:").pack()
            basic_salary_entry = tk.Entry(edit_window)
            basic_salary_entry.insert(0, employee.basic_salary)
            basic_salary_entry.pack()

            tk.Label(edit_window, text="Age:").pack()
            age_entry = tk.Entry(edit_window)
            age_entry.insert(0, employee.age)
            age_entry.pack()

            tk.Label(edit_window, text="Date of Birth:").pack()
            dob_entry = tk.Entry(edit_window)
            dob_entry.insert(0, employee.dob)
            dob_entry.pack()

            tk.Label(edit_window, text="Passport Details:").pack()
            passport_details_entry = tk.Entry(edit_window)
            passport_details_entry.insert(0, employee.passport_details)
            passport_details_entry.pack()

            tk.Label(edit_window, text="Manager ID (Optional):").pack()
            manager_id_entry = tk.Entry(edit_window)
            manager_id_entry.insert(0, employee.manager_id if employee.manager_id else "")
            manager_id_entry.pack()

            def save_edited_employee():
                new_employee_data = {
                    'name': name_entry.get(),
                    'department': department_entry.get(),
                    'job_title': job_title_entry.get(),
                    'basic_salary': basic_salary_entry.get(),
                    'age': age_entry.get(),
                    'dob': dob_entry.get(),
                    'passport_details': passport_details_entry.get(),
                    'manager_id': manager_id_entry.get() if manager_id_entry.get() else None
                }
                Employee.edit_employee_by_id(emp_id_entry.get(), new_employee_data)
                edit_window.destroy()

            # Button to save edited employee details
            save_btn = tk.Button(edit_window, text="Save", command=save_edited_employee)
            save_btn.pack(pady=10)

        fetch_btn = tk.Button(edit_window, text="Fetch Employee", command=fetch_employee_to_edit)
        fetch_btn.pack(pady=10)

    # Function to delete employee                              
    def delete_employee():
        # NEw window creation for delete
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Employee")
        delete_window.geometry("300x100")

        tk.Label(delete_window, text="Enter Employee ID:").pack()
        emp_id_entry = tk.Entry(delete_window)
        emp_id_entry.pack()

        # Confirmation message 
        def confirm_deletion():
            emp_id = emp_id_entry.get()
            Employee.delete_employee_by_id(emp_id)

        delete_btn = tk.Button(delete_window, text="Delete Employee", command=confirm_deletion)
        delete_btn.pack(pady=10)
    
    # Function to display employee details
    def display_employee():
        # Creating a window to display employee details
        display_window = tk.Toplevel(root)
        display_window.title("Display Employee")
        display_window.geometry("300x100")

        # Label and entry field for entering employee ID
        tk.Label(display_window, text="Enter Employee ID:").pack()
        emp_id_entry = tk.Entry(display_window)
        emp_id_entry.pack()

        def fetch_employee_details():
            # Function to fetch and display employee details
            
            # Getting the employee ID entered by the user
            emp_id = emp_id_entry.get()
            
            # Calling a function to display employee details based on the entered ID
            Employee.display_employee_by_id(emp_id)

        # Button to trigger fetching and displaying employee details
        display_btn = tk.Button(display_window, text="Display Employee", command=fetch_employee_details)
        display_btn.pack(pady=10)

    # Button to add a new employee, triggers the add_employee function when clicked
    add_btn = tk.Button(employee_window, text="Add", command=add_employee, width=20)
    add_btn.pack(pady=10)

    # Button to edit an existing employee, triggers the edit_employee function when clicked
    edit_btn = tk.Button(employee_window, text="Edit", command=edit_employee, width=20)
    edit_btn.pack(pady=10)

    # Button to delete an existing employee, triggers the delete_employee function when clicked
    delete_btn = tk.Button(employee_window, text="Delete", command=delete_employee, width=20)
    delete_btn.pack(pady=10)

    # Button to display details of an employee, triggers the display_employee function when clicked
    display_btn = tk.Button(employee_window, text="Display", command=display_employee, width=20)
    display_btn.pack(pady=10)

# Function to open a form for managing clients
def open_client_form():
    # Create a new window for client management
    client_window = tk.Toplevel(root)
    client_window.title("Client Management")
    client_window.geometry("400x300")

    # Function to add a new client
    def add_client():
        # Create a new window for adding a client
        add_window = tk.Toplevel(root)
        add_window.title("Add Client")
        add_window.geometry("400x300")

        # Create labels and entry fields for client details
        tk.Label(add_window, text="Name:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Client ID:").pack()
        client_id_entry = tk.Entry(add_window)
        client_id_entry.pack()

        tk.Label(add_window, text="Address:").pack()
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        tk.Label(add_window, text="Contact Details:").pack()
        contact_details_entry = tk.Entry(add_window)
        contact_details_entry.pack()

        tk.Label(add_window, text="Budget:").pack()
        budget_entry = tk.Entry(add_window)
        budget_entry.pack()

        # Function to get data from entry fields and add the client
        def add_client_from_entry():
            name = name_entry.get()
            client_id = client_id_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()
            budget = budget_entry.get()

            # Call the add_client function of the Client class
            Client.add_client(client_id, name, address, contact_details, budget)
            add_window.destroy()

        # Button to add the client
        add_btn = tk.Button(add_window, text="Add Client", command=add_client_from_entry)
        add_btn.pack(pady=10)

    # Function to open a window for editing a client
    def edit_client():
        # Create a new window for editing a client
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Client")
        edit_window.geometry("400x300")

        # Create a label and an entry field for entering the client ID
        client_id_label = tk.Label(edit_window, text="Client ID:")
        client_id_label.pack()
        client_id_entry = tk.Entry(edit_window)
        client_id_entry.pack()

        # Function to fetch the client details for editing
        def fetch_client_to_edit():
            # Get the client ID entered by the user
            client_id = client_id_entry.get()
            
            # Open the data file containing client information
            with open('data2', 'rb') as file:
                try:
                    # Loop through each client in the file
                    while True:
                        # Load the client data from the file
                        client = pickle.load(file)
                        
                        # Check if the client ID matches the one entered by the user
                        if client.client_id == client_id:
                            # If a matching client is found, fill the edit form with client details
                            fill_edit_form(client)
                            break
                except EOFError:
                    # If the end of the file is reached and no matching client is found, show a message
                    messagebox.showinfo("Edit Client", "Client not found.")


        def fill_edit_form(client):
            # Create labels and entry fields for client details
            tk.Label(edit_window, text="Name:").pack()
            name_entry = tk.Entry(edit_window)
            name_entry.insert(0, client.name)
            name_entry.pack()

            tk.Label(edit_window, text="Client ID:").pack()
            client_id_entry = tk.Entry(edit_window)
            client_id_entry.insert(0, client.client_id)
            client_id_entry.pack()

            tk.Label(edit_window, text="Address:").pack()
            address_entry = tk.Entry(edit_window)
            address_entry.insert(0, client.address)
            address_entry.pack()

            tk.Label(edit_window, text="Contact Details:").pack()
            contact_details_entry = tk.Entry(edit_window)
            contact_details_entry.insert(0, client.contact_details)
            contact_details_entry.pack()

            tk.Label(edit_window, text="Budget:").pack()
            budget_entry = tk.Entry(edit_window)
            budget_entry.insert(0, client.budget)
            budget_entry.pack()

            # Function to save the edited client details
            def save_edited_client():
                # Get the new client details entered by the user
                new_client_data = {
                    'name': name_entry.get(),
                    'address': address_entry.get(),
                    'contact_details': contact_details_entry.get(),
                    'budget': budget_entry.get(),
                }
                
                # Call the edit_client_by_id function of the Client class with the new client data
                Client.edit_client_by_id(client.client_id, new_client_data)
                
                # Close the edit window after saving the changes
                edit_window.destroy()

            # Button to trigger saving edited client details
            save_btn = tk.Button(edit_window, text="Save", command=save_edited_client)
            save_btn.pack(pady=10)

            # Button to fetch the client to be edited
            fetch_btn = tk.Button(edit_window, text="Fetch Client", command=fetch_client_to_edit)
            fetch_btn.pack(pady=10)

    # Function to handle client deletion
    def delete_client():
        # Create a new window for deleting a client
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Client")
        delete_window.geometry("300x100")

        # Label and entry field for entering the client ID to be deleted
        tk.Label(delete_window, text="Enter Client ID:").pack()
        client_id_entry = tk.Entry(delete_window)
        client_id_entry.pack()

        # Function to confirm deletion when the delete button is clicked
        def confirm_deletion():
            # Get the client ID entered by the user
            client_id = client_id_entry.get()
            
            # Call the delete_client_by_id function of the Client class to delete the client
            Client.delete_client_by_id(client_id)

        # Button to trigger client deletion when clicked
        delete_btn = tk.Button(delete_window, text="Delete Client", command=confirm_deletion)
        delete_btn.pack(pady=10)


   # Function to display client details
    def display_client():
        # Create a new window for displaying client details
        display_window = tk.Toplevel(root)
        display_window.title("Display Client")
        display_window.geometry("300x100")

        # Label and entry field for entering the client ID to be displayed
        tk.Label(display_window, text="Enter Client ID:").pack()
        client_id_entry = tk.Entry(display_window)
        client_id_entry.pack()

        # Function to fetch and display client details when the display button is clicked
        def fetch_client_details():
            # Get the client ID entered by the user
            client_id = client_id_entry.get()
            
            # Call the display_client_by_id function of the Client class to fetch and display client details
            Client.display_client_by_id(client_id)

        # Button to trigger fetching and displaying client details when clicked
        display_btn = tk.Button(display_window, text="Display Client", command=fetch_client_details)
        display_btn.pack(pady=10)

    # Buttons to perform different client operations (Add, Edit, Delete, Display)
    add_btn = tk.Button(client_window, text="Add", command=add_client, width=20)
    add_btn.pack(pady=10)

    edit_btn = tk.Button(client_window, text="Edit", command=edit_client, width=20)
    edit_btn.pack(pady=10)

    delete_btn = tk.Button(client_window, text="Delete", command=delete_client, width=20)
    delete_btn.pack(pady=10)

    display_btn = tk.Button(client_window, text="Display", command=display_client, width=20)
    display_btn.pack(pady=10)


# Function to open the supplier management form
def open_supplier_form():
    # Create a new window for managing suppliers
    supplier_window = tk.Toplevel(root)
    supplier_window.title("Supplier Management")
    supplier_window.geometry("400x300")

    # Function to add a new supplier
    def add_supplier():
        # Create a new window for adding a supplier
        add_window = tk.Toplevel(root)
        add_window.title("Add Supplier")
        add_window.geometry("400x300")

        # Create labels and entry fields for entering supplier details
        tk.Label(add_window, text="Name:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Supplier ID:").pack()
        supplier_id_entry = tk.Entry(add_window)
        supplier_id_entry.pack()

        tk.Label(add_window, text="Address:").pack()
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        tk.Label(add_window, text="Contact Details:").pack()
        contact_details_entry = tk.Entry(add_window)
        contact_details_entry.pack()

        tk.Label(add_window, text="Menu:").pack()
        menu_entry = tk.Entry(add_window)
        menu_entry.pack()

        tk.Label(add_window, text="Minimum Guests:").pack()
        min_guests_entry = tk.Entry(add_window)
        min_guests_entry.pack()

        tk.Label(add_window, text="Maximum Guests:").pack()
        max_guests_entry = tk.Entry(add_window)
        max_guests_entry.pack()


        # Function to get data from entry fields and add the supplier
        def add_supplier_from_entry():
            name = name_entry.get()
            supplier_id = supplier_id_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()
            menu = menu_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            # Call the add_supplier function of the Supplier class
            Supplier.add_supplier(supplier_id, name, address, contact_details, menu, min_guests, max_guests)
            add_window.destroy()

        # Button to add the supplier
        add_btn = tk.Button(add_window, text="Add Supplier", command=add_supplier_from_entry)
        add_btn.pack(pady=10)

    # Function to open the edit supplier window
    def edit_supplier():
        # Create a new window for editing suppliers
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Supplier")
        edit_window.geometry("400x300")

        # Create label and entry field for entering supplier ID
        supplier_id_label = tk.Label(edit_window, text="Supplier ID:")
        supplier_id_label.pack()
        supplier_id_entry = tk.Entry(edit_window)
        supplier_id_entry.pack()

        # Function to fetch supplier details for editing
        def fetch_supplier_to_edit():
            # Get the supplier ID entered by the user
            supplier_id = supplier_id_entry.get()
            
            # Open the data file containing supplier information
            with open('data5', 'rb') as file:
                try:
                    # Loop through each entry in the file
                    while True:
                        # Load each supplier from the file
                        supplier = pickle.load(file)
                        
                        # If the supplier ID matches the entered ID, fill the edit form
                        if supplier.supplier_id == supplier_id:
                            fill_edit_form(supplier)
                            break
                except EOFError:
                    # If the end of file is reached and no match is found, display a message
                    messagebox.showinfo("Edit Supplier", "Supplier not found.")


        def fill_edit_form(supplier):
            # Create labels and entry fields for supplier details
            tk.Label(edit_window, text="Name:").pack()
            name_entry = tk.Entry(edit_window)
            name_entry.insert(0, supplier.name)
            name_entry.pack()

            tk.Label(edit_window, text="Supplier ID:").pack()
            supplier_id_entry = tk.Entry(edit_window)
            supplier_id_entry.insert(0, supplier.supplier_id)
            supplier_id_entry.pack()

            tk.Label(edit_window, text="Address:").pack()
            address_entry = tk.Entry(edit_window)
            address_entry.insert(0, supplier.address)
            address_entry.pack()

            tk.Label(edit_window, text="Contact Details:").pack()
            contact_details_entry = tk.Entry(edit_window)
            contact_details_entry.insert(0, supplier.contact_details)
            contact_details_entry.pack()

            tk.Label(edit_window, text="Menu:").pack()
            menu_entry = tk.Entry(edit_window)
            menu_entry.insert(0, supplier.menu)
            menu_entry.pack()

            tk.Label(edit_window, text="Minimum Guests:").pack()
            min_guests_entry = tk.Entry(edit_window)
            min_guests_entry.insert(0, supplier.min_guests)
            min_guests_entry.pack()

            tk.Label(edit_window, text="Maximum Guests:").pack()
            max_guests_entry = tk.Entry(edit_window)
            max_guests_entry.insert(0, supplier.max_guests)
            max_guests_entry.pack()

            def save_edited_supplier():
                new_supplier_data = {
                    'name': name_entry.get(),
                    'address': address_entry.get(),
                    'contact_details': contact_details_entry.get(),
                    'menu': menu_entry.get(),
                    'min_guests': min_guests_entry.get(),
                    'max_guests': max_guests_entry.get(),
                }
                # Call the edit_supplier_by_id function of the Supplier class
                Supplier.edit_supplier_by_id(supplier_id_entry.get(), new_supplier_data)
                edit_window.destroy()

            # Button to save edited supplier details
            save_btn = tk.Button(edit_window, text="Save", command=save_edited_supplier)
            save_btn.pack(pady=10)

        fetch_btn = tk.Button(edit_window, text="Fetch Supplier", command=fetch_supplier_to_edit)
        fetch_btn.pack(pady=10)

    def delete_supplier():
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Supplier")
        delete_window.geometry("300x100")

        tk.Label(delete_window, text="Enter Supplier ID:").pack()
        supplier_id_entry = tk.Entry(delete_window)
        supplier_id_entry.pack()

        def confirm_deletion():
            supplier_id = supplier_id_entry.get()
            # Call the delete_supplier_by_id function of the Supplier class
            Supplier.delete_supplier_by_id(supplier_id)

        delete_btn = tk.Button(delete_window, text="Delete Supplier", command=confirm_deletion)
        delete_btn.pack(pady=10)

    # Function to open the display supplier window
    def display_supplier():
        # Create a new window for displaying supplier details
        display_window = tk.Toplevel(root)
        display_window.title("Display Supplier")
        display_window.geometry("300x100")

        # Create label and entry field for entering supplier ID
        tk.Label(display_window, text="Enter Supplier ID:").pack()
        supplier_id_entry = tk.Entry(display_window)
        supplier_id_entry.pack()

        # Function to fetch and display supplier details
        def fetch_supplier_details():
            # Get the supplier ID entered by the user
            supplier_id = supplier_id_entry.get()
            
            # Call the display_supplier_by_id function of the Supplier class with the entered ID
            Supplier.display_supplier_by_id(supplier_id)

        # Button to trigger the fetching and displaying of supplier details
        display_btn = tk.Button(display_window, text="Display Supplier", command=fetch_supplier_details)
        display_btn.pack(pady=10)

    # Create buttons for adding, editing, deleting, and displaying suppliers
    add_btn = tk.Button(supplier_window, text="Add", command=add_supplier, width=20)
    add_btn.pack(pady=10)

    edit_btn = tk.Button(supplier_window, text="Edit", command=edit_supplier, width=20)
    edit_btn.pack(pady=10)

    delete_btn = tk.Button(supplier_window, text="Delete", command=delete_supplier, width=20)
    delete_btn.pack(pady=10)

    display_btn = tk.Button(supplier_window, text="Display", command=display_supplier, width=20)
    display_btn.pack(pady=10)


# Function to open the venue management form
def open_venue_form():
    # Create a new window for venue management
    venue_window = tk.Toplevel(root)
    venue_window.title("Venue Management")
    venue_window.geometry("400x300")

    # Function to add a new venue
    def add_venue():
        # Create a new window for adding a venue
        add_window = tk.Toplevel(root)
        add_window.title("Add Venue")
        add_window.geometry("400x300")

        # Create labels and entry fields for venue details
        tk.Label(add_window, text="Name:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Venue ID:").pack()
        venue_id_entry = tk.Entry(add_window)
        venue_id_entry.pack()

        tk.Label(add_window, text="Address:").pack()
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        tk.Label(add_window, text="Contact:").pack()
        contact_entry = tk.Entry(add_window)
        contact_entry.pack()

        tk.Label(add_window, text="Minimum Guests:").pack()
        min_guests_entry = tk.Entry(add_window)
        min_guests_entry.pack()

        tk.Label(add_window, text="Maximum Guests:").pack()
        max_guests_entry = tk.Entry(add_window)
        max_guests_entry.pack()

        # Function to get data from entry fields and add the venue
        def add_venue_from_entry():
            name = name_entry.get()
            venue_id = venue_id_entry.get()
            address = address_entry.get()
            contact = contact_entry.get()
            min_guests = min_guests_entry.get()
            max_guests = max_guests_entry.get()

            Venue.add_venue(venue_id, name, address, contact, min_guests, max_guests)
            add_window.destroy()

        # Button to add the venue
        add_btn = tk.Button(add_window, text="Add Venue", command=add_venue_from_entry)
        add_btn.pack(pady=10)

    # Function to open the venue editing form
    def edit_venue():
        # Create a new window for editing venue details
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Venue")
        edit_window.geometry("400x300")

        # Create a label and entry field for entering the venue ID
        venue_id_label = tk.Label(edit_window, text="Venue ID:")
        venue_id_label.pack()
        venue_id_entry = tk.Entry(edit_window)
        venue_id_entry.pack()

        # Function to fetch the venue details to edit
        def fetch_venue_to_edit():
            # Get the venue ID entered by the user
            venue_id = venue_id_entry.get()
            # Open the file containing venue data
            with open('data4', 'rb') as file:
                try:
                    # Iterate through each venue object in the file
                    while True:
                        venue = pickle.load(file)
                        # Check if the venue ID matches the entered ID
                        if venue.venue_id == venue_id:
                            # Call a function to fill the edit form with venue details
                            fill_edit_form(venue)
                            break
                # Handle the end of file error
                except EOFError:
                    # Display a message if the venue is not found
                    messagebox.showinfo("Edit Venue", "Venue not found.")

        def fill_edit_form(venue):
            # Create labels and entry fields for venue details
            tk.Label(edit_window, text="Name:").pack()
            name_entry = tk.Entry(edit_window)
            name_entry.insert(0, venue.name)
            name_entry.pack()

            tk.Label(edit_window, text="Venue ID:").pack()
            venue_id_entry = tk.Entry(edit_window)
            venue_id_entry.insert(0, venue.venue_id)
            venue_id_entry.pack()

            tk.Label(edit_window, text="Address:").pack()
            address_entry = tk.Entry(edit_window)
            address_entry.insert(0, venue.address)
            address_entry.pack()

            tk.Label(edit_window, text="Contact:").pack()
            contact_entry = tk.Entry(edit_window)
            contact_entry.insert(0, venue.contact)
            contact_entry.pack()

            tk.Label(edit_window, text="Minimum Guests:").pack()
            min_guests_entry = tk.Entry(edit_window)
            min_guests_entry.insert(0, venue.min_guests)
            min_guests_entry.pack()

            tk.Label(edit_window, text="Maximum Guests:").pack()
            max_guests_entry = tk.Entry(edit_window)
            max_guests_entry.insert(0, venue.max_guests)
            max_guests_entry.pack()

            def save_edited_venue():
                new_venue_data = {
                    'name': name_entry.get(),
                    'address': address_entry.get(),
                    'contact': contact_entry.get(),
                    'min_guests': min_guests_entry.get(),
                    'max_guests': max_guests_entry.get(),
                }
                Venue.edit_venue_by_id(venue_id_entry.get(), new_venue_data)
                edit_window.destroy()

            # Button to save edited venue details
            save_btn = tk.Button(edit_window, text="Save", command=save_edited_venue)
            save_btn.pack(pady=10)

        fetch_btn = tk.Button(edit_window, text="Fetch Venue", command=fetch_venue_to_edit)
        fetch_btn.pack(pady=10)

    def delete_venue():
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Venue")
        delete_window.geometry("300x100")

        tk.Label(delete_window, text="Enter Venue ID:").pack()
        venue_id_entry = tk.Entry(delete_window)
        venue_id_entry.pack()

        def confirm_deletion():
            venue_id = venue_id_entry.get()
            Venue.delete_venue_by_id(venue_id)

        delete_btn = tk.Button(delete_window, text="Delete Venue", command=confirm_deletion)
        delete_btn.pack(pady=10)

    def display_venue():
        display_window = tk.Toplevel(root)
        display_window.title("Display Venue")
        display_window.geometry("300x100")

        tk.Label(display_window, text="Enter Venue ID:").pack()
        venue_id_entry = tk.Entry(display_window)
        venue_id_entry.pack()

        def fetch_venue_details():
            venue_id = venue_id_entry.get()
            Venue.display_venue_by_id(venue_id)

        display_btn = tk.Button(display_window, text="Display Venue", command=fetch_venue_details)
        display_btn.pack(pady=10)

    add_btn = tk.Button(venue_window, text="Add", command=add_venue, width=20)
    add_btn.pack(pady=10)

    edit_btn = tk.Button(venue_window, text="Edit", command=edit_venue, width=20)
    edit_btn.pack(pady=10)

    delete_btn = tk.Button(venue_window, text="Delete", command=delete_venue, width=20)
    delete_btn.pack(pady=10)

    display_btn = tk.Button(venue_window, text="Display", command=display_venue, width=20)
    display_btn.pack(pady=10)

def open_event_form():
    event_window = tk.Toplevel(root)
    event_window.title("Event Management")
    event_window.geometry("400x300")

    def add_event():
        add_window = tk.Toplevel(root)
        add_window.title("Add Event")
        add_window.geometry("400x300")

        # Create labels and entry fields for event details
        tk.Label(add_window, text="Event ID:").pack()
        event_id_entry = tk.Entry(add_window)
        event_id_entry.pack()

        tk.Label(add_window, text="Event Type:").pack()
        event_type_entry = tk.Entry(add_window)
        event_type_entry.pack()

        tk.Label(add_window, text="Theme:").pack()
        theme_entry = tk.Entry(add_window)
        theme_entry.pack()

        tk.Label(add_window, text="Date:").pack()
        date_entry = tk.Entry(add_window)
        date_entry.pack()

        tk.Label(add_window, text="Time:").pack()
        time_entry = tk.Entry(add_window)
        time_entry.pack()

        tk.Label(add_window, text="Duration:").pack()
        duration_entry = tk.Entry(add_window)
        duration_entry.pack()

        tk.Label(add_window, text="Venue Address:").pack()
        venue_address_entry = tk.Entry(add_window)
        venue_address_entry.pack()

        tk.Label(add_window, text="Client ID:").pack()
        client_id_entry = tk.Entry(add_window)
        client_id_entry.pack()

        tk.Label(add_window, text="Guest List:").pack()
        guest_list_entry = tk.Entry(add_window)
        guest_list_entry.pack()

        tk.Label(add_window, text="Suppliers:").pack()
        suppliers_entry = tk.Entry(add_window)
        suppliers_entry.pack()

        # Function to get data from entry fields and add the event
        def add_event_from_entry():
            event_id = event_id_entry.get()
            event_type = event_type_entry.get()
            theme = theme_entry.get()
            date = date_entry.get()
            time = time_entry.get()
            duration = duration_entry.get()
            venue_address = venue_address_entry.get()
            client_id = client_id_entry.get()
            guest_list = guest_list_entry.get()
            suppliers = suppliers_entry.get()

            Event.add_event(event_id,event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers)
            add_window.destroy()

        # Button to add the event
        add_btn = tk.Button(add_window, text="Add Event", command=add_event_from_entry)
        add_btn.pack(pady=10)
    
    def edit_event():
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Event")
        edit_window.geometry("400x300")

        event_id_label = tk.Label(edit_window, text="Event ID:")
        event_id_label.pack()
        event_id_entry = tk.Entry(edit_window)
        event_id_entry.pack()

        def fetch_event_to_edit():
            event_id = event_id_entry.get()
            with open('data6', 'rb') as file:
                try:
                    while True:
                        event = pickle.load(file)
                        if event.event_id == event_id:
                            fill_edit_form(event)
                            break
                except EOFError:
                    messagebox.showinfo("Edit Event", "Event not found.")

        def fill_edit_form(event):
            # Create labels and entry fields for event details
            tk.Label(edit_window, text="Event Type:").pack()
            event_type_entry = tk.Entry(edit_window)
            event_type_entry.insert(0, event.event_type)
            event_type_entry.pack()

            tk.Label(edit_window, text="Theme:").pack()
            theme_entry = tk.Entry(edit_window)
            theme_entry.insert(0, event.theme)
            theme_entry.pack()

            tk.Label(edit_window, text="Date:").pack()
            date_entry = tk.Entry(edit_window)
            date_entry.insert(0, event.date)
            date_entry.pack()

            tk.Label(edit_window, text="Time:").pack()
            time_entry = tk.Entry(edit_window)
            time_entry.insert(0, event.time)
            time_entry.pack()

            tk.Label(edit_window, text="Duration:").pack()
            duration_entry = tk.Entry(edit_window)
            duration_entry.insert(0, event.duration)
            duration_entry.pack()

            tk.Label(edit_window, text="Venue Address:").pack()
            venue_address_entry = tk.Entry(edit_window)
            venue_address_entry.insert(0, event.venue_address)
            venue_address_entry.pack()

            tk.Label(edit_window, text="Client ID:").pack()
            client_id_entry = tk.Entry(edit_window)
            client_id_entry.insert(0, event.client_id)
            client_id_entry.pack()

            tk.Label(edit_window, text="Guest List:").pack()
            guest_list_entry = tk.Entry(edit_window)
            guest_list_entry.insert(0, event.guest_list)
            guest_list_entry.pack()

            tk.Label(edit_window, text="Suppliers:").pack()
            suppliers_entry = tk.Entry(edit_window)
            suppliers_entry.insert(0, event.suppliers)
            suppliers_entry.pack()

            def save_edited_event():
                new_event_data = {
                    'event_type': event_type_entry.get(),
                    'theme': theme_entry.get(),
                    'date': date_entry.get(),
                    'time': time_entry.get(),
                    'duration': duration_entry.get(),
                    'venue_address': venue_address_entry.get(),
                    'client_id': client_id_entry.get(),
                    'guest_list': guest_list_entry.get(),
                    'suppliers': suppliers_entry.get(),
                }
                Event.edit_event_by_id(event_id_entry.get(), new_event_data)
                edit_window.destroy()

            # Button to save edited event details
            save_btn = tk.Button(edit_window, text="Save", command=save_edited_event)
            save_btn.pack(pady=10)

        fetch_btn = tk.Button(edit_window, text="Fetch Event", command=fetch_event_to_edit)
        fetch_btn.pack(pady=10)

    def delete_event():
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Event")
        delete_window.geometry("300x100")

        tk.Label(delete_window, text="Enter Event ID:").pack()
        event_id_entry = tk.Entry(delete_window)
        event_id_entry.pack()

        def confirm_deletion():
            event_id = event_id_entry.get()
            Event.delete_event_by_id(event_id)

        delete_btn = tk.Button(delete_window, text="Delete Event", command=confirm_deletion)
        delete_btn.pack(pady=10)
    
    def display_event():
        display_window = tk.Toplevel(root)
        display_window.title("Display Event")
        display_window.geometry("300x100")

        tk.Label(display_window, text="Enter Event ID:").pack()
        event_id_entry = tk.Entry(display_window)
        event_id_entry.pack()

        def fetch_event_details():
            event_id = event_id_entry.get()
            Event.display_event_by_id(event_id)

        display_btn = tk.Button(display_window, text="Display Event", command=fetch_event_details)
        display_btn.pack(pady=10)

    add_btn = tk.Button(event_window, text="Add", command=add_event, width=20)
    add_btn.pack(pady=10)

    edit_btn = tk.Button(event_window, text="Edit", command=edit_event, width=20)
    edit_btn.pack(pady=10)

    delete_btn = tk.Button(event_window, text="Delete", command=delete_event, width=20)
    delete_btn.pack(pady=10)

    display_btn = tk.Button(event_window, text="Display", command=display_event, width=20)
    display_btn.pack(pady=10)

def open_guest_form():
    guest_window = tk.Toplevel(root)
    guest_window.title("Guest Management")
    guest_window.geometry("400x300")

    def add_guest():
        add_window = tk.Toplevel(root)
        add_window.title("Add Guest")
        add_window.geometry("400x300")

        # Create labels and entry fields for guest details
        tk.Label(add_window, text="Name:").pack()
        name_entry = tk.Entry(add_window)
        name_entry.pack()

        tk.Label(add_window, text="Guest ID:").pack()
        guest_id_entry = tk.Entry(add_window)
        guest_id_entry.pack()

        tk.Label(add_window, text="Address:").pack()
        address_entry = tk.Entry(add_window)
        address_entry.pack()

        tk.Label(add_window, text="Contact Details:").pack()
        contact_details_entry = tk.Entry(add_window)
        contact_details_entry.pack()

        # Function to get data from entry fields and add the guest
        def add_guest_from_entry():
            name = name_entry.get()
            guest_id = guest_id_entry.get()
            address = address_entry.get()
            contact_details = contact_details_entry.get()

            Guest.add_guest(guest_id, name, address, contact_details)
            add_window.destroy()

        # Button to add the guest
        add_btn = tk.Button(add_window, text="Add Guest", command=add_guest_from_entry)
        add_btn.pack(pady=10)

    def edit_guest():
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Guest")
        edit_window.geometry("400x300")

        guest_id_label = tk.Label(edit_window, text="Guest ID:")
        guest_id_label.pack()
        guest_id_entry = tk.Entry(edit_window)
        guest_id_entry.pack()

        def fetch_guest_to_edit():
            guest_id = guest_id_entry.get()
            with open('data3', 'rb') as file:
                try:
                    while True:
                        guest = pickle.load(file)
                        if guest.guest_id == guest_id:
                            fill_edit_form(guest)
                            break
                except EOFError:
                    messagebox.showinfo("Edit Guest", "Guest not found.")

        def fill_edit_form(guest):
            # Create labels and entry fields for guest details
            tk.Label(edit_window, text="Name:").pack()
            name_entry = tk.Entry(edit_window)
            name_entry.insert(0, guest.name)
            name_entry.pack()

            tk.Label(edit_window, text="Guest ID:").pack()
            guest_id_entry = tk.Entry(edit_window)
            guest_id_entry.insert(0, guest.guest_id)
            guest_id_entry.pack()

            tk.Label(edit_window, text="Address:").pack()
            address_entry = tk.Entry(edit_window)
            address_entry.insert(0, guest.address)
            address_entry.pack()

            tk.Label(edit_window, text="Contact Details:").pack()
            contact_details_entry = tk.Entry(edit_window)
            contact_details_entry.insert(0, guest.contact_details)
            contact_details_entry.pack()

            def save_edited_guest():
                new_guest_data = {
                    'name': name_entry.get(),
                    'address': address_entry.get(),
                    'contact_details': contact_details_entry.get(),
                }
                Guest.edit_guest_by_id(guest_id_entry.get(), new_guest_data)
                edit_window.destroy()

            # Button to save edited guest details
            save_btn = tk.Button(edit_window, text="Save", command=save_edited_guest)
            save_btn.pack(pady=10)

        fetch_btn = tk.Button(edit_window, text="Fetch Guest", command=fetch_guest_to_edit)
        fetch_btn.pack(pady=10)

    def delete_guest():
        delete_window = tk.Toplevel(root)
        delete_window.title("Delete Guest")
        delete_window.geometry("300x100")

        tk.Label(delete_window, text="Enter Guest ID:").pack()
        guest_id_entry = tk.Entry(delete_window)
        guest_id_entry.pack()

        def confirm_deletion():
            guest_id = guest_id_entry.get()
            Guest.delete_guest_by_id(guest_id)

        delete_btn = tk.Button(delete_window, text="Delete Guest", command=confirm_deletion)
        delete_btn.pack(pady=10)

    def display_guest():
        display_window = tk.Toplevel(root)
        display_window.title("Display Guest")
        display_window.geometry("300x100")

        tk.Label(display_window, text="Enter Guest ID:").pack()
        guest_id_entry = tk.Entry(display_window)
        guest_id_entry.pack()

        def fetch_guest_details():
            guest_id = guest_id_entry.get()
            Guest.display_guest_by_id(guest_id)

        display_btn = tk.Button(display_window, text="Display Guest", command=fetch_guest_details)
        display_btn.pack(pady=10)

    add_btn = tk.Button(guest_window, text="Add", command=add_guest, width=20)
    add_btn.pack(pady=10)

    edit_btn = tk.Button(guest_window, text="Edit", command=edit_guest, width=20)
    edit_btn.pack(pady=10)

    delete_btn = tk.Button(guest_window, text="Delete", command=delete_guest, width=20)
    delete_btn.pack(pady=10)

    display_btn = tk.Button(guest_window, text="Display", command=display_guest, width=20)
    display_btn.pack(pady=10)

def main():
    # Initialize the main window of the application
    global root
    root = tk.Tk()
    root.title("Event Management System")  # Set the title of the window
    root.geometry("400x300")  # Set the initial size of the window

    # Menu bar setup
    menu = tk.Menu(root)  # Create a menu bar
    root.config(menu=menu)  # Configure the menu bar

    # Create a file menu with an exit command
    file_menu = tk.Menu(menu, tearoff=0)
    file_menu.add_command(label="Exit", command=root.quit)

    # Main Menu Buttons
    # Create buttons for different management sections and place them in the main window
    employee_btn = tk.Button(root, text="Employee", command=open_employee_form, width=20)
    employee_btn.place(relx=0.5, rely=0.2, anchor="center")  # Position the button in the window

    client_btn = tk.Button(root, text="Client", command=open_client_form, width=20)
    client_btn.place(relx=0.5, rely=0.3, anchor="center")

    supplier_btn = tk.Button(root, text="Supplier", command=open_supplier_form, width=20)
    supplier_btn.place(relx=0.5, rely=0.4, anchor="center")

    venue_btn = tk.Button(root, text="Venue", command=open_venue_form, width=20)
    venue_btn.place(relx=0.5, rely=0.5, anchor="center")

    event_btn = tk.Button(root, text="Event", command=open_event_form, width=20)
    event_btn.place(relx=0.5, rely=0.6, anchor="center")

    guest_btn = tk.Button(root, text="Guest", command=open_guest_form, width=20)
    guest_btn.place(relx=0.5, rely=0.7, anchor="center")

    root.mainloop()  # Start the event loop to display the main window 


if __name__ == "__main__":
    main()
