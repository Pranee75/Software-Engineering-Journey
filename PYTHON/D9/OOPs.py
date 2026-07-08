# Class, Object, and Constructor

class Student:
    def __init__(self, name, age):  # Constructor
        self.name = name           # Instance attribute
        self.__age = age           # Private attribute (Encapsulation)

    def display(self):
        print(f"Name: {self.name}, Age: {self.__age}")

s1 = Student("Alice", 20)
s1.display()


# Inheritance and super()

class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        super().speak()  # Calls parent method
        print("Dog barks")

d = Dog()
d.speak()


# Encapsulation (Getters & Setters)

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount


# Abstraction

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
    