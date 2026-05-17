from employee import Employee


class Ceo(Employee):
    role = "ceo"

    def fire_employee(self, company):
        emp_id = input("Enter Employee ID to fire: ")
        emp = company.get_employee_by_id(emp_id)
        if not emp:
            print(" Employee not found.")
            return
        for dept in company.get_departments().values():
            if emp in dept.employees:
                dept.employees.remove(emp)
                print(f" {emp.name} has been fired.")
                return
        print(" Employee not in any department.")

    def call_board_meeting(self):
        print(f"{self.name} (CEO) is calling a board meeting.")

    def role_action(self):
        self.call_board_meeting()


class Accountant(Employee):
    role = "accountant"

    def generate_financial_report(self):
        print(f"{self.name} is generating the financial report.")

    def role_action(self):
        return self.generate_financial_report()


class HRManager(Employee):
    role = "hr_manager"

    def organize_training(self):
        print(f"{self.name} is organizing a training session for employees.")

    def conduct_interview(self):
        print(f"{self.name} is conducting an interview.")

    def role_action(self):
        self.organize_training()


class SalesExecutive(Employee):
    role = "sales_executive"

    def achieve_target(self):
        print(f"{self.name} is working to achieve monthly sales target.")

    def role_action(self):
        self.achieve_target()


class DevOpsEngineer(Employee):
    role = "devops_engineer"

    def monitor_servers(self):
        print(f"{self.name} is monitoring the servers and infrastructure.")

    def deploy_updates(self):
        print(f"{self.name} is deploying new code updates.")

    def role_action(self):
        self.monitor_servers()
