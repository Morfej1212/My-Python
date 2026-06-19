# from products.product import create_product, print_product
# from utils.price_utils import add_tax, apply_discount,format_price


# product = create_product("Laptop", 2000)

# print_product(product)

# price_with_tax = add_tax(product["price"], 0.2)

# print("Price with tax:", price_with_tax)

# discount_price = apply_discount(price_with_tax, 0.1)

# print("Price with discount:", discount_price)


# print("Final price:", format_price(discount_price))

# import cowsay


# cowsay.cow("itproger")


# y = x2 + 2x - 3
# import math


# for i in range(-5, 6):
#        b = (i ** 2 ) + (2*i) - math.cos(6)
#        print(i, b ) 

# import random

# while True:
#     x = random.randint(1, 6)
#     print(x)
#     a = input("Хочеш ще кидати?")
#     if a == "ні":
#         break

# import math

# x1 = 5
# y1 = 5
# x2 = 5
# y2 = 5
# d = math.sqrt(x2-x1)**2 + (y2-y1)**2
# print(d)

# import random
# a = 0
# b = 0
# for i in range(1, 11):
#     x = random.choice(["Орел", "Решка"])
#     if x == "Орел":
#         a +=1
#     else:
#         b +=1
    
# print(f"Орел: {a}, Решка: {b}")



# class Car:
#     def __init__(self, brand, speed, color, vinCod = 0):
#         self.brand = brand
#         self.speed = speed
#         self.color = color
#         self.__vinCod = vinCod

#     def drive(self):
#         print("driving", self.__vinCod)

# car1 = Car("BMW", 255, "Whait")
# car2 = Car("Audi", 120, "Blek")   
# car3 = Car("Citroen", 400, "Red")

# print(car1.brand)
# print(car2.brand)
# print(car3.brand)

# car1.drive()
# car2.drive()
# car3.drive()


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info (self):
#         print(self.title, self.author, self.pages)


# info1 = Book ("Біле ікло", "Джон Увік", 400)
# info2 = Book ("Кока", "Сінді", 100)
# info3 = Book ("Роза", "Каян", 200)

# info1.info()
# info2.info()
# info3.info()

# class Dog:
#     name = None
#     age = None
#     isHappy = None

#     def set_data(self, name, age, isHappy):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy

#     def get_data(self):
#         print(self.name, "age:", self.age, "Happy", self.isHappy)

# dog1 = Dog()
# dog1.set_data = ("Bob", 12, True)


# dog2 = Dog()
# dog2.name = "Skybi"
# dog2.age = 2
# dog2.isHappy = False

# dog1.get_data()
# dog2.get_data()

# class Calculator:
#     def add (self, a, b,):
#         return a+b
    
#     def subtract (self, a, b):
#         return a-b
    
#     def multiply (self, a, b,):
#         return a*b
    
# calc = Calculator()

# print(calc.add(3, 4))
# print(calc.subtract(2, 8))
# print(calc.multiply(3, 9))

# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit_amount(self):
#         return 
    
#     def withdraw_an_amount(self):
#         return 
    
#     def get_balance(self):
#         return
    
# bank = BankAccount()

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def get_data(self):
#          return f"{self.name} {self.age}"
 

# class Pitbul(Dog):
#     def __init__(self, name, age, isHappy):
#         super().__init__(name, age)
#         self.isHappy = isHappy


# dog1 = Dog("Bob", 2)
# dogPitbul = Pitbul("Tom", 2, True)

# print(dog1.name)
# print(dogPitbul.get_data())

# class Car:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed

#     def auto(self):
#         print(f"{self.brand} їде зі швидкістю {self.speed} км/год")

# class Disel(Car):
#     def __init__(self, brand, speed, rosxid):
#         super().__init__(brand, speed)
#         self.rosxid = rosxid

#     def ros(self):
#         self.speed -= self.rosxid 
#         return self.rosxid

# car1 = Car("BMW", 500,)
# car2 = Car("Audi", 100,)
# car3 = Car("Citroen", 1000,)

# car1.ros()
# car2.auto()
# car3.auto()

# class Dog:
#     def _init_(self, name, age):
#         self.name = name
#         self.age = age

#     def walk(self):
#         return f"{self.name} is walking."
    
# class Labrador(Dog):
#     def _init_(self, name, age, isHappy):
#         super()._init_(name, age)
#         self.isHappy = isHappy

# class Bulldog(Dog):
#     def _init_(self, name, age):
#         super()._init_(name, age)

# labrador1 = Labrador('Max', 3, True)    
# print(labrador1.walk())

# labrador2 = Labrador('Max2', 2, True)    
# print(labrador2.walk())

# bulldog1 = Bulldog('Max3', 1, True)    
# print(bulldog1.walk())

