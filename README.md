# Employee Management System

A command-line employee management system built in Python demonstrating object-oriented design, role-based access control, and CSV-driven data loading.

Built as an OOP exercise — models a small company with departments, employees, role-specific permissions, and a salary ledger.

## Features

- **Role-based access control** — CEO, Accountant, HR Manager, Sales Executive, DevOps Engineer each have different menu permissions
- **Department auto-assignment** — employees are loaded from CSV and grouped into departments automatically
- **Salary ledger** — generates salary slips with experience-based bonuses (20% for >2 years of service)
- **Role-specific actions** — each role has its own behavior (CEO can fire, Accountant generates reports, HR organizes training, etc.)
- **Login by employee ID** — the menu adapts to who logged in

## Project Structure

```
.
├── main.py              # Entry point, menu loop, permission checks
├── company.py           # Company aggregate — owns departments and employees
├── departments.py       # Department + AccountsDepartment (has SalaryManager)
├── employee.py          # Base Employee class — experience + bonus logic
├── roles.py             # Ceo, Accountant, HRManager, SalesExecutive, DevOpsEngineer
├── salary_manager.py    # Generates salary slips, maintains ledger
├── csv_importer.py      # Loads employees from CSV → role-specific instances
└── employees.csv        # Sample data
```

## How to Run

Requires Python 3.7+. No external dependencies.

```bash
python main.py
```

You'll be prompted for an employee ID. Try these from the sample CSV:

| ID    | Name  | Role             | Access                          |
|-------|-------|------------------|---------------------------------|
| E102  | Ahmed | CEO              | All menu options                |
| E101  | Zara  | Accountant       | View departments, role action   |
| E103  | Sana  | HR Manager       | View, search by ID, role action |
| E104  | Ali   | DevOps Engineer  | Role action only                |

## Permissions Matrix

| Action                     | CEO | Accountant | HR | Sales | DevOps |
|----------------------------|:---:|:----------:|:--:|:-----:|:------:|
| 1. View employees by dept  | ✓   | ✓          | ✓  | ✓     |        |
| 2. View salary ledger      | ✓   |            |    |       |        |
| 3. Search salary by ID     | ✓   |            | ✓  |       |        |
| 4. Fire an employee        | ✓   |            |    |       |        |
| 5. Perform role action     | ✓   | ✓          | ✓  | ✓     | ✓      |

## Concepts Demonstrated

- Inheritance and polymorphism (`Employee` → role subclasses, each with its own `role_action()`)
- Composition (`Company` → `Department` → `Employee`; `AccountsDepartment` → `SalaryManager`)
- Class-as-key lookup for permissions (`{Ceo: {"all"}, Accountant: {1, 5}, ...}`)
- CSV → object factory pattern (`CSVImporter.get_role_class()`)
- Separation of concerns across modules
