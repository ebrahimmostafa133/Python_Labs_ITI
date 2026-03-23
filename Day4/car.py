class Car:
    def __init__(self,fuelRate,velocity,name='fiat 128'):
        self.name=name
        self.fuelRate=fuelRate
        self.velocity=velocity

    @property
    def fuelRate(self):
        return self._fuelRate
    
    @fuelRate.setter
    def fuelRate(self,fuelRate):
        if fuelRate>=0 and fuelRate <=100:
            self._fuelRate=fuelRate
        else:
            raise ValueError("Fuel Rate Value 0-100")
        
    @property
    def velocity(self):
        return self._velocity
    
    @velocity.setter
    def velocity(self,velocity):
        if velocity>=0 and velocity<=200:
            self._velocity=velocity
        else:
            raise ValueError("Velocity value 0-200")
    

    def run(self,velocity,distance):
        self.velocity=velocity
        travelled=0
        while travelled < distance:
            cycle = min(10,distance-travelled) 
            travelled+= cycle
            self.fuelRate= max(0, self.fuelRate- cycle ) # to prevent crashes when if fuel dec than zero 
            if self.fuelRate <=0:
                self.stop(distance-travelled)
                return 
        
        self.stop(0)
            

    def stop(self,distance):
        self.velocity=0 # or self.velocity=0 but will fail cond.
        if distance ==0:
            print("You've arrived")
        else:
            print(f"You stoppend midway with Remaining distance {distance}")


    def to_dict(self):
        return {
            "name": self.name,
            "fuelRate": self.fuelRate,
            "velocity": self.velocity
        }
