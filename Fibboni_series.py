def armstrong(n):
    sum=0
    temp=n
    while(n>0):
        r=n%10
        sum=sum+(r*r*r)
        n=n/10
    if(temp==sum):
        print("Armstrong Number")
    else:
        print("Not a armstrong Number")
        
armstrong(153)