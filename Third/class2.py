
from class1 import  Humen

class Engineer(Humen):
    pass
   
class Accountent(Humen):
    pass

class Devloper(Humen):
    pass


class MechnicalEngneer(Engineer):
    def do_mechnica(self):
        print(f"{self.name} is do mechnical work  And age is {self.age}")

class Electrical_Engneer(Engineer):
    def do_electrical(self):
        print(f"{self.name} is do electrical work  And age is {self.age}")

class CivilEngneer(Engineer):
    def do_civil(self):
        print(f"{self.name} is do civil work  And age is {self.age}")

class ChatertedAccountent(Accountent):
    def work(self):
        print(f"{self.name} is do work  And age is {self.age}")

class FrontendDevloper(Devloper):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self):
        print(f"{self.name} is do front work  And age is {self.age}")

class BackendDevloper(Devloper):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self):
        print(f"{self.name} is do backend work  And age is {self.age}")


class FullstackDevloper(Devloper):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self):
        print(f"{self.name} is do fullstack work  And age is {self.age}")


class ProductManeger(FullstackDevloper,BackendDevloper):
    def __init__(self, name, age):
        super().__init__(name, age)

    def work(self):
        print(f"{self.name} is do product management work And age is {self.age}")




Engineer1=Engineer("vyom",20)
Engineer1.eat()

Mechnical_engneer1=MechnicalEngneer("Neel",17)
Mechnical_engneer1.play()
Mechnical_engneer1.do_mechnica()

electrical_engneer1=Electrical_Engneer("Mohan",28)
electrical_engneer1.play()
electrical_engneer1.do_electrical()

civillengneer1=CivilEngneer("Shubham",37)
civillengneer1.play()
civillengneer1.docivil()

Accountent1=Accountent("vyom",20)
Accountent1.eat()

ChatertedAccountent1=ChatertedAccountent("Harsh",27)
ChatertedAccountent1.play()
ChatertedAccountent1.work()

Devloper1=Devloper("vyom",20)

FrontendDevloper1=FrontendDevloper("anji",24)
FrontendDevloper1.work()

BackendDevloper1=BackendDevloper("devu",22)
BackendDevloper1.work()

FullstackDevloper1=FullstackDevloper("Harsh",27)
FullstackDevloper1.work()

Product_Maneger1=ProductManeger("Harshita",27)
Product_Maneger1.work()