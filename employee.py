import json

employees = [
    {"employee_id": 201, "name": "Raj", "department": "IT", "salary": 45000},
    {"employee_id": 202, "name": "Sneha", "department": "HR", "salary": 55000},
    {"employee_id": 203, "name": "Aakash", "department": "Finance", "salary": 65000},
    {"employee_id": 204, "name": "Pooja", "department": "IT", "salary": 75000},
    {"employee_id": 205, "name": "Rohan", "department": "Marketing", "salary": 50000}
]

with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

with open("employees.json", "r") as file:
    employee_data = json.load(file)

print("All Employees:")

for employee in employee_data:
    print(
        employee["employee_id"],
        employee["name"],
        employee["department"],
        employee["salary"]
    )

print("\nEmployees with salary greater than ₹50,000:")

for employee in employee_data:
    if employee["salary"] > 50000:
        print(employee["name"], employee["salary"])

highest_salary_employee = max(
    employee_data,
    key=lambda employee: employee["salary"]
)

print("\nHighest Paid Employee:")
print("Name:", highest_salary_employee["name"])
print("Salary:", highest_salary_employee["salary"])

total_salary = 0

for employee in employee_data:
    total_salary += employee["salary"]

average_salary = total_salary / len(employee_data)

print("Average Salary:", average_salary)