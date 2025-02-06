# class Human:
#     def __init__(self,name = "Human"):
#         self.name = name
# class Auto:
#     def __init__(self, brand):
#         self.brand = brand
#         self.passenger = []
#     def add_passenger(self, *args):
#         for passenger in args:
#             self.passenger.append(args)
#     def print_passenger_names(self):
#         if self.passenger != []:
#             print("Names of {self.brand} passenger: ")
#             for passenger in self.passenger:
#                 print(passenger.name)
#         else:
#             print("There are no passenger in {self.brand} ")
# nick = Human("Nick")
# kate = Human("Kate")
# car = Auto("Porsche")
# car.add_passenger(nick, kate)
# car.print_passenger_names()


import random


class Human:
    def __init__(self, name ="Human", job = None, home = None, car = None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home= House()
    def get_car(self):
        self.car = Auto(brands_of_car)
    def get_job(self):
        if self.car.drive():
            ...
        else:
            self.to_repair()
            return
        self.job = job(job_list)
    def eat(self):
        if self.food<=0
            self

    def work(self):

    def shopping(self, manage):

    def chill(self):

    def clean_home(self):

    def to_repair(self):


    def days_indexes(self, day):

    def is_alive(self):

    def live(self,day):

class Auto:
    def __init__(self, brand_list):
        self.band = random.choise(list (brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["strenght"]

    def drive(self):
        if self.strenght > 0 and  self.fuel>=self.consumption:
            self.fuel-=self.consumption
            self.strenght -=1
            return True
        else:
            print("The car cannot move")
            return False
class House:
    def __init__(self):
        self.mess = 0
        self.food = 0


brands_of_car = {
    "BMW":{"fuel": 100, "strength":100, "consumption": 6 },
    "Porshe": {"fuel": 150, "strength": 40, "consumption": 10},
    "Pagani": {"fuel": 100, "strength": 50, "consumption": 8},
    "Ferrari": {"fuel": 150, "strength": 200, "consumption": 14},
}
job_list={
    "Java developer": {"salaray":50, "gladness": 10},
    "Python developer": {"salaray": 40, "gladness": 3},
    "C++ developer": {"salaray": 45, "gladness": 25},
    "Rust developer": {"salaray": 70, "gladness": 1}
}


class job:
    def __init__(self, job_list):
        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]["salary"]
        self.gladness_less = job-list[self.job]["glandness_less"]