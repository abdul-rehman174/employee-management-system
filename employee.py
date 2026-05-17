from datetime import datetime


class Employee:
    role = "unidentified"

    def __init__(self, name, emp_id, base_salary, joining_date, department):
        self.name = name
        self.emp_id = emp_id
        self.base_salary = float(base_salary)
        self.joining_date = joining_date
        self.department = department

    def experienced_years(self):
        joining = datetime.strptime(self.joining_date, "%Y-%m-%d")
        today = datetime.now()
        experienced_years = (today-joining).days//365
        return experienced_years

    def bonus(self):
        if self.experienced_years() > 2:
            return self.base_salary * 0.20
