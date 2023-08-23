import Program_3
name=input("Enter the name of the Food Please ensure that it has atmost 5 characters and atleast 1 letter ")
c=0
for i in name:
    if(i.isalpha()):
        c=c+1
if(len(name)>5 or c==0):
    print("Wrong Input format Ensure the food name has maximum of 5 characters or atleast 1 letter Try Again ")
else:
    Program_3.EncodeQR(name)



def EncodeQR(name):
    l=["10000000","01000000","00100000","00010000","00001000"]
    count=0
    pad=""
    for i in name:
        asc=ord(i)
        bi=bin(asc)
        bi=bi[2:]
        pad=pad+l[count]+bi
        count=count+1
    print("The QR CODE for the food ",name," is ")
    print(pad)


