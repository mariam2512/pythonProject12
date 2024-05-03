import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class Event:
    def __init__(self, eventID, type, theme, date, time, duration, venueAddress, clientID, guestList, cateringCompany, cleaningCompany, decorationsCompany, entertainmentCompany, furnitureSupplyCompany, invoice):
        self.__eventID = eventID
        self.__type = type
        self.__theme = theme
        self.__date = date
        self.__time = time
        self.__duration = duration
        self.__venueAddress = venueAddress
        self.__clientID = clientID
        self.__guestList = guestList
        self.__cateringCompany = cateringCompany
        self.__cleaningCompany = cleaningCompany
        self.__decorationsCompany = decorationsCompany
        self.__entertainmentCompany = entertainmentCompany
        self.__furnitureSupplyCompany = furnitureSupplyCompany
        self.__invoice = invoice

    # Set methods
    def setEventID(self, eventID):
        self.__eventID = eventID

    def setType(self, type):
        self.__type = type

    def setTheme(self, theme):
        self.__theme = theme

    def setDate(self, date):
        self.__date = date

    def setTime(self, time):
        self.__time = time

    def setDuration(self, duration):
        self.__duration = duration

    def setVenueAddress(self, venueAddress):
        self.__venueAddress = venueAddress

    def setClientID(self, clientID):
        self.__clientID = clientID

    def setGuestList(self, guestList):
        self.__guestList = guestList

    def setCateringCompany(self, cateringCompany):
        self.__cateringCompany = cateringCompany

    def setCleaningCompany(self, cleaningCompany):
        self.__cleaningCompany = cleaningCompany

    def setDecorationsCompany(self, decorationsCompany):
        self.__decorationsCompany = decorationsCompany

    def setEntertainmentCompany(self, entertainmentCompany):
        self.__entertainmentCompany = entertainmentCompany

    def setFurnitureSupplyCompany(self, furnitureSupplyCompany):
        self.__furnitureSupplyCompany = furnitureSupplyCompany

    def setInvoice(self, invoice):
        self.__invoice = invoice

    def getEventID(self):
        return self.__eventID

    def getType(self):
        return self.__type

    def getTheme(self):
        return self.__theme

    def getDate(self):
        return self.__date

    def getTime(self):
        return self.__time

    def getDuration(self):
        return self.__duration

    def getVenueAddress(self):
        return self.__venueAddress

    def getClientID(self):
        return self.__clientID

    def getGuestList(self):
        return self.__guestList

    def getCateringCompany(self):
        return self.__cateringCompany

    def getCleaningCompany(self):
        return self.__cleaningCompany

    def getDecorationsCompany(self):
        return self.__decorationsCompany

    def getEntertainmentCompany(self):
        return self.__entertainmentCompany

    def getFurnitureSupplyCompany(self):
        return self.__furnitureSupplyCompany

    def getInvoice(self):
        return self.__invoice

    def display(self):
        event_details = (
            f"Event ID: {self.__eventID}\n"
            f"Type: {self.__type}\n"
            f"Theme: {self.__theme}\n"
            f"Date: {self.__date}\n"
            f"Time: {self.__time}\n"
            f"Duration: {self.__duration}\n"
            f"Venue Address: {self.__venueAddress}\n"
            f"Client ID: {self.__clientID}\n"
            f"Guest List: {', '.join(self.__guestList)}\n"
            f"Catering Company: {self.__cateringCompany}\n"
            f"Cleaning Company: {self.__cleaningCompany}\n"
            f"Decorations Company: {self.__decorationsCompany}\n"
            f"Entertainment Company: {self.__entertainmentCompany}\n"
            f"Furniture Supply Company: {self.__furnitureSupplyCompany}\n"
            f"Invoice: {self.__invoice}\n"
        )
        print(event_details)


class EventManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Event Management System")

        # Create buttons for various actions
        self.add_event_button = tk.Button(root, text="Add Event", command=self.add_event)
        self.add_event_button.pack()

        self.display_event_button = tk.Button(root, text="Display Event Details", command=self.display_event)
        self.display_event_button.pack()

        self.delete_event_button = tk.Button(root, text="Delete Event", command=self.delete_event)
        self.delete_event_button.pack()

        self.modify_event_button = tk.Button(root, text="Modify Event", command=self.modify_event)
        self.modify_event_button.pack()

    def add_event(self):
        event_display = Event("20247", "Graduation", "Black and White", "03-05-2024", "18:00", "3 hours",
                              "Jumeirah Str", "567", ["Mariam", "Zainab", "Shahad", "Moza", "Sara"], "Mara Company",
                              "Mitsubishi Company", "DXB celebrations Company", "Pixuol Company", "2XL Company", "$150")
        event_display.display()

    def delete_event(self):
        event_id = simpledialog.askstring("Delete Event", "Enter the Event ID to delete:")

        if event_id:
            try:
                with open("events.pkl", "rb") as file:
                    events = pickle.load(file)
            except FileNotFoundError:
                events = {}

            if event_id in events:
                del events[event_id]
                messagebox.showinfo("Event Deleted", f"Event with ID {event_id} deleted successfully.")
            else:
                messagebox.showerror("Error", f"Event with ID {event_id} not found.")

            with open("events.pkl", "wb") as file:
                pickle.dump(events, file)

    def modify_event(self):
        event_id = simpledialog.askstring("Modify Event", "Enter the Event ID to modify:")

        if event_id:
            try:
                with open("events.pkl", "rb") as file:
                    events = pickle.load(file)
            except FileNotFoundError:
                events = {}

            if event_id in events:
                messagebox.showinfo("Event Modified", f"Event with ID {event_id} modified successfully.")
            else:
                messagebox.showerror("Error", f"Event with ID {event_id} not found.")

            # Save events back to file
            with open("events.pkl", "wb") as file:
                pickle.dump(events, file)

    def display_event(self):
        event_id = simpledialog.askstring("Display Event", "Enter the Event ID to display:")
        if event_id:
            try:
                with open("events.pkl", "rb") as file:
                    events = pickle.load(file)
            except FileNotFoundError:
                events = {}

            if event_id in events:
                event = events[event_id]
                event_details = (
                    f"Event ID: {event.getEventID()}\n"
                    f"Type: {event.getType()}\n"
                    f"Theme: {event.getTheme()}\n"
                    f"Date: {event.getDate()}\n"
                    f"Time: {event.getTime()}\n"
                    f"Duration: {event.getDuration()}\n"
                    f"Venue Address: {event.getVenueAddress()}\n"
                    f"Client ID: {event.getClientID()}\n"
                    f"Guest List: {', '.join(event.getGuestList())}\n"
                    f"Catering Company: {event.getCateringCompany()}\n"
                    f"Cleaning Company: {event.getCleaningCompany()}\n"
                    f"Decorations Company: {event.getDecorationsCompany()}\n"
                    f"Entertainment Company: {event.getEntertainmentCompany()}\n"
                    f"Furniture Supply Company: {event.getFurnitureSupplyCompany()}\n"
                    f"Invoice: {event.getInvoice()}\n"
                )

                display_window = tk.Toplevel(self.root)
                display_window.title("Event Details")

                event_text = tk.Text(display_window, height=20, width=60)
                event_text.insert(tk.END, event_details)
                event_text.pack(padx=10, pady=10)

                display_window.mainloop()
            else:
                messagebox.showerror("Error", f"Event with ID {event_id} not found.")

def main():
    root = tk.Tk()
    app = EventManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