# class Car:
#     def _init_(self, make, model, year, vinCode):
#         self.make = make
#         self.model = model
#         self.year = year # public attribute
#         self._y = 2024 # protected attribute (не інсує в Python, але це конвенція для позначення захищених атрибутів)
#         self.__vinCode = vinCode # private attribute

#     def get_info(self):
#         return f"{self.year} {self.make} {self.model}"
    
#     def get_vin(self):
#         return self.__vinCode
    
#     def set_vin(self, new_vin):
#         self.__vinCode = new_vin
    
# class ElectricCar(Car):
#     def _init_(self, make, model, year, battery_size, vinCode):
#         super()._init_(make, model, year, vinCode)
#         self.battery_size = battery_size

#     def get_battery_info(self):
#         return f"This car has a {self.battery_size}-kWh battery."
    
# class GasCar(Car):
#     def _init_(self, make, model, year, fuel_capacity, vinCode):
#         super()._init_(make, model, year, vinCode)
#         self.fuel_capacity = fuel_capacity

#     def get_fuel_info(self):
#         return f"This car has a fuel capacity of {self.fuel_capacity} liters."

# electricCar1 = ElectricCar("Tesla", "Model S", 2020, 100, "5YJSA1E26MF1XXXXX")
# gasCar1 = GasCar("Toyota", "Camry", 2019, 50, "4T1B11HK")

# print(electricCar1.get_info())
# print(electricCar1.get_battery_info())
# print(electricCar1.get_vin())

# electricCar1.year = 2021
# electricCar1.set_vin("1")

# print(electricCar1.get_vin())

# print(gasCar1.get_info())
# print(gasCar1.get_fuel_info())
# print(gasCar1.get_vin())

# class Dog:
#     name = None
#     age = None
#     isHappy = None

#     def __init__(self, name, age, isHappy):
#         self.set_dog(name, age, isHappy)
#         self.get_dog()

#     def set_dog(self, name, age, isHappy = True):
#         self.name = name
#         self.age = age
#         self.isHappy = isHappy
    
#     def get_dog(self):
#         print(self.name, "age:", self.age, "isHappy:", self.isHappy)


# dog1 = Dog("Tom", 3, True)
# dog1.set_dog("Томасок", 4)
# dog2 = Dog("Dchek", 3, False)        


# class Book:
#     title = None
#     author = None
#     pages = None

#     def __init__(self, title, author,  pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def info (self):
#         print("title:", self.title, "author:", self.author, "pages", self.pages)

# book1 = Book("Заголовок", "Jon Vik", 345)
# book2 = Book("Заголовок", "Jon Vik", 10)
# book3 = Book("Заголовок", "Jon Vik", 3)

# book1.info()
# book2.info()
# book3.info()

# class Calculator:
#     add = None #додавати
#     subtract = None #віднімати
#     multiply = None #множити

#     def add (self, a, b):
#         return a + b
    
#     def subtract (self, a, b):
#         return a - b
    
#     def multiply (self, a, b):
#         return a * b

# calc = Calculator()
# print(calc.add (89, 88))
# print(calc.subtract (90, 89))
# print(calc.multiply (3, 3))


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.onwer = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
    
#     def take_off (self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#         else:
#             print("Недостатньо коштів:")
        
#     def get_balance(self):
#         return self.balance
    

# account = BankAccount("Jon", 500)

# account.deposit(50)
# account.take_off(900)

# print(account.get_balance())


# class Vehicle:
#     def move (self):
#         print("Транспорт рухається:")

# class Car(Vehicle):
#     def move(self):
#         print("Їде по дорозі")

# class Bike(Vehicle):
#     def move(self):
#         print("Їде на двох колесах")

# class Airplane(Vehicle):
#     def move(self):
#         print("Летить")

# car = Car()
# bike = Bike()
# airplane = Airplane()

# car.move()
# bike.move()
# airplane.move()


# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def work (self):
#         print("Працівник працює:")

# class Developer(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)

#     def work (self):
#         print("Пише код:")
    

# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)

#     def work (self):
#         print("Керує командою:")


# dev = Developer("Іван", 3000)
# mgr = Manager("Оля", 5000)

# dev.work()
# mgr.work()


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class Cart:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product):
#         self.products.append(product)

#     def total_price(self):
#         total = 0
#         for product in self.products:
#             total += product.price
#         return total


# cart = Cart()

# cart.add_product(Product("Phone", 500))
# cart.add_product(Product("Laptop", 1000))

# print(cart.total_price())


# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# class DiscountProduct(Product):   #Знижковий продукт
#     def __init__(self, name, price, discount):
#         super().__init__(name, price)
#         self.discount = discount  

#     def get_price(self):
#         return self.price - (self.price * self.discount / 100)



# p1 = Product("Phone", 500)
# p2 = DiscountProduct("Laptop", 1000, 20)

