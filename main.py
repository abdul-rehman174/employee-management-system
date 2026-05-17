from csv_importer import CSVImporter
from company import Company
from roles import Ceo, SalesExecutive, DevOpsEngineer, Accountant, HRManager


class MenuPrinter:
    def show_menu(self):
        user = app.current_user

        print(f"\nWelcome to {app.company.name}, {user.name} ({user.__class__.__name__})")
        print("Menu Options:")
        print("1. View employees by departments")

        print("2. View salary ledger")
        print("3. Search salary by ID")

        print("4. Fire an employee")
        print("5. Perform role action")

        print("0. Exit")


class Main:
    def __init__(self, company_name, filename):
        self.company = Company(company_name)
        self.importer = CSVImporter()
        self.menu = MenuPrinter()
        self.salary_manager = None
        self.filename = filename
        self.current_user = None
        self.permissions = {
            Ceo: {"all"},
            Accountant: {1, 5},
            HRManager: {1, 3, 5},
            SalesExecutive: {1, 5},
            DevOpsEngineer: {5}
        }

    def setup(self):
        employees = self.importer.import_employees(self.filename)
        self.company.assign_employees_to_departments(employees)
        self.salary_manager = self.company.get_departments()["Accounts"].salary_manager

    def login(self):
        print(f"Welcome to '{app.company.name}'\n\nplease login with your id")
        employ_id = input("Enter  ID: ")
        emp = self.company.get_employee_by_id(employ_id)
        if emp:
            self.current_user = emp
            print(f"\n Welcome, {emp.name} ({emp.__class__.__name__})")
        else:
            print("no person with that id exist")
            exit()

    def view_departments(self):
        print("\nSalary Slips by Department:")
        for dept_name, dept in self.company.get_departments().items():
            print(f"\nDepartment: {dept_name}")
            for emp in dept.employees:
                slip = self.salary_manager.generate_salary_slip(emp)
                print(slip)

    def view_ledger(self):
        ledger = self.salary_manager.get_ledger()
        if ledger:
            print("\nSalary Ledger:")
            for slip in ledger:
                print(slip)
        else:
            print("Ledger is empty. Generate salary slips first.")

    def search_by_id(self):
        emp_id = input("\nEnter Employee ID to get specific slip: ")
        emp = self.company.get_employee_by_id(emp_id)
        if emp:
            print("\nSpecific Salary Slip:")
            print(self.salary_manager.generate_salary_slip(emp))
        else:
            print("Employee not found.")

    def exit_program(self):
        print("\nExiting program.")
        exit()

    def handle_choice(self, choice):
        user = self.current_user

        if choice == 0:
            self.exit_program()

        elif choice == 1:
            if self.is_allowed(1):
                self.view_departments()
            else:
                print("u dont have access")
        elif choice == 2:
            if self.is_allowed(2):
                self.view_ledger()
            else:
                print("u dont have access")

        elif choice == 3:
            if self.is_allowed(3):
                self.search_by_id()
            else:
                print("u dont have access")

        elif choice == 4:
            if self.is_allowed(4):
                user.fire_employee(self.company)
            else:
                print("u dont have access")
        elif choice == 5:
            if self.is_allowed(5):
                self.perform_role_action()
            else:
                print("u dont have access")
        else:
            print("❌ You are not allowed to perform this action.")

    def is_allowed(self, choice):
        user = self.current_user
        user_role = type(user)
        allowed_choices = self.permissions.get(user_role, set())

        if "all" in allowed_choices:
            return True
        elif choice in allowed_choices:
            return True
        else:
            return None

    def perform_role_action(self):
        user = self.current_user
        user.role_action()

    def run(self):
        self.setup()
        self.login()
        while True:
            try:
                self.menu.show_menu()
                choice = int(input("\nEnter your choice: "))
                self.handle_choice(choice)
            except ValueError:
                print("Please enter a valid number.")


if __name__ == "__main__":
    app = Main("Guru Petroleum", "employees.csv")
    app.run()
