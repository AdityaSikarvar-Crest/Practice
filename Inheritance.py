# Single Inheritance
class Parent:
    def func1(self):
        print("This is function 1 in Parent class")

class Child(Parent):
    def func2(self):
        print("This is function 2 in Child class")

# Multiple Inheritance
class Mother:
    def func3(self):
        print("This is function 3 in Mother class")

class Father:
    def func4(self):
        print("This is function 4 in Father class")

class Child(Mother, Father):
    def func5(self):
        print("This is function 5 in Child class")

# Multilevel Inheritance
class Grandparent:
    def func6(self):
        print("This is function 6 in Grandparent class")

class Parent(Grandparent):
    def func7(self):
        print("This is function 7 in Parent class")

class Child(Parent):
    def func8(self):
        print("This is function 8 in Child class")

# Hierarchical Inheritance
class Parent:
    def func9(self):
        print("This is function 9 in Parent class")

class Child1(Parent):
    def func10(self):
        print("This is function 10 in Child1 class")

class Child2(Parent):
    def func11(self):
        print("This is function 11 in Child2 class")

# Hybrid Inheritance
class Base:
    def func12(self):
        print("This is function 12 in Base class")

class Derived1(Base):
    def func13(self):
        print("This is function 13 in Derived1 class")

class Derived2(Base):
    def func14(self):
        print("This is function 14 in Derived2 class")

class Derived3(Derived1, Derived2):
    def func15(self):
        print("This is function 15 in Derived3 class")

# Creating objects and calling methods to demonstrate inheritance
if __name__ == "__main__":
    # Single Inheritance
    obj1 = Child()
    obj1.func1()
    obj1.func2()

    # Multiple Inheritance
    obj2 = Child()
    obj2.func3()
    obj2.func4()
    obj2.func5()

    # Multilevel Inheritance
    obj3 = Child()
    obj3.func6()
    obj3.func7()
    obj3.func8()

    # Hierarchical Inheritance
    obj4 = Child1()
    obj5 = Child2()
    obj4.func9()
    obj4.func10()
    obj5.func9()
    obj5.func11()

    # Hybrid Inheritance
    obj6 = Derived3()
    obj6.func12()
    obj6.func13()
    obj6.func14()
    obj6.func15() 