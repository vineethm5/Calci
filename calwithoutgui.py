
def add(a,b):
    return(a+b)

def sub(a,b):
    return(a-b)

def mul(a,b):
    return(a*b)

def div(a,b):
    return(a/b)
m=1
while(m!=0):
    a=int(input("Enter the 1st no"))
    b=int(input("Enter the second no"))
    print("Enter the operstion that you want to perform")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")

    choice=int(input("Enter now"))

    # if choice in ("1","2","3","4"):
    if(choice ==1):
        print(add(a,b))
    elif(choice ==2):
        print(sub(a,b))
    elif(choice ==3):
        print(mul(a,b))
    elif(choice ==4):
        print(div(a,b))

    print("Do you want to continue Y/N")
    n=input()
    if(n == "Y" or n== "y"):
        m=1
    else:
        m=0