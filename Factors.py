def factors(a):
  for i in range(1,a+1):
     if(a%i==0):
        print(i)

def factorial(a):
    if a<0:
        return 0
    elif(a==0 or a==1):
      return 1
    else:
        fact=1
        while (a>1 and a!=0):
            fact=fact*a
            a=a-1
        return fact

def number(a):
    if a>0:
        print("Positive Number");
    elif a<0:
        print("Negative Number");
    else:
        print("Zero");

def even_odd(a):
    if(a%2==0):
        print("Even Number")
    elif(a%2!=0):
        print("Odd Number")

a=int(input("Enter number : "))
print('*-*-* Finding the factors of the Number *-*-*')
factors(a)
print('*-*-* Finding the factorial of the Number *-*-*')
print(factorial(a))
print("*-*-* Nature of the Number *-*-*")
number(a)
even_odd(a)