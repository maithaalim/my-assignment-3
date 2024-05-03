import pickle  # Importing the pickle module for object serialization
from tkinter import messagebox  # Importing the messagebox class from tkinter for displaying messages
import os  # Importing the os module for file operations

class Guest:
    def __init__(self, guest_id, name, address, contact_details):
        # Constructor method to initialize Guest object with provided attributes
        self.guest_id = guest_id  # give guest ID
        self.name = name  # give guest name
        self.address = address  # give guest address
        self.contact_details = contact_details  # give guest contact details

    @staticmethod
    def add_guest(guest_id, name, address, contact_details):
        # Static method to add a new guest to the data file
        new_guest = Guest(guest_id, name, address, contact_details)  # Creating a new Guest object
        with open('data3', 'ab') as file:  # Opening the data file in binary append mode
            pickle.dump(new_guest, file)  # Serializing and writing the new guest object to the file
        messagebox.showinfo("Add Guest", "Guest added successfully.")  # Showing success message

    @staticmethod
    def display_guest_by_id(guest_id):
        # Static method to display guest details by ID
        with open('data3', 'rb') as file:  # Opening the data file in binary read mode
            try:
                while True:
                    guest = pickle.load(file)  # Deserializing and loading guest objects one by one
                    if guest.guest_id == guest_id:  # Checking if guest ID matches
                        # Constructing message with guest details
                        message = f"Guest ID: {guest.guest_id}\nName: {guest.name}\nAddress: {guest.address}\nContact Details: {guest.contact_details}"
                        messagebox.showinfo("Guest Details", message)  # Displaying guest details
                        break
            except EOFError:
                messagebox.showinfo("Guest Details", "Guest not found.")  # Showing message if guest not found

    @staticmethod
    def delete_guest_by_id(guest_id):
        # Static method to delete guest by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data3', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    guest = pickle.load(file)  # Deserializing and loading guest objects one by one
                    if guest.guest_id != guest_id:  # Checking if guest ID does not match
                        pickle.dump(guest, temp)  # Writing guest object to temporary file
            except EOFError:
                pass

        os.remove('data3')  # Removing original data file
        os.rename(temp_file, 'data3')  # Renaming temporary file to original name
        messagebox.showinfo("Delete Guest", "Guest deleted successfully.")  # Showing success message

    @staticmethod
    def edit_guest_by_id(guest_id, new_guest_data):
        # Static method to edit guest details by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data3', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    guest = pickle.load(file)  # Deserializing and loading guest objects one by one
                    if guest.guest_id == guest_id:  # Checking if guest ID matches
                        # Updating guest attributes with new data
                        guest.name = new_guest_data['name']
                        guest.address = new_guest_data['address']
                        guest.contact_details = new_guest_data['contact_details']
                    pickle.dump(guest, temp)  # Writing guest object to temporary file
            except EOFError:
                pass

        os.remove('data3')  # Removing original data file
        os.rename(temp_file, 'data3')  # Renaming temporary file to original name
        messagebox.showinfo("Edit Guest", "Guest details updated successfully.")  # Showing success message
