import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class Caterer:
    def __init__(self, catererID, nameCaterer, addressCaterer, contactDetailsCaterer, menu, minGuestsCaterer, maxiGuestsCaterer):
        self.__catererID = catererID
        self.__nameCaterer = nameCaterer
        self.__addressCaterer = addressCaterer
        self.__contactDetailsCaterer = contactDetailsCaterer
        self.__menu = menu
        self.__minGuestsCaterer = minGuestsCaterer
        self.__maxiGuestsCaterer = maxiGuestsCaterer

    # Setter methods
    def setCatererID(self, catererID):
        self.__catererID = catererID

    def setNameCaterer(self, nameCaterer):
        self.__nameCaterer = nameCaterer

    def setAddressCaterer(self, addressCaterer):
        self.__addressCaterer = addressCaterer

    def setContactDetailsCaterer(self, contactDetailsCaterer):
        self.__contactDetailsCaterer = contactDetailsCaterer

    def setMenu(self, menu):
        self.__menu = menu

    def setMinGuestsCaterer(self, minGuestsCaterer):
        self.__minGuestsCaterer = minGuestsCaterer

    def setMaxiGuestsCaterer(self, maxiGuestsCaterer):
        self.__maxiGuestsCaterer = maxiGuestsCaterer

    # Getter methods
    def getCatererID(self):
        return self.__catererID

    def getNameCaterer(self):
        return self.__nameCaterer

    def getAddressCaterer(self):
        return self.__addressCaterer

    def getContactDetailsCaterer(self):
        return self.__contactDetailsCaterer

    def getMenu(self):
        return self.__menu

    def getMinGuestsCaterer(self):
        return self.__minGuestsCaterer

    def getMaxiGuestsCaterer(self):
        return self.__maxiGuestsCaterer


class CatererManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Caterer Management System")

        # Create buttons for various actions
        self.add_caterer_button = tk.Button(root, text="Add Caterer", command=self.add_caterer)
        self.add_caterer_button.pack()

        self.display_caterer_button = tk.Button(root, text="Display Caterer Details", command=self.display_caterer)
        self.display_caterer_button.pack()

        self.delete_caterer_button = tk.Button(root, text="Delete Caterer", command=self.delete_caterer)
        self.delete_caterer_button.pack()

        self.modify_caterer_button = tk.Button(root, text="Modify Caterer", command=self.modify_caterer)
        self.modify_caterer_button.pack()

    def add_caterer(self):
        caterer = Caterer("20247", "Mara Catering", "Truck", "1234567890", "International", 50, 100)
        caterer_details = (
            f"Caterer ID: {caterer.get_catererID()}\n"
            f"Name: {caterer.get_nameCaterer()}\n"
            f"Address: {caterer.get_addressCaterer()}\n"
            f"Contact Details: {caterer.get_contactDetailsCaterer()}\n"
            f"Menu: {caterer.get_menu()}\n"
            f"Minimum Guests: {caterer.get_minGuestsCaterer()}\n"
            f"Maximum Guests: {caterer.get_maxiGuestsCaterer()}\n"
        )
        print(caterer_details)

    def delete_caterer(self):
        caterer_id = simpledialog.askstring("Delete Caterer", "Enter the Caterer ID to delete:")

        if caterer_id:
            print(f"Caterer with ID {caterer_id} deleted successfully.")

    def modify_caterer(self):
        caterer_id = simpledialog.askstring("Modify Caterer", "Enter the Caterer ID to modify:")

        if caterer_id:
            print(f"Caterer with ID {caterer_id} modified successfully.")

    def display_caterer(self):
        caterer_id = simpledialog.askstring("Display Caterer", "Enter the Caterer ID to display:")
        if caterer_id:
            print(f"Displaying details for Caterer with ID {caterer_id}")

def main():
    root = tk.Tk()
    app = CatererManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()