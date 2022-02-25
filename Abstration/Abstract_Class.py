class AB_class(object):
    def set_val(self, val):
        return

    def get_val(self):
        return


def hello():
    print("Calling Hello method")
    print("I am not part of the abstract methods defined in AB_class")


class Main_method(AB_class):
    def __init__(self):
        self._val = None

    def set_val(self, input):
        self._val = input


obj = Main_method()
obj.set_val(200)
print(obj.get_val())
hello()
