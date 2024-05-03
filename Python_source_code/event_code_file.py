import pickle  # Importing the pickle module for serializing and deserializing objects
from tkinter import messagebox  # Importing the messagebox class from tkinter for displaying messages
import os  # Importing the os module for file operations

class Event:
    def __init__(self, event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers):
        # Constructor method to initialize Event object with provided attributes
        self.event_id = event_id  # give event ID
        self.event_type = event_type  # give event type
        self.theme = theme  # give event theme
        self.date = date  # give event date
        self.time = time  # give event time
        self.duration = duration  # give event duration
        self.venue_address = venue_address  # give event venue address
        self.client_id = client_id  # give client ID associated with the event
        self.guest_list = guest_list  # give list of guests for the event
        self.suppliers = suppliers  # give list of suppliers for the event

    @staticmethod
    def add_event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers):
        # Static method to add a new event to the data file
        new_event = Event(event_id, event_type, theme, date, time, duration, venue_address, client_id, guest_list, suppliers)  # Creating a new Event object
        with open('data6', 'ab') as file:  # Opening the data file in binary append mode
            pickle.dump(new_event, file)  # Serializing and writing the new event object to the file
        messagebox.showinfo("Add Event", "Event added successfully.")  # Showing success message

    @staticmethod
    def display_event_by_id(event_id):
        # Static method to display event details by ID
        with open('data6', 'rb') as file:  # Opening the data file in binary read mode
            try:
                while True:
                    event = pickle.load(file)  # Deserializing and loading event objects one by one
                    if event.event_id == event_id:  # Checking if event ID matches
                        # Constructing message with event details
                        message = f"Event ID: {event.event_id}\nType: {event.event_type}\nTheme: {event.theme}\nDate: {event.date}\nTime: {event.time}\nDuration: {event.duration}\nVenue Address: {event.venue_address}\nClient ID: {event.client_id}\nGuest List: {event.guest_list}\nSuppliers: {event.suppliers}"
                        messagebox.showinfo("Event Details", message)  # Displaying event details
                        break
            except EOFError:
                messagebox.showinfo("Event Details", "Event not found.")  # Showing message if event not found

    @staticmethod
    def delete_event_by_id(event_id):
        # Static method to delete event by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data6', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    event = pickle.load(file)  # Deserializing and loading event objects one by one
                    if event.event_id != event_id:  # Checking if event ID does not match
                        pickle.dump(event, temp)  # Writing event object to temporary file
            except EOFError:
                pass

        os.remove('data6')  # Removing original data file
        os.rename(temp_file, 'data6')  # Renaming temporary file to original name
        messagebox.showinfo("Delete Event", "Event deleted successfully.")  # Showing success message

    @staticmethod
    def edit_event_by_id(event_id, new_event_data):
        # Static method to edit event details by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data6', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    event = pickle.load(file)  # Deserializing and loading event objects one by one
                    if event.event_id == event_id:  # Checking if event ID matches
                        # Updating event attributes with new data
                        event.event_type = new_event_data['event_type']
                        event.theme = new_event_data['theme']
                        event.date = new_event_data['date']
                        event.time = new_event_data['time']
                        event.duration = new_event_data['duration']
                        event.venue_address = new_event_data['venue_address']
                        event.client_id = new_event_data['client_id']
                        event.guest_list = new_event_data['guest_list']
                        event.suppliers = new_event_data['suppliers']
                    pickle.dump(event, temp)  # Writing event object to temporary file
            except EOFError:
                pass

        os.remove('data6')  # Removing original data file
        os.rename(temp_file, 'data6')  # Renaming temporary file to original name
        messagebox.showinfo("Edit Event", "Event details updated successfully.")  # Showing success message
