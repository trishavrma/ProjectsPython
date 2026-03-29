import pandas as pd

df = pd.read_excel("employee.xlsx")

print("\nEmployees in Automotive Domain:\n")
print(df[df['Department'] == 'Automotive'])

eid = int(input("Enter Employee ID: "))
print("\nEmployee Details:\n")
print(df[df['EmployeeID'] == eid])

print("\nDevelopers List:\n")
print(df[df['Designation'] == 'Developer'])