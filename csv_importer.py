import csv
from roles import Ceo, Accountant, HRManager, DevOpsEngineer, Employee, SalesExecutive


class CSVImporter:

    def get_role_class(self, role_key):
        role_map = {
            "ceo": Ceo,
            "accountant": Accountant,
            "devops_engineer": DevOpsEngineer,
            "hr_manager": HRManager,
            "sales_executive": SalesExecutive
        }
        return role_map.get(role_key.lower(), Employee)

    def import_employees(self, filename):
        employee_list = []
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                role_key = row.get("role")
                employee_class = self.get_role_class(role_key)
                emp = employee_class(
                    row.get("name"),
                    row.get("emp_id"),
                    row.get("base_salary"),
                    row.get("joining_date"),
                    row.get("department")
                )
                employee_list.append(emp)
        return employee_list
