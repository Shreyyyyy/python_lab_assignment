#1 STR

#a) 

para = """Airline ticket booking has revolutionized the way people travel, offering 
seamless convenience and accessibility to flights worldwide. With the advent of advanced online 
platforms and mobile applications, passengers can now effortlessly secure their 
journeys with just a few clicks. This domain encompasses a wide array of services, including flight 
searches, fare comparisons, seat selections, and 
payment processing, all streamlined to provide a user-friendly experience. Travelers can 
choose from an extensive range of airlines, routes, and timings, tailoring their itineraries 
to suit their preferences and budgets. Moreover, the integration of real-time updates on flight 
availability and price fluctuations ensures that customers are well-informed before making 
their final bookings. As technology continues to evolve, the airline ticket booking domain 
constantly seeks innovative ways to enhance the overall travel experience, making it an indispensable 
aspect of modern-day aviation and tourism."""

print("------------------------------------------------------------------")

print(para.lower().count("airline ticket booking")) # frequency

print(len(para.split(" "))) # counting words

print(len(para.split("."))) #counting lines

print(len(para)) #counting chars

print("------------------------------------------------------------------")


#b)

def encrypt_string(input_string, n):
    encrypted_string = ""
    for char in input_string:
        if char.isalpha():
            base = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - base + n) % 26 + base)
            encrypted_string += shifted_char
        else:
            encrypted_string += char
    return encrypted_string

# Input from the user
input_string = para
#n = int(input("Enter the value of n: "))
n=3
# Encrypt the string using the given method
encrypted_string = encrypt_string(input_string, n)

print("Encrypted Output:", encrypted_string)

print("------------------------------------------------------------------")


#2) 

def pay(wage,hours):
    if(hours>40):
        s = print(1.5*wage*hours)
        return s
    else:
        q = print(wage*hours)
        return q
    
pay(10,35)
pay(10,45)

#3)

# Create the list of tuples with two numeric values and one string value
houses_for_rent = [('main st.', 4, 4000), ('elm st.', 1, 1200), ('pine st.', 2, 1600)]

# Sort the list in ascending order by first numeric value (index 1)
houses_for_rent.sort(key=lambda x: (x[1], x[2]))

# Sort the list in descending order by second numeric value (index 2)
houses_for_rent.sort(key=lambda x: x[2], reverse=True)

# Sort the list in alphabetical order of string value (index 0)
houses_for_rent.sort()

# Print the sorted list (a)
print("Sorted by first numeric value (ascending):")
print(houses_for_rent)

# Revert the sorting of the second numeric value to the original order (b)
houses_for_rent.sort(key=lambda x: (x[1], x[2]))

print("\nSorted by second numeric value (descending):")
print(houses_for_rent)

# Sort the list again in alphabetical order of string value (index 0) (c)
houses_for_rent.sort()

print("\nSorted alphabetically by string value:")
print(houses_for_rent)