import tkinter as tk
from tkinter import simpledialog, messagebox
import pickle

class Employee:
    def __init__(self, nameEmployee, employeeID, department, jobTitle, basicSalary, age, dateOfBirth, passportDetails):
        self.__nameEmployee = nameEmployee
        self.__employeeID = employeeID
        self.__department = department
        self.__jobTitle = jobTitle
        self.__basicSalary = basicSalary
        self.__age = age
        self.__dateOfBirth = dateOfBirth
        self.__passportDetails = passportDetails

    # Setter methods
    def set_nameEmployee(self, nameEmployee):
        self.__nameEmployee = nameEmployee

    def set_employeeID(self, employeeID):
        self.__employeeID = employeeID

    def set_department(self, department):
        self.__department = department

    def set_jobTitle(self, jobTitle):
        self.__jobTitle = jobTitle

    def set_basicSalary(self, basicSalary):
        self.__basicSalary = basicSalary

    def set_age(self, age):
        self.__age = age

    def set_dateOfBirth(self, dateOfBirth):
        self.__dateOfBirth = dateOfBirth

    def set_passportDetails(self, passportDetails):
        self.__passportDetails = passportDetails

    # Getter methods
    def get_nameEmployee(self):
        return self.__nameEmployee

    def get_employeeID(self):
        return self.__employeeID

    def get_department(self):
        return self.__department

    def get_jobTitle(self):
        return self.__jobTitle

    def get_basicSalary(self):
        return self.__basicSalary

    def get_age(self):
        return self.__age

    def get_dateOfBirth(self):
        return self.__dateOfBirth

    def get_passportDetails(self):
        return self.__passportDetails


class EmployeeManagementGUI:
    def __init__(self, root):
        self.root = root
        root.title("Employee Management System")

        # Create buttons for various actions
        self.add_employee_button = tk.Button(root, text="Add Employee", command=self.add_employee)
        self.add_employee_button.pack()

        self.display_employee_button = tk.Button(root, text="Display Employee Details", command=self.display_employee)
        self.display_employee_button.pack()

        self.delete_employee_button = tk.Button(root, text="Delete Employee", command=self.delete_employee)
        self.delete_employee_button.pack()

        self.modify_employee_button = tk.Button(root, text="Modify Employee", command=self.modify_employee)
        self.modify_employee_button.pack()

    def add_employee(self):
        # Example of adding an employee
        employee = Employee("John Doe", "EMP123", "HR", "Manager", 5000, 35, "1989-05-25", "AB123456")
        employee_details = (
            f"Name: {employee.get_nameEmployee()}\n"
            f"Employee ID: {employee.get_employeeID()}\n"
            f"Department: {employee.get_department()}\n"
            f"Job Title: {employee.get_jobTitle()}\n"
            f"Basic Salary: {employee.get_basicSalary()}\n"
            f"Age: {employee.get_age()}\n"
            f"Date of Birth: {employee.get_dateOfBirth()}\n"
            f"Passport Details: {employee.get_passportDetails()}\n"
        )
        print(employee_details)

    def delete_employee(self):
        employee_id = simpledialog.askstring("Delete Employee", "Enter the Employee ID to delete:")

        if employee_id:
            print(f"Employee with ID {employee_id} deleted successfully.")

    def modify_employee(self):
        employee_id = simpledialog.askstring("Modify Employee", "Enter the Employee ID to modify:")

        if employee_id:
            print(f"Employee with ID {employee_id} modified successfully.")

    def display_employee(self):
        employee_id = simpledialog.askstring("Display Employee", "Enter the Employee ID to display:")
        if employee_id:
            print(f"Displaying details for Employee with ID {employee_id}")

def main():
    root = tk.Tk()
    app = EmployeeManagementGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()