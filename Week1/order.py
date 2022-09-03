'''Practice in Object-Oriented Programming about Classes and Objects use __add__'''

# Step Of OOP:
#         1. define a class : All class definitions start with the class keyword 
#         2. initialize : .__init__() can give any number of parameters, 
#                         but the first parameter will always be a variable called self
#         3. creat function


class Orders:

    def __init__(self, items):
        "initialize"
        self.items = items

    def __add__(self, other):
        "add items"
        return self.items + other.items

order1 = Orders([1, 2, 3, 4, 5, 6])
order2 = Orders([10, 20, 30])

print("order1 + order2=", order1 + order2)