
class SalaryManager:
    def __init__(self):
        self.ledger = []

    def generate_salary_slip(self, emp):
        years_of_service = emp.experienced_years()
        incremented_salary = emp.bonus()

        slip = {
            "Name": emp.name,
            "Emp_ID": emp.emp_id,
            "BaseSalary": emp.base_salary,
            "YearsOfService": years_of_service,
            "incremented_Salary": incremented_salary,
            "JoiningDate": emp.joining_date,
            "Department": emp.department,
        }

        self.ledger.append(slip)
        return slip

    def get_ledger(self):
        return self.ledger
