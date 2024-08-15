'''
Write a Python class Employee with properties id, name, salary, and department and methods like _init_ calculateSalary, assignDepartment and _str_.

Sample Employee Data:

"E7876", "ADAMS", 50000, "ACCOUNTING"
"E7499", "JONES", 45000, "RESEARCH"
"E7900", "MARTIN", 50000, "SALES"
"E7698", "SMITH", 55000, "OPERATIONS"
Use 'assignDepartment' method to change the department of an employee.

Use '_str_' method to print the details of an employee.

Use 'calculateSalary' method takes two arguments: salary and hours_worked, which is the number of hours worked by the employee. If the number of hours worked is more than 50, the method computes overtime and adds it to the salary.

Overtime is calculated as following formula: overtime = hours_worked - 50 Overtime amount = (overtime * (salary / 50))


'''

class Staff:
    def __init__(self, staff_id, full_name, base_salary, team):
        self.staff_id = staff_id
        self.full_name = full_name
        self.base_salary = base_salary
        self.team = team

    def compute_pay(self, hours_worked):
        standard_hours = 40
        overtime_rate = 1.5
        if hours_worked > standard_hours:
            overtime_hours = hours_worked - standard_hours
            overtime_pay = overtime_hours * (self.base_salary / standard_hours) * overtime_rate
            total_salary = self.base_salary + overtime_pay
        else:
            total_salary = self.base_salary
        return total_salary

    def change_team(self, new_team):
        self.team = new_team

    def __str__(self):
        return f"Staff ID: {self.staff_id}\nName: {self.full_name}\nTeam: {self.team}"

# Creating an instance
john_doe = Staff(12345, "John Doe", 3200, "Engineering")

print(john_doe)
print("="*80)

print(john_doe.compute_pay(50))
print("="*80)

john_doe.change_team("Research & Development")
print(john_doe.team)
print(john_doe)
