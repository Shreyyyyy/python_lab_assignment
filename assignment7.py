import numpy as np

# Creating a structured array for the Employee table
employee_data = np.array([(1000, 'Torbati', 'Yolanda', 'F', 'Programmer'),
                           (1001, 'Kleinn', 'Joel', 'M', 'Programmer'),
                           (1002, 'Ginsburg', 'Laura', 'F', 'President'),
                           (1003, 'Cox', 'Jennifer', 'F', 'Programmer'),
                           (1005, 'Ziada', 'Mauri', 'M', 'Product designer'),
                           (1006, 'Keyser', 'Cara', 'F', 'Account Executive'),
                           (1010, 'Smith', 'Roxie', 'M', 'Programmer'),
                           (1011, 'Nelson', 'Robert', 'M', 'Programmer'),
                           (1012, 'Sachsen', 'Lars', 'M', 'Support Technician'),
                           (1013, 'Shanon', 'Don', 'M', 'Product Designer')],
                          dtype=[('Emp_id', 'i4'), ('Last_Name', 'U20'), ('First_Name', 'U20'), ('Gender', 'U1'), ('Title', 'U20')])

# 1. Count Male employees
male_count = np.sum(employee_data['Gender'] == 'M')
print("Number of Male employees:", male_count)

# 2. Display details of employees whose Last_Name starts with 'S'
#last_name_s = employee_data[employee_data['Last_Name'].startswith('S')]
#print("Employees whose Last_Name starts with 'S':\n", last_name_s)

# 3. Sort Female Employee details in descending order based on First_Name
female_employees = employee_data[employee_data['Gender'] == 'F']
sorted_female_employees = np.sort(female_employees, order='First_Name')[::-1]
print("Female Employee details sorted in descending order based on First_Name:\n", sorted_female_employees)

# 4. Extract 1D array and reshape it into 2D array
emp_ids_1d = employee_data['Emp_id']
emp_ids_2d = emp_ids_1d.reshape(5, 2)  # Reshape into a 5x2 matrix
print("2D Array of Emp_ids:\n", emp_ids_2d)

# 5. Extract a matrix using Boolean and Fancy indexing
indices = [1, 3, 5]  # Employee indices to extract
selected_employees = employee_data[indices]
print("Selected employees using Boolean and Fancy indexing:\n", selected_employees)


#1002, 'Ginsburg' , 'President'
#1003, 'Cox' , 'Programmer'
#1005, 'Ziada', 'Product designer'
#1006, 'Keyser','Account Executive'
#1010, 'Smith', 'Programmer'
#1011, 'Nelson', 'Programmer'
#1012, 'Sachsen','Support Technician'


#1000, 'Torbati', 'Yolanda', 'F', 'Programmer'
#1001 , 'Kleinn', 'Joel', 'M', 'Programmer'
#1002, 'Ginsburg', 'Laura', 'F', 'President'
#1003, 'Cox', 'Jennifer', 'F', 'Programmer'
#1005, 'Ziada', 'Mauri', 'M', 'Product designer'
#1006, 'Keyser', 'Cara', 'F', 'Account Executive'
#1010, 'Smith', 'Roxie', 'M', 'Programmer'
#1011, 'Nelson', 'Robert', 'M', 'Programmer'
#1012, 'Sachsen', 'Lars', 'M', 'Support Technician'
#1013, 'Shanon', 'Don', 'M', 'Product Designer'