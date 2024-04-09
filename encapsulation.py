class Human:
    def __init__(self,eyes,nose,hand,lag,ears,mouth):
        self.eyes=eyes
        self.nose=nose
        self.hand=hand
        self.lag=lag
        self.ears=ears
        self.mouth=mouth
        
    def __addeyes(self):
        print(f"{self.eyes} eyes are added ")

    def __addnose(self):
        print(f"{self.nose} nose are added ")

    def __addhand(self):
        print(f"{self.hand} hand are added ")

    def __addlag(self):
        print(f"{self.lag} lag are added ")

    def __addears(self):
        print(f"{self.ears} ears are added ")

    def __addmouth(self):
        print(f"{self.mouth} mouth are added ")

    def makehuman(self):
        self.__addeyes()
        self.__addnose()
        self.__addhand()
        self.__addlag()
        self.__addears()
        self.__addmouth()

human1=Human(eye=2,nose=3,hand=1,lag=3,ears=4,mouth=3)
human1.makehuman()


