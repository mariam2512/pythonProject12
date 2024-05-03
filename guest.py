import tkinter as tk
from tkinter import simpledialog

class Guest:
    def __init__(self, clientIDGuest, nameGuest, addressGuest, contactDetailsGuest):
        self.__clientIDGuest = clientIDGuest
        self.__nameGuest = nameGuest
        self.__addressGuest = addressGuest
        self.__contactDetailsGuest = contactDetailsGuest

    # Setter methods
    def setClientIDGuest(self, clientIDGuest):
        self.__clientIDGuest = clientIDGuest

    def setNameGuest(self, nameGuest):
        self.__nameGuest = nameGuest

    def setAddressGuest(self, addressGuest):
        self.__addressGuest = addressGuest

    def setContactDetailsGuest(self, contactDetailsGuest):
        self.__contactDetailsGuest = contactDetailsGuest

    # Getter methods
    def getClientIDGuest(self):
        return self.__clientIDGuest

    def getNameGuest(self):
        return self.__nameGuest

    def getAddressGuest(self):
        return self.__addressGuest

    def getContactDetailsGuest(self):
        return self.__contactDetailsGuest

class GuestManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Guest Management System")

        # Create buttons for various actions
        self.add_guest_button = tk.Button(root, text="Add Guest", command=self.add_guest)
        self.add_guest_button.pack()

        self.display_guest_button = tk.Button(root, text="Display Guest Details", command=self.display_guest)
        self.display_guest_button.pack()

        self.delete_guest_button = tk.Button(root, text="Delete Guest", command=self.delete_guest)
        self.delete_guest_button.pack()

        self.modify_guest_button = tk.Button(root, text="Modify Guest", command=self.modify_guest)
        self.modify_guest_button.pack()

    def add_guest(self):
        guest = Guest("20247", "Zainab", "Al Zahia Street", "123456789")
        guest_details = (
            f"Guest ID: {guest.getClientIDGuest()}\n"
            f"Name: {guest.getNameGuest()}\n"
            f"Address: {guest.getAddressGuest()}\n"
            f"Contact Details: {guest.getContactDetailsGuest()}\n"
        )
        print(guest_details)

    def delete_guest(self):
        guest_id = simpledialog.askstring("Delete Guest", "Enter the Guest ID to delete:")
        if guest_id:
            print(f"Guest with ID {guest_id} deleted successfully.")

    def modify_guest(self):
        guest_id = simpledialog.askstring("Modify Guest", "Enter the Guest ID to modify:")
        if guest_id:
            print(f"Guest with ID {guest_id} modified successfully.")

    def display_guest(self):
        guest_id = simpledialog.askstring("Display Guest", "Enter the Guest ID to display:")
        if guest_id:
            print(f"Displaying details for Guest with ID {guest_id}")

def main():
    root = tk.Tk()
    app = GuestManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
