class Person:
    name="I have no name :("
    def sayname(self):
        print('Who are r u.....?  '+self.name)

def main():
    op=Person()
    op.sayname()
    op.name="Big Similey : D  :)"
    op.sayname()
main()