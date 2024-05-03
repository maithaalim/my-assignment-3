import pickle  # Importing pickle for object serialization
from tkinter import messagebox  # Importing messagebox from tkinter for displaying messages
import os  # Importing os for file operations

class Supplier:
    def __init__(self, supplier_id, name, address, contact_details, menu=None, min_guests=None, max_guests=None):
        # Initializing Supplier object with provided attributes
        self.supplier_id = supplier_id  # Supplier ID
        self.name = name  # Supplier name
        self.address = address  # Supplier address
        self.contact_details = contact_details  # Supplier contact details
        self.menu = menu  # Supplier menu (optional)
        self.min_guests = min_guests  # Minimum number of guests (optional)
        self.max_guests = max_guests  # Maximum number of guests (optional)

    @staticmethod
    def add_supplier(supplier_id, name, address, contact_details, menu=None, min_guests=None, max_guests=None):
        # Static method to add a new supplier to the data file
        new_supplier = Supplier(supplier_id, name, address, contact_details, menu, min_guests, max_guests)  # Creating a new Supplier object
        with open('data5', 'ab') as file:  # Opening the data file in binary append mode
            pickle.dump(new_supplier, file)  # Serializing and writing the new supplier object to the file
        messagebox.showinfo("Add Supplier", "Supplier added successfully.")  # Showing success message

    @staticmethod
    def display_supplier_by_id(supplier_id):
        # Static method to display supplier details by ID
        with open('data5', 'rb') as file:  # Opening the data file in binary read mode
            try:
                while True:
                    supplier = pickle.load(file)  # Deserializing and loading supplier objects one by one
                    if supplier.supplier_id == supplier_id:  # Checking if supplier ID matches
                        # Constructing message with supplier details
                        message = f"Supplier ID: {supplier.supplier_id}\nName: {supplier.name}\nAddress: {supplier.address}\nContact Details: {supplier.contact_details}\nMenu: {supplier.menu}\nMinimum Guests: {supplier.min_guests}\nMaximum Guests: {supplier.max_guests}"
                        messagebox.showinfo("Supplier Details", message)  # Displaying supplier details
                        break
            except EOFError:
                messagebox.showinfo("Supplier Details", "Supplier not found.")  # Showing message if supplier not found

    @staticmethod
    def delete_supplier_by_id(supplier_id):
        # Static method to delete supplier by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data5', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    supplier = pickle.load(file)  # Deserializing and loading supplier objects one by one
                    if supplier.supplier_id != supplier_id:  # Checking if supplier ID does not match
                        pickle.dump(supplier, temp)  # Writing supplier object to temporary file
            except EOFError:
                pass

        os.remove('data5')  # Removing original data file
        os.rename(temp_file, 'data5')  # Renaming temporary file to original name
        messagebox.showinfo("Delete Supplier", "Supplier deleted successfully.")  # Showing success message

    @staticmethod
    def edit_supplier_by_id(supplier_id, new_supplier_data):
        # Static method to edit supplier details by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data5', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    supplier = pickle.load(file)  # Deserializing and loading supplier objects one by one
                    if supplier.supplier_id == supplier_id:  # Checking if supplier ID matches
                        # Updating supplier attributes with new data
                        supplier.name = new_supplier_data['name']
                        supplier.address = new_supplier_data['address']
                        supplier.contact_details = new_supplier_data['contact_details']
                        supplier.menu = new_supplier_data['menu']
                        supplier.min_guests = new_supplier_data['min_guests']
                        supplier.max_guests = new_supplier_data['max_guests']
                    pickle.dump(supplier, temp)  # Writing supplier object to temporary file
            except EOFError:
                pass

        os.remove('data5')  # Removing original data file
        os.rename(temp_file, 'data5')  # Renaming temporary file to original name
        messagebox.showinfo("Edit Supplier", "Supplier details updated successfully.")  # Showing success message
