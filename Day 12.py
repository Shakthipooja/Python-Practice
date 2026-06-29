#INHERITANCE
#person to student
class Person:
    def display(self):
        print("I am a person")
class Student(Person):
    pass
s=Student()
s.display()
#Animal to dog
class Animal:
    def eat(self):
        print("Animal eats food")
class Dog(Animal):
    pass
d=Dog()
d.eat()
#Vehical to car
class Vehicle:
    def start(self):
        print("Vehical started")
class Car(Vehicle):
    pass
c=Car()
c.start()
#METHOD OVERRIDING
#Animal sound
class Animal:
    def sound(self):
        print("Animal sound")
class Dog(Animal):
    def sound(self):
        print("Bark")
d = Dog()
d.sound()
#Shape area
class Shape:
    def area(self):
        print("Area Calculation")
class Circle(Shape):
    def area(self):
        radius = 5
        print("Area = ",3.14*radius*radius)
c = Circle()
c.area()
#ENCAPSULATION
#STUDENT MARKS
class Student:
    def __init__(self):
        self.__marks=95
    def display(self):
        print("Marks = ",self.__marks)
s = Student()
s.display()
#Bank account Example
class BankAccount:
    def __init__(self):
        self. __balance =  10000
    def show_balance(self):
        print("Balance: ",self. __balance)
account = BankAccount()
account.show_balance()
#POLYMORPHISM
#Bird Fly Example
class Bird:
    def fly(self):
        print("Birds Flies")
class Eagle:
    def fly(self):
        print("Eagle flies is high")
class Sparrow:
    def fly(self):
        print("Sparrows flies low")
birds = [Eagle(),Sparrow()]
for bird in birds:
    bird.fly()
#Payment method
class CreditCard:
    def pay(self):
        print("Paid using Credit Card")
class UPI:
    def pay(self):
        print("Paid using UPI")
class Cash:
    def pay(self):
        print("Paid using Cash")
payments = [ CreditCard(),UPI(),Cash()]
for payment in payments:
    payment.pay()

        
