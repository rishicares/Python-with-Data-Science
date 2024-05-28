class Demo:
    def __init__ (self, name):
        self.name = name
    def display(self):
        print(f"this is demo display. The name is {self.name}")

obj1 = Demo("Prabal")
obj1.display()

print(obj1.name)

obj2 = Demo("Rahul")
print(obj2.name)