class Person:
    moods = ("happy","tired","lazy")

    def __init__(self,name,money,mood,healthRate): #constructor
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate # property (need setter and getter)

    def sleep(self,hours):
        if hours == 7:
            self.mood=self.moods[0]
        elif hours < 7:
            self.mood= self.moods[1]
        else:
            self.mood= self.moods[2]


    def eat(self,meals): 
        if meals ==3:
            self.healthRate=100  # use setter valid
        elif meals==2:
            self.healthRate=75
        elif meals ==1:
            self.healthRate=50


    def buy(self,items):
        for i in range(items):
            self.money-=10

    @property
    def healthRate(self): # getter
        return self._healthRate
    
    @healthRate.setter
    def healthRate(self,healthRate): # setter
        if healthRate >= 0 and healthRate <= 100:
            self._healthRate = healthRate
        else:
            raise ValueError("HealthRate must be 0-100")


if __name__ == "__main__":
    p1 = Person("sami",2999,"tired",100)

    p1.buy(50)
    p1._healthRate=30
    p1.eat(3)
    print(p1.healthRate)
