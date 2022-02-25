try:
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    c=a/b;
    print("The value of a/b is %d"%c);

# except Exception as e:
#     print(e)
#
except ValueError as e:
    print(e)

# except IndexError as e:
#     print(e)

# except ZeroDivisionError as e:
#     print(e)

else:
    print("Printing else block")