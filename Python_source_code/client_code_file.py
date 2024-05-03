import pickle  # Importing pickle module to work with binary files
from tkinter import messagebox  # Importing the messagebox class from tkinter for displaying messages
import os  # Importing os module for file operations

class Client:
    def __init__(self, client_id, name, address, contact_details, budget):
        # Constructor method to initialize Client object with provided attributes
        self.client_id = client_id  # client ID
        self.name = name  # client name
        self.address = address  # client address
        self.contact_details = contact_details  # client contact details
        self.budget = budget  # client budget

    @staticmethod
    def add_client(client_id, name, address, contact_details, budget):
        # Static method to add a new client to the data file
        new_client = Client(client_id, name, address, contact_details, budget)  # Creating a new Client object
        with open('data2', 'ab') as file:  # Opening the data file in binary append mode
            pickle.dump(new_client, file)  # Serializing and writing the new client object to the file
        messagebox.showinfo("Add Client", "Client added successfully.")  # Showing success message

    @staticmethod
    def display_client_by_id(client_id):
        # Static method to display client details by ID
        with open('data2', 'rb') as file:  # Opening the data file in binary read mode
            try:
                while True:
                    client = pickle.load(file)  # Deserializing and loading client objects one by one
                    if client.client_id == client_id:  # Checking if client ID matches
                        message = f"Client ID: {client.client_id}\nName: {client.name}\nAddress: {client.address}\nContact Details: {client.contact_details}\nBudget: {client.budget}"
                        messagebox.showinfo("Client Details", message)  # Displaying client details
                        break
            except EOFError:
                messagebox.showinfo("Client Details", "Client not found.")  # Showing message if client not found

    @staticmethod
    def delete_client_by_id(client_id):
        # Static method to delete client by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data2', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    client = pickle.load(file)  # Deserializing and loading client objects one by one
                    if client.client_id != client_id:  # Checking if client ID does not match
                        pickle.dump(client, temp)  # Writing client object to temporary file
            except EOFError:
                pass

        os.remove('data2')  # Removing original data file
        os.rename(temp_file, 'data2')  # Renaming temporary file to original name
        messagebox.showinfo("Delete Client", "Client deleted successfully.")  # Showing success message

    @staticmethod
    def edit_client_by_id(client_id, new_client_data):
        # Static method to edit client details by ID
        temp_file = 'temp.pkl'  # Temporary file name
        with open('data2', 'rb') as file, open(temp_file, 'wb') as temp:  # Opening both original and temporary files
            try:
                while True:
                    client = pickle.load(file)  # Deserializing and loading client objects one by one
                    if client.client_id == client_id:  # Checking if client ID matches
                        # Updating client attributes with new data
                        client.name = new_client_data['name']
                        client.address = new_client_data['address']
                        client.contact_details = new_client_data['contact_details']
                        client.budget = new_client_data['budget']
                    pickle.dump(client, temp)  # Writing client object to temporary file
            except EOFError:
                pass

        os.remove('data2')  # Removing original data file
        os.rename(temp_file, 'data2')  # Renaming temporary file to original name
        messagebox.showinfo("Edit Client", "Client details updated successfully.")  # Showing success message
