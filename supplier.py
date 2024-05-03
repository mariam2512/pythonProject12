import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class Supplier:
    def __init__(self, supplierID, nameSupplier, addressSupplier, contactSupplier, productsSupplier):
        self.__supplierID = supplierID
        self.__nameSupplier = nameSupplier
        self.__addressSupplier = addressSupplier
        self.__contactSupplier = contactSupplier
        self.__productsSupplier = productsSupplier

    # Setter methods
    def setSupplierID(self, supplierID):
        self.__supplierID = supplierID

    def setNameSupplier(self, nameSupplier):
        self.__nameSupplier = nameSupplier

    def setAddressSupplier(self, addressSupplier):
        self.__addressSupplier = addressSupplier

    def setContactSupplier(self, contactSupplier):
        self.__contactSupplier = contactSupplier

    def setProductsSupplier(self, productsSupplier):
        self.__productsSupplier = productsSupplier

    # Getter methods
    def getSupplierID(self):
        return self.__supplierID

    def getNameSupplier(self):
        return self.__nameSupplier

    def getAddressSupplier(self):
        return self.__addressSupplier

    def getContactSupplier(self):
        return self.__contactSupplier

    def getProductsSupplier(self):
        return self.__productsSupplier

class SuppliertManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Supplier Management System")

        self.add_supplier_button = tk.Button(root, text="Add Supplier", command=self.add_supplier)
        self.add_supplier_button.pack()

        self.display_supplier_button = tk.Button(root, text="Display Supplier Details", command=self.display_supplier)
        self.display_supplier_button.pack()

        self.delete_supplier_button = tk.Button(root, text="Delete Supplier", command=self.delete_supplier)
        self.delete_supplier_button.pack()

        self.modify_supplier_button = tk.Button(root, text="Modify Supplier", command=self.modify_supplier)
        self.modify_supplier_button.pack()

    def add_supplier(self):
        supplier = Supplier("SUP123", "ABC Supplier", "123 Main Street", "123-456-7890", ["Product1", "Product2"])
        supplier_details = (
            f"Supplier ID: {supplier.get_supplierID()}\n"
            f"Name: {supplier.get_nameSupplier()}\n"
            f"Address: {supplier.get_addressSupplier()}\n"
            f"Contact: {supplier.get_contactSupplier()}\n"
            f"Products: {', '.join(supplier.get_productsSupplier())}\n"
        )
        print(supplier_details)

    def delete_supplier(self):
        supplier_id = simpledialog.askstring("Delete Supplier", "Enter the Supplier ID to delete:")
        if supplier_id:
            print(f"Supplier with ID {supplier_id} deleted successfully.")

    def modify_supplier(self):
        supplier_id = simpledialog.askstring("Modify Supplier", "Enter the Supplier ID to modify:")
        if supplier_id:
            print(f"Supplier with ID {supplier_id} modified successfully.")

    def display_supplier(self):
        supplier_id = simpledialog.askstring("Display Supplier", "Enter the Supplier ID to display:")
        if supplier_id:
            print(f"Displaying details for Supplier with ID {supplier_id}")

def main():
    root = tk.Tk()
    app = SuppliertManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()