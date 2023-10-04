import re

def verify_form_inputs(name, phone, email, dob, payment_option):
    # Verify name (letters and dot)
    if re.match("^[A-Za-z. ]+$", name):
        print("Name input is correct.")
    else:
        print("Invalid name input.")

    # Verify input has only digits
    if re.match("^\d+$", phone):
        print("Digit input has only digits.")
    else:
        print("Invalid digit input.")

    # Verify email ID
    if re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        print("Email ID is valid.")
    else:
        print("Invalid email ID.")

    # Verify date of birth (dd/mm/yyyy format)
    if re.match("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", dob):
        print("Date of birth is valid.")
    else:
        print("Invalid date of birth.")
    payment_option.lower()
    # Verify payment option (Credit/Debit/Netbanking)
    if payment_option in ['credit', 'debit', 'netbanking']:
        print("Payment option is valid.")
    else:
        print("Invalid payment option.")

    # Verify if all entries received correct input
    if all([re.match("^[A-Za-z. ]+$", name),
            re.match("^\d+$", phone),
            re.match("^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email),
            re.match("^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$", dob),
            payment_option in ['credit', 'debit', 'netbanking']]):
        print("All entries received correct input.")
    else:
        print("At least one entry received incorrect input.")

Name=input("Enter your name please ")
Phone=input("Enter your phone number ")
Email=input("Enter your email address ")
DOB=input("Enter your date of birth (dd/mm/yyyy format) ")
payment=input("Enter the payment method Credit Debit or NetBanking ")

verify_form_inputs(Name, Phone, Email, DOB, payment)