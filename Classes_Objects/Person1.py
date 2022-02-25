class Person:
    name="No name :("
    def __init__(self,name="Sushmitha"):
        self.name=name
def main():
    op=Person("Prashanth")
    print(op.name)
    gaint=Person()
    print("My Sister name is ",gaint.name)
main()