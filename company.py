from departments import Department, AccountsDepartment


class Company:
    def __init__(self, name):
        self.name = name
        self.departments = {"Accounts": AccountsDepartment()}

    def get_employee_by_id(self, employ_id):
        for depart in self.departments.values():
            for emp in depart.employees:
                if emp.emp_id == employ_id:
                    return emp
        print("Person with that ID not found")

    def get_departments(self):
        return self.departments

    def assign_employees_to_departments(self, employee_list):
        for emp in employee_list:
            if emp.department not in self.departments:
                self.departments[emp.department] = Department(emp.department)
            self.departments[emp.department].employees.append(emp)

    def get_salary_manager(self):
        return self.departments["Accounts"].salary_manager