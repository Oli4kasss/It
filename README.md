#1 завдання
# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#     def get_info(self):
#         return (f"{self.make} {self.model} {self.year}")
#
# car = Car("German","Porshe", 2021)
# print(car.get_info())
#
#
# #2 завдання
# class Employee:
#     def __init__(self,name, salary):
#         self.name = name
#         self.salary = salary
#
# class Department:
#     def __init__(self):
#         self.employees = []
#
#     def add(self, employees):
#         self.employees.append(employees)
#
#     def total_salary(self):
#         return sum(e.salary for e in self.employees)
#
# d = Department()
# d.add(Employee("Максим", 4000))
# d.add(Employee("Володя", 3500))
# print(d.total_salary())
#
#
# #3 завдання
# class Device:
#     def turn_on(self):
#         print("Увімкнено")
#     def turn_off(self):
#         print("Вимкненно")
#
# class Laptop (Device):
#     def download(self):
#         print("Ноутбук завантажує програму")
# class Phone(Device):
#     def charge(self):
#         print("Телефон заряджається")
#
# laptop = Laptop()
# laptop.turn_on()
# laptop.download()
#
# phone = Phone()
# phone.turn_on()
# phone.charge()
#

# #4 завдання
# import random
# def gen():
#         yield random.letters("abcdefghijklmnopqrstuvyzwx")
#      while True:
# g = gen()
# for i in range(4):
#  print(next(g))

