class MyClass():
    def some_method(self):
        print(f"Say hi to {self}")

class MyOtherClass():
    def __init__(self, name):
        self.name = name

myObject = MyClass()
myOtherObject = MyOtherClass('Sammy')

myObject.some_method()
print(myOtherObject.name)
