class MyClass:
    def __init__(self, val=10):
        self._val = val

    def get_val(self):
        return self._val

    def set_val(self, value):
        self._val = value


obj1 = MyClass()
obj2 = MyClass()
obj1.set_val(60)
obj2.set_val(80)
print(obj1.get_val())
print(obj2.get_val())