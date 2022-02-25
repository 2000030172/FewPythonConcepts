print(" *-*-* Arithematic and Logic operations *-*-* ")
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

def roundup(a,b):
    num=a//b
    print("Round of two numbers : ",num)

def mod(a,b):
    num=a%b
    print("Modulus of two numbers : ",num)

def xor(a,b):
    num=a^b
    print("Bitwise operator XOR of two numbers : ",num)

def bitor(a,b):
    num=a|b
    print("Bitwise operator OR of two numbers : ",num)

def bitand(a,b):
    num=a&b
    print("Bitwise operator AND of two numbers : ",num)

def nota(a):
    num=~a
    print("Not of a value : ",num)

def notb(b):
    num=~b
    print("Not of b value : ",num)

def power(a,b):
    num=a**b
    print("Power of two numbers : ",num)
    
a=int(input("Enter a value : "))
b=int(input("Enter b value : "))
add(a,b)
mul(a,b)
sub(a,b)
div(a,b)
mod(a,b)
roundup(a,b)
xor(a,b)
bitor(a,b)
bitand(a,b)
nota(a)
notb(b)
power(a,b)