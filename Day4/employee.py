import re
import json
from person import Person


class Employee(Person):
    def __init__(self,name,money,mood,healthRate,id,car,email,salary,distanceToWork):
        super().__init__(name,money,mood,healthRate)
        self.id = id
        self.car = car # this is car obj (dependency injection)
        self.email= email # use setter for valid., not self._email
        self.salary= salary
        self.distanceToWork= distanceToWork

    def work(self,hours):
        if hours == 8:
            self.mood= self.moods[0] # emp. inherits moods from parent
        elif hours < 8:
            self.mood= self.moods[2]
        else:
            self.mood= self.moods[1]


    def drive(self,velocity=60):
        self.car.velocity=velocity
        self.car.run(self.car.velocity,self.distanceToWork)
        

    def refuel(self,gasAmount=100):
        self.car.fuelRate = min(100,self.car.fuelRate + gasAmount)
        

    def send_mail(self,to,subject,msg,receiver_name):
        to=Employee.valid_email(to)
        with open ('email.txt','w') as file:
            file.write(
f"From: {self.email}\n"
f"To: {to}\n"
f"\n"
f"Hi, {receiver_name}\n"
f"{msg}\n"
f"Thanks\n"
f"Best Regards, {self.name}"
        )


    @staticmethod
    def valid_email(email):
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        if re.match(pattern, email):
            return email
        else:
            raise ValueError("Enter vaild email")

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,email):
        self._email=Employee.valid_email(email)


    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self,salary):
        if salary >= 1000:
            self._salary=salary
        else:
            raise ValueError("Salary must be 1000 or more")
        

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "salary": self.salary,
            "distanceToWork": self.distanceToWork,
            "car": self.car.to_dict()    
        }
    
    def save_to_json(self):
        with open(self.name + ".json", "w") as file:
            json.dump(self.to_dict(), file, indent=4)
        print(f"Saved to {self.name}.json")