# print(p1.price)
# print(p2.get_price())



# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area (self):
#         pass
   
# class Triangle(Shape):         
#     def area (self, a, b):
#       return a * b/2

    
# triangle = Triangle()
# triangle.area(3, 5.5)
# print(triangle.area(3, 5.5))


# from abc import ABC, abstractmethod

# class Car(ABC):
#     @abstractmethod
#     def drive(self):
#         print("Driving the car")

#     @abstractmethod
#     def stop(self):
#         print("Stopping the car")

# class GasCar(Car):
#     def __init__(self, model, speed, color, fuel_capacity):
#         self.model = model
#         self.speed = speed
#         self.color = color
#         self.fuel_capacity = fuel_capacity

#     def drive(self):
#         print(f"{self.model} is driving at {self.speed} km/h")

#     def stop(self):
#         print(f"{self.model} has stopped")

# class ElectricCar(Car):
#     def __init__(self, model, speed, color, battery_capacity):
#         self.model = model
#         self.speed = speed
#         self.color = color
#         self.battery_capacity = battery_capacity

#     def drive(self):
#         print(f"{self.model} is driving at {self.speed} km/h")

#     def stop(self):
#         print(f"{self.model} has stopped")

# gasCar = GasCar("Toyota Camry", 180, "Blue", 50)
# print(f"Model: {gasCar.model}")
# print(f"Speed: {gasCar.speed} km/h")
# print(f"Color: {gasCar.color}")
# print(f"Fuel Capacity: {gasCar.fuel_capacity} liters")
# gasCar.drive()
# gasCar.stop()

# electricCar = ElectricCar("Tesla Model S", 250, "Red", 100)
# print(f"Model: {electricCar.model}")
# print(f"Speed: {electricCar.speed} km/h")
# print(f"Color: {electricCar.color}")
# print(f"Battery Capacity: {electricCar.battery_capacity} kWh")
# electricCar.drive()
# electricCar.stop()

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print(f"{self.name}, {self.age}, says: Woof!")

# class Cat(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print(f"{self.name}, {self.age}, says: Meow!")

# class Cow(Animal):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def make_sound(self):
#         print(f"{self.name}, {self.age}, says: Moo!")

# dog = Dog("Rex", 2)
# cat = Cat("Murka", 3)
# cow = Cow("Sirka", 8)

# dog.make_sound()
# cat.make_sound()
# cow.make_sound()

# from abc import ABC, abstractmethod

# class Transport(ABC):
#     @abstractmethod
#     def transport_go(self):
#         pass

# class Bicycle(Transport):
#     def __init__(self, name, sped):
#         self.name = name
#         self.sped = sped

#     def transport_go (self):
#         print (f"{self.name}, moves at, {self.sped} , km/hod")

# class Plane(Transport):
#     def __init__(self, name, sped):
#         self.name = name
#         self.sped = sped

#     def transport_go (self):
#         print(f"{self.name}, flies at, {self.sped} , km/hod")

# bicycle = Bicycle("Motor", 33)
# plane = Plane("Airobus", 940)

# bicycle.transport_go()
# plane.transport_go()

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f"{self.name} says Woof!")

#     # Реалізуй метод make_sound

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name

#     def make_sound(self):
#         print(f"{self.name} says Meow!")

#     # Реалізуй метод make_sound

# dog = Dog("Rex")
# cat = Cat("Murka")

# dog.make_sound()
# cat.make_sound()

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Rectangle(Shape):
#     def __init__(self,width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#        return(self.width * self.height)

# class Square(Shape):
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return(self.side * self.side)
    

# rectangle = Rectangle(5, 8)
# square = Square(6)

# print(rectangle.area())
# print(square.area())

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         return (f"{self.name} says Woof!")

# class Cat(Animal):
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         return (f"{self.name} says Meow!")
    
# dog = Dog("Rex")
# cat = Cat("Barsik")

# print(dog.sound())
# print(cat.sound())

# animals = [dog, cat]

# for animal in animals:
#     print(animal.sound())

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass
       
# class Car(Vehicle):
#     def __init__ (self, name, speed):
#         self.name = name
#         self.speed = speed

#     def move(self):
#         return f"{self.name} moves at {self.speed} km/h"

# class Bicycle(Vehicle):
#     def move(self):
#         return f"{self.name} moves at {self.speed} km/h"

# class Plane(Vehicle):
#     def move(self):
#         return f"{self.name} moves at {self.speed} km/h"

# car = Car("BMW", 500 )
# bicycle = Bicycle("Horobez", 12)
# plane = Plane("Antonov", 900)

# print(car.move())
# print(bicycle.move())
# print(plane.move())

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     def __init__(self, name, speed):
#         self.name = name
#         self.speed = speed

#     @abstractmethod
#     def move(self):
#         pass

