import pickle  # Importing pickle for object serialization
from tkinter import messagebox  # Importing messagebox from tkinter for displaying messages
import os  # Importing os for file operations

class Venue:
    def __init__(self, venue_id, name, address, contact, min_guests, max_guests):
        # Initializing Venue object with provided attributes
        self.venue_id = venue_id  # Venue ID
        self.name = name  # Venue name
        self.address = address  # Venue address
        self.contact = contact  # Venue contact details
        self.min_guests = min_guests  # Minimum number of guests allowed
        self.max_guests = max_guests  # Maximum number of guests allowed

    @staticmethod
    def add_venue(venue_id, name, address, contact, min_guests, max_guests):
        # Static method to add a new venue to the data file
        new_venue = Venue(venue_id, name, address, contact, min_guests, max_guests)  # Creating a new Venue object
        with open('data4', 'ab') as file:  # Opening the data file in binary append mode
            pickle.dump(new_venue, file)  # Serializing and writing the new venue object to the file
        messagebox.showinfo("Add Venue", "Venue added successfully.")  # Showing success message

    @staticmethod
    def display_venue_by_id(venue_id):
        # Static method to display venue details by ID
        with open('data4', 'rb') as file:  # Opening the data file in binary read mode
            try:
                while True:
                    venue = pickle.load(file)  # Deserializing and loading venue objects one by one
                    if venue.venue_id == venue_id:  # Checking if venue ID matches
                        # Constructing message with venue details
                        message = f"Venue ID: {venue.venue_id}\nName: {venue.name}\nAddress: {venue.address}\nContact: {venue.contact}\nMinimum Guests: {venue.min_guests}\nMaximum Guests: {venue.max_guests}"
                        messagebox.showinfo("Venue Details", message)  # Displaying venue details
                        break
            except EOFError:
                messagebox.showinfo("Venue Details", "Venue not found.")  # Showing message if venue not found

    @staticmethod
    def delete_venue_by_id(venue_id):
        # Static method to delete venue by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data4', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    venue = pickle.load(file)  # Deserializing and loading venue objects one by one
                    if venue.venue_id != venue_id:  # Checking if venue ID does not match
                        pickle.dump(venue, temp)  # Writing venue object to temporary file
            except EOFError:
                pass

        os.remove('data4')  # Removing original data file
        os.rename(temp_file, 'data4')  # Renaming temporary file to original name
        messagebox.showinfo("Delete Venue", "Venue deleted successfully.")  # Showing success message

    @staticmethod
    def edit_venue_by_id(venue_id, new_venue_data):
        # Static method to edit venue details by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data4', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    venue = pickle.load(file)  # Deserializing and loading venue objects one by one
                    if venue.venue_id == venue_id:  # Checking if venue ID matches
                        # Updating venue attributes with new data
                        venue.name = new_venue_data['name']
                        venue.address = new_venue_data['address']
                        venue.contact = new_venue_data['contact']
                        venue.min_guests = new_venue_data['min_guests']
                        venue.max_guests = new_venue_data['max_guests']
                    pickle.dump(venue, temp)  # Writing venue object to temporary file
            except EOFError:
                pass

        os.remove('data4')  # Removing original data file
        os.rename(temp_file, 'data4')  # Renaming temporary file to original name
        messagebox.showinfo("Edit Venue", "Venue details updated successfully.")  # Showing success message
