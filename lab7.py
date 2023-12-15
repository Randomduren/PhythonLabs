class Parent:
    def display(self):
        print("Это метод родительского класса")

class Child(Parent):
    def display(self):
        print("Это метод дочернего класса")


parent = Parent()
child = Child()


parent.display()
child.display()
