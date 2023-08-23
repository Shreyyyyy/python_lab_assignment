class CustomException(Exception):
    pass
date=input("Enter the date of birth in the format DD/MM/YYYY ")
if date=="":
    print("Please enter the date of birth. Try again later")
    exit(0)
elif (date=="q" or date=="Q"):
    raise CustomException("Bye! Hope you run this program again")
elif date=='?':
    date=input("Enter the date of birth in the format DD/MM/YYYY ")
    try:
        d=date[0:2]
        m=date[3:5]
        y=date[6:10]
        if (int(d)>=1 and int(d)<=31 and int(m)>=1 and int(m)<=12):
            AGE=2023-int(y)
            print("Your age is ",AGE)
    except (IndexError,ValueError):
        print("Please enter the date of birth in the format DD/MM/YYYY")
else:
    try:
        if(date[0]=="0"):
            d=date[1:2]
        else:
            d=date[0:2]
    except (IndexError,ValueError):
        print("Please enter the date of birth in the format DD/MM/YYYY")
    try:
        if(date[0]=='0'):
            m=date[4:5]
        else:
             m=date[3:5]
    except (IndexError,ValueError):
        print("Please enter the date of birth in the format DD/MM/YYYY")
    try:
        y=date[6:10]
    except (IndexError,ValueError):
        print("Please enter the date of birth in the format DD/MM/YYYY")
    try:
        if (int(d)>=1 and int(d)<=31 and int(m)>=1 and int(m)<=12):
            AGE=2023-int(y)
            print("Your age is ",AGE)
        else:
            print("Please enter the date of birth in the format DD/MM/YYYY")
    except ValueError:
            print("Please enter the date of birth in the format DD/MM/YYYY")