# class Car(Vehicle):
#     def move(self):
#         return f"{self.name} moves at {self.speed} km/h"

# class Bicycle(Vehicle):
#     def move(self):
#         return f"{self.name} moves at {self.speed} km/h"

# class Plane(Vehicle):
#     def move(self):
#         return f"{self.name} flies at {self.speed} km/h"


# car = Car("BMW", 500)
# bicycle = Bicycle("Horobez", 12)
# plane = Plane("Antonov", 900)

# print(car.move())
# print(bicycle.move())
# print(plane.move())

# try:
#     chuselnuk = float(input("Введіть чисельник: "))
#     znamennuk = float(input("Введіть знаменник: "))

#     result = chuselnuk / znamennuk

#     print("Результат ділення:", result)

# except ZeroDivisionError:
#     print("Помилка: ділення на нуль неможливе!")

# while True:
#     try:
#         number = int(input("Введіть ціле число: "))
#     except ValueError:
#         print("Помилка! Це не ціле число. Спробуйте ще раз.")
#     else:
#         print("Ви ввели число:", number)
#         break

# def check_password(password):
#     if len(password) <= 8:
#         raise ValueError("Пароль повинен містити не менше 8 символів.")

#     print("Пароль прийнято.")


# try:
#     user_password = input("Введіть пароль: ")
#     check_password(user_password)

# except ValueError as error:
#     print("Помилка:", error)

# while True:
#     try:
#         operation = input("operation: + - / * ")
#         a = int(input("Enter number one: "))
#         b= int(input("Enter number sekond: "))
          
#         sum = 0

#         if operation == "+":
#             sum = a + b
#         if operation == "-":
#             sum = a - b
#         if operation == "*":
#             sum = a * b
#         if operation == "/":
#             sum = a / b
        

#         print(sum)
#         cou = int(input("1 - go, 0 - stop "))

#         if cou == 1:
#             cou = int(input("1 - go, 0 - stop "))
#         else:
#             cou == 0
#             break
        
#     except:
#         print("Помилка!!!")


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#         self.is_borrowed = False

#     def borrow_book(self):
#         if self.is_borrowed:
#             print(f"Книга '{self.title}' вже зайнята.")
#         else:
#             self.is_borrowed = True
#             print(f"Книгу '{self.title}' успішно взято.")

#     def return_book(self):
#         if not self.is_borrowed:
#             print(f"Книга '{self.title}' вже повернена.")
#         else:
#             self.is_borrowed = False
#             print(f"Книгу '{self.title}' повернуто.")



# book1 = Book("Лицар Темряви", "Джохар Дудаєв", 2022)
# book2 = Book("Код Черчилля", "Стівен Джон", 2020)
# book3 = Book("Python для початківців", "Іван Петренко", 2024)


# book1.borrow_book()


# book1.borrow_book()
# book2.borrow_book()
# book3.borrow_book()

# class User:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.__balance = balance

#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"{self.name} поповнив баланс на {amount} грн")

#     def get_balance(self):
#         return self.__balance


# class PremiumUser(User):
#     def buy_item(self, price):
#         discount_price = price * 0.9  # знижка 10%

#         if self.get_balance() >= discount_price:
#             # доступ до приватного атрибута через name mangling
#             self._User__balance -= discount_price
#             print(f"{self.name} купив товар за {discount_price:.0f} грн")
#         else:
#             print("Недостатньо коштів!")


# # Тестування
# user1 = PremiumUser("Іван", 100)

# print("Баланс:", user1.get_balance())

# user1.buy_item(50)

# print("Баланс після покупки:", user1.get_balance())

# user1.buy_item(100)

# print("Кінцевий баланс:", user1.get_balance())    
    
class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def move(self):
        return f"{self.brand} їде зі швидкістю {self.speed} км/год"


class Car(Vehicle):
    pass


class ElectricCar(Vehicle):
    def __init__(self, brand, speed, battery_level):
        super().__init__(brand, speed)
        self.battery_level = battery_level

    def move(self):
        if self.battery_level <= 0:
            return f"{self.brand} не може їхати. Батарея розряджена."

        self.battery_level -= 5

        if self.battery_level < 0:
            self.battery_level = 0

        return (f"{self.brand} їде зі швидкістю "
                f"{self.speed} км/год. "
                f"Заряд: {self.battery_level}%")



def start_race(vehicles_list):
    for vehicle in vehicles_list:
        print(vehicle.move())


# Створення об'єктів
car1 = Car("BMW", 180)
car2 = Car("Audi", 200)
tesla = ElectricCar("Tesla", 220, 15)

vehicles = [car1, car2, tesla]

# Гонка
start_race(vehicles)

print()

# Ще кілька викликів для Tesla
print(tesla.move())
print(tesla.move())
print(tesla.move())