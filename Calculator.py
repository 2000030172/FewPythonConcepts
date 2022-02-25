def add(a,b):
    num=a+b
    print("Add of two numbers : ",num)

def mul(a,b):
    num=a*b
    print("Multiply of two numbers : ",num)

def sub(a,b):
    if(a-b>0):
        num=a-b
        print("Substract of two numbers : ",num)
    elif(b-a>0):
        num=b-a
        print("Substract of two numbers : ",num)

def div(a,b):
    if(a>0 and b>0):
        num=a/b
        print("Division of two numbers : ",num)

    
print(" *-*-* Basic Simple Calculator *-*-* ")
while (True):
    print("Main Menu of the Calulator")
    print("1. Addition")
    print("2. Substraction")
    print("3. Division")
    print("4. Multiply")
    cho=int(input("Enter your choice : "))
    #switch cho
    if cho==1:
        a=int(input("Enter a value : "))
        b=int(input("Enter b value : "))
        add(a,b)
        break
    elif(cho==2):
        a=int(input("Enter a value : "))
        b=int(input("Enter b value : "))
        sub(a,b)
        break
    elif(cho==3):
        a=int(input("Enter a value : "))
        b=int(input("Enter b value : "))
        div(a,b)
        break
    elif(cho==4):
        a=int(input("Enter a value : "))
        b=int(input("Enter b value : "))
        mul(a,b)
        break
    else:
        print("Enter proper number from the Main Menu")
        break