name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
department = input("Enter Department: ")
basic_salary = float(input("Enter Basic Salary: "))


da = 0.92 * basic_salary
hra = 0.58 * basic_salary
ta = 0.30 * basic_salary
lic = 500  # Fixed deduction

gross_salary = basic_salary + da + hra + ta
net_salary = gross_salary - lic

print("\n--- Employee Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", department)
print("Basic Salary:", basic_salary)
print("DA (92%):", da)
print("HRA (58%):", hra)
print("TA (30%):", ta)
print("LIC Deduction:", lic)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)