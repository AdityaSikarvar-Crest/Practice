class Bird:
    def intro(self):
        print("There are many types of birds.")
    
    def flight(self):
        print("Most of the birds can fly but some cannot.")

class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")

class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")

def demonstrate_polymorphism(bird):
    bird.intro()
    bird.flight()

# Create instances of each class
bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

# Demonstrate polymorphism
demonstrate_polymorphism(bird)
demonstrate_polymorphism(sparrow)
demonstrate_polymorphism(ostrich)