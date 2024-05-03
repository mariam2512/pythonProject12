import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class Venue:
    def __init__(self, venueID, nameVenue, addressVenue, contactVenue, minGuestsVenue, maxGuestsVenue):
        self.__venueID = venueID
        self.__nameVenue = nameVenue
        self.__addressVenue = addressVenue
        self.__contactVenue = contactVenue
        self.__minGuestsVenue = minGuestsVenue
        self.__maxGuestsVenue = maxGuestsVenue

    # Setter methods
    def setVenueID(self, venueID):
        self.__venueID = venueID

    def setNameVenue(self, nameVenue):
        self.__nameVenue = nameVenue

    def setAddressVenue(self, addressVenue):
        self.__addressVenue = addressVenue

    def setContactVenue(self, contactVenue):
        self.__contactVenue = contactVenue

    def setMinGuestsVenue(self, minGuestsVenue):
        self.__minGuestsVenue = minGuestsVenue

    def setMaxGuestsVenue(self, maxGuestsVenue):
        self.__maxGuestsVenue = maxGuestsVenue

    # Getter methods
    def getVenueID(self):
        return self.__venueID

    def getNameVenue(self):
        return self.__nameVenue

    def getAddressVenue(self):
        return self.__addressVenue

    def getContactVenue(self):
        return self.__contactVenue

    def getMinGuestsVenue(self):
        return self.__minGuestsVenue

    def getMaxGuestsVenue(self):
        return self.__maxGuestsVenue


class VenueManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Venue Management System")

        # Create buttons for various actions
        self.add_venue_button = tk.Button(root, text="Add Venue", command=self.add_venue)
        self.add_venue_button.pack()

        self.display_venue_button = tk.Button(root, text="Display Venue Details", command=self.display_venue)
        self.display_venue_button.pack()

        self.delete_venue_button = tk.Button(root, text="Delete Venue", command=self.delete_venue)
        self.delete_venue_button.pack()

        self.modify_venue_button = tk.Button(root, text="Modify Venue", command=self.modify_venue)
        self.modify_venue_button.pack()

    def add_venue(self):
        # Example of adding a venue
        venue = Venue("2001", "Grand Hall", "456 Oak St", "987-654-3210", 50, 500)
        venue_details = (
            f"Venue ID: {venue.get_venueID()}\n"
            f"Name: {venue.get_nameVenue()}\n"
            f"Address: {venue.get_addressVenue()}\n"
            f"Contact Details: {venue.get_contactVenue()}\n"
            f"Minimum Guests: {venue.get_minGuestsVenue()}\n"
            f"Maximum Guests: {venue.get_maxGuestsVenue()}\n"
        )
        print(venue_details)

    def delete_venue(self):
        venue_id = simpledialog.askstring("Delete Venue", "Enter the Venue ID to delete:")

        if venue_id:
            print(f"Venue with ID {venue_id} deleted successfully.")

    def modify_venue(self):
        venue_id = simpledialog.askstring("Modify Venue", "Enter the Venue ID to modify:")

        if venue_id:
            print(f"Venue with ID {venue_id} modified successfully.")

    def display_venue(self):
        venue_id = simpledialog.askstring("Display Venue", "Enter the Venue ID to display:")
        if venue_id:
            print(f"Displaying details for Venue with ID {venue_id}")

def main():
    root = tk.Tk()
    app = VenueManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
