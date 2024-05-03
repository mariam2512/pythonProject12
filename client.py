import tkinter as tk
from tkinter import simpledialog

class Client:
    def __init__(self, clientID, nameClient, addressClient, contactDetailsClient, budget):
        self.__clientID = clientID
        self.__nameClient = nameClient
        self.__addressClient = addressClient
        self.__contactDetailsClient = contactDetailsClient
        self.__budget = budget

    # Setter methods
    def set_clientID(self, clientID):
        self.__clientID = clientID

    def set_nameClient(self, nameClient):
        self.__nameClient = nameClient

    def set_addressClient(self, addressClient):
        self.__addressClient = addressClient

    def set_contactDetailsClient(self, contactDetailsClient):
        self.__contactDetailsClient = contactDetailsClient

    def set_budget(self, budget):
        self.__budget = budget

    # Getter methods
    def get_clientID(self):
        return self.__clientID

    def get_nameClient(self):
        return self.__nameClient

    def get_addressClient(self):
        return self.__addressClient

    def get_contactDetailsClient(self):
        return self.__contactDetailsClient

    def get_budget(self):
        return self.__budget

class ClientManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Client Management System")

        # Create buttons for various actions
        self.add_client_button = tk.Button(root, text="Add Client", command=self.add_client)
        self.add_client_button.pack()

        self.display_client_button = tk.Button(root, text="Display Client Details", command=self.display_client)
        self.display_client_button.pack()

        self.delete_client_button = tk.Button(root, text="Delete Client", command=self.delete_client)
        self.delete_client_button.pack()

        self.modify_client_button = tk.Button(root, text="Modify Client", command=self.modify_client)
        self.modify_client_button.pack()

    def add_client(self):
        # Example of adding a client
        client = Client("20247", "Mariam", "Al Butterfly", "123456789", "$100000")
        client_details = (
            f"Client ID: {client.get_clientID()}\n"
            f"Name: {client.get_nameClient()}\n"
            f"Address: {client.get_addressClient()}\n"
            f"Contact Details: {client.get_contactDetailsClient()}\n"
            f"Budget: {client.get_budget()}\n"
        )
        print(client_details)

    def delete_client(self):
        client_id = simpledialog.askstring("Delete Client", "Enter the Client ID to delete:")
        if client_id:
            print(f"Client with ID {client_id} deleted successfully.")

    def modify_client(self):
        client_id = simpledialog.askstring("Modify Client", "Enter the Client ID to modify:")
        if client_id:
            print(f"Client with ID {client_id} modified successfully.")

    def display_client(self):
        client_id = simpledialog.askstring("Display Client", "Enter the Client ID to display:")
        if client_id:
            print(f"Displaying details for Client with ID {client_id}")

def main():
    root = tk.Tk()
    app = ClientManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
