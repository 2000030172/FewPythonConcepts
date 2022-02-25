row=int(input("Enter a value : "))
print('Left Angled Triangle')
def pattern(row):
    myList=[]
    for i in range(1,row+1):
        print()
        myList.append(" * "*i)
    print("\n".join(myList))
pattern(row)
