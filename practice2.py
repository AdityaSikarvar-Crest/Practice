class OuterClass:
    def __init__(self, outer_var):
        self.outer_var = outer_var
        self.inner_instance = self.InnerClass()
    def show(self):
        print("This is an outer class")


    class InnerClass:
        def __init__(self):
            self.inner_var = "Inner Variable"
        def show(self):
            print("This is an inner class")

# Example usage
outer_instance = OuterClass("Outer Variable")
inner_var2=OuterClass.InnerClass()
# print(inner_var2.inner_var)
# print(outer_instance.outer_var)  # Output: Outer Variable
# print(outer_instance.inner_instance.inner_var)  # Output: Inner Variable
outer_instance.show()
inner_var2.show()