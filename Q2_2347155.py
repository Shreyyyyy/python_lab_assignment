print("----------------------------------------------------------")
print("------------Q2---2347155------Shreyans Jain---------------")
print("----------------------------------------------------------")
# Function to check if a number is divisible by 3
def div_3(num):
    return num % 3 == 0

# Given list
shrey = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# Check if the given list is divisible by 3 or not
divisible_by_3 = [num for num in shrey if div_3(num)]
print("Numbers divisible by 3:", divisible_by_3)

# Square of even numbers in the list
square_of_even = [num**2 for num in shrey if num % 2 == 0]
print("Square of even numbers:", square_of_even)

# Sum of digits of all EVEN numbers in the list
sum_of_digits_even = [num for num in shrey if num % 2 == 0]
sum=0 
for i in sum_of_digits_even:
    sum+=i
print("sum is : " ,sum)

# Remove duplicate numbers in the list
unique_list = list(set(shrey))
print("List with duplicates removed:", unique_list)


print("----------------------------------------------------------")
#----------------------------------------------------------------------------------------

# Dictionary to store the details of company employees
employee_details = {
    'Virat Kohli': '5 November 1988',
    'Umesh Yadav': '25 October 1987',
    'Manish Pandey': '10 September 1989',
    'Rohit Sharma': '30 April 1987',
    'Ravindra Jadeja': '6 December 1988',
    'Hardik Pandya': '11 October 1993'
}

# Function to get the birthdate of an employee
def birthDate(name):
    return employee_details.get(name, "Employee not found")

# Example:
print(birthDate('Umesh Yadav')) # 25 october

print("----------------------------------------------------------")
