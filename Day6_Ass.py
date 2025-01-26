'''Using the Pandas library, perform the following tasks:

1. Create a DataFrame from the following data:
   | Name     | Age | Department   | Salary  |
   |----------|-----|--------------|---------|
   | John     | 28  | HR           | 45000   |
   | Alice    | 34  | IT           | 60000   |
   | Bob      | 23  | Marketing    | 35000   |
   | Diana    | 29  | Finance      | 50000   |
'''

import pandas as pd

# Data to create the DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Diana'],
    'Age': [28, 34, 23, 29],
    'Department': ['HR', 'IT', 'Marketing', 'Finance'],
    'Salary': [45000, 60000, 35000, 50000]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
print('\n')
#***********************************************************************

'''2. Write code to:
   - Display the first 2 rows of the DataFrame.
   - Add a new column named `Bonus` where the bonus is 10% of the salary.
   - Calculate the average salary of employees in the DataFrame.
   - Filter and display employees who are older than 25.'''


# Task 1: Display the first 2 rows of the DataFrame
print("First 2 rows of the DataFrame:")
print(df.head(2))
print("\n")

# Task 2: Add a new column named 'Bonus' where the bonus is 10% of the salary
df['Bonus'] = df['Salary'] * 0.10
print("DataFrame with Bonus column added:")
print(df)
print("\n")

# Task 3: Calculate the average salary of employees
average_salary = df['Salary'].mean()
print("Average salary of employees:", average_salary)
print("\n")

# Task 4: Filter and display employees who are older than 25
filtered_df = df[df['Age'] > 25]
print("Employees older than 25:")
print(filtered_df)

