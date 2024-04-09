

class Humen:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def eat(self):
        print(f"{self.name} is eatting And age is {self.age}")

    def drive(self):
        print(f"{self.name} is drive And age is {self.age}")

    def play(self):
        print(f"{self.name} is play And age is {self.age}")
        

first=Humen("Darshi",22)
first.eat()
first.drive()
first.play()


second=Humen("Dhyan",18)
second.eat()
second.drive()
second.play()


third=Humen("Ravi",27)
third.eat()
third.drive()
third.play()

fourth=Humen("Hetu",24)
fourth.eat()
fourth.drive()
fourth.play()
