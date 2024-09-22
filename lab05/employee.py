"""
Cleaning Employee dataset:
1. Defined the problems in this dataset.
2. Make sure that no white space in column headers
3. No leading or ending white space in each values
4. No Duplicated data
5. Keep the correct format text data
6. Keep a single value in each column

ex: Dataset employee 
1. The problem of this dataset
- Termination date null on many rows
- First name column appear every print
"""
import pandas as pd
class Employee:
    def __init__(self, path) -> None:
        self.path = path

    def load(self):
        # df = pd.re
        return pd.read_excel(self.path, header=0)
    


employee = Employee("data/Employee Dataset.xlsx")
df = employee.load()
# Strip whitespaces from all column names
df.columns = df.columns.str.strip()
print(df.columns.tolist())
df = df.rename(columns={'First name': 'first_name', 
                        'Last name': 'last_name',
                        'Gender': 'gender',
                        'Department': 'department',
                        'Position': 'position',
                        'Employee level': 'employee_level',
                        'Performance score': 'performance_score',
                        'Employment satisfaction': 'employment_satisfaction',
                        'Hired date': 'hired_date',
                        'Termination date': 'termination_date'})

# print(df.columns)
print(df.columns.tolist())
# print(df['termination_date'])
# print(df['department'])

#1. Which Department has the most employee?
# Count the occurrences of each department
department_counts = df['department'].value_counts()
# print("department count: ", department_counts)
# Display the department with the most employees
most_employees_department = department_counts.idxmax()  # Department with the most employees
most_employees_count = department_counts.max()  # Number of employees in that department
print(f"The department with the most employees is: {most_employees_department} with {most_employees_count} employees.")

#2. Which Employee Level has the most employee?
employee_level_counts = df['employee_level'].value_counts()
# print("employee_level count: ", employee_level_counts)
# Display the employee level with the most employees
most_employees_level = employee_level_counts.idxmax()
most_employees_level_count = employee_level_counts.max()
print(f"The employee level with the most employees is: {most_employees_level} with {most_employees_level_count} employees.")

#3. Which Employee Level has the highest Performance Score in average?
# Group by 'employee_level' and calculate the average performance score
avg_performance_by_level = df.groupby('employee_level')['performance_score'].mean()
print("group of avg performance: ", avg_performance_by_level)

# Find the employee level with the highest average performance score
highest_avg_performance_level = avg_performance_by_level.idxmax()  # Employee level with the highest average score
highest_avg_performance_score = avg_performance_by_level.max()  # The highest average performance score

print(f"Employee level with the highest average performance score is: {highest_avg_performance_level} with an average score of {highest_avg_performance_score:.2f}.")

#4. Which Department has Performance Score in average?
# Group by 'department' and calculate the average performance score
avg_performance_by_department = df.groupby('department')['performance_score'].mean()

# Display the average performance score for each department
print("Average Performance Score by Department:")
print(avg_performance_by_department)

#5. Which Department has the most Senior?
# Filter for Senior employees
senior_employees = df[df['employee_level'].str.strip() == 'Senior']
# print("senior employee: ", senior_employees)

# Count the number of Senior employees in each department
senior_count_by_department = senior_employees['department'].value_counts()

# Display the department with the most Senior employees
most_seniors_department = senior_count_by_department.idxmax()  # Department with most Seniors
most_seniors_count = senior_count_by_department.max()  # Number of Seniors in that department

print(f"The department with the most Senior employees is: {most_seniors_department} with {most_seniors_count} Senior employees.")







