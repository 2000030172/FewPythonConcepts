print(' *-*-* Pascals Triangle *-*-* ')
def factorial(i):
    if(i==0):
        return 1;
    return i*factorial(i-1)
rows=int(input("Enter the number of rows : "))
for i in range(rows):
    for j in range(rows-i+1):
        print(end=" ")
    for j in range(i+1):
        result=factorial(i)//(factorial(j)*factorial(i-j))
        print(result, end=" ")
    print()
    

