from salary_manager import SalaryManager


class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []


class AccountsDepartment(Department):
    def __init__(self):
        super().__init__("Accounts")
        self.salary_manager = SalaryManager()
