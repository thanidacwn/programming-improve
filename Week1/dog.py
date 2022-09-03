'''Practice in Object-Oriented Programming about Classes and Objects use __str__ '''

class Dog:

    def __init__(self, name, age):
        """ initialize """
        self.name = name
        self.age = age

    def __str__(self):
        """ return string """
        return f"{self.name} is {self.age} years old "

    def speak(self, sound):
        return f"{self.name} says {sound}"