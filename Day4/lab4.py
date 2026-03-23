

 # Write a program that choose a random website name from list and open it in your browser 
import random
import webbrowser

websites = [ "https://www.youtube.com", "https://www.stackoverflow.com", "https://www.reddit.com"]

selected_website = random.choice(websites)
webbrowser.open(selected_website)


# 1- Create the following classes:
# - Person Class:
# - attributes (name, money, mood, healthRate).
# - methods (sleep, eat, buy).

# - sleep (hours): - Method in Person Class (7 hours  happy, <7 hours  tired, >7 hours  Lazy)
# - eat (meals):- Method in Person Class (3 meals  100% hth , 2 meals 75% , 1 meal  50%)
# - buy (items):- Method in Person Class (1 item  decrease money 10 L.E)

# - healthRate Property: must be between 0 to 100.
# - There is moods class variable which is tuple of happy, tired and lazy


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
    

p1 = Person("sami",2999,"tired",100)

p1.buy(50)
p1._healthRate=30
p1.eat(3)
print(p1.healthRate)



# 2. Employee Class (is a Person):
# - attributes (id , car, email, salary, distanceToWork)
# - methods (work, drive, refuel, send_mail)

# - work (hours): - Method in Employee Class (8 hourshappy, >8 hours  tired,<8 hours  Lazy)
# - drive (distance): Method in Employee Class (Give the order to run method and give it distance and velocity).
# - refuel (gasAmount = 100): Method in Employee Class (add gasAmount to fuelRate).
# - send_mail(to, subject, msg, receiver_name): Create Email File like the next page specification (Email Composer)

# - salary Property: must be 1000 or more.
# - email Property: must be valid.

import re,json


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








# 3. Office Class:
# - attributes (name, employees)
# -methods (get_all_employees, get_employee, hire, fire, calculate_lateness,deduct, reward)

# - get_all_employees (): Method in Office Class (Return a list of the current Employees)
# - get_employee (empId): Method in Office Class (Return the Employees of given id)
# - hire (Employee): Method in Office Class (Hire the given Employee)
# - fire (empId): Method in Office Class (Fire Employee with the given id)

# - deduct (empId, deduction): Method in Office Class (Deduce Money from salary from Employee)
# - reward (empId, reward): Method in Office Class (add Money to salary from Employee)

# - calculate_lateness (targetHour , moveHour, distance, velocity): Static Method in Office Class (Calculate If employee is late or not )
# - check_lateness (empId, moveHour): Method in Office Class (Check if employee is late or not and deduce if he is late -10 and reward if he is not late +10)
# - check_lateness calls calculate_lateness + deduct/reward accordingly
# - change_emps_num (num) class method which modify the number of Employees in all offices.

# - employeesNum class variable which declared the number of Employees in all offices.


class Office:
    employeesNum =0

    def __init__(self,name,employees=None):
        self.name=name
        if employees is None:
            self.employees=[]
        else: 
            self.employees=employees

    def get_all_employees(self):
        return self.employees
    
    def get_employee(self,emp_id):
        for emp in self.employees:
            if emp.id == emp_id:
                return emp

    def hire(self,employee): #type of emp
        self.employees.append(employee)
        Office.employeesNum+=1

    def fire(self,emp_id):
        emp = self.get_employee(emp_id)
        if emp is not None:
            self.employees.remove(emp)
            Office.employeesNum-=1
            return

    def deduct(self, emp_id, deduction):
        emp = self.get_employee(emp_id)
        if emp is None:
            print("Employee not found")
        elif emp.salary - deduction >= 1000:
            emp.salary -= deduction
        else:
            print("Cannot deduct, alary would drop below 1000")

    
    def reward(self,emp_id,reward):
        emp=self.get_employee(emp_id)
        if emp is not None:
            emp.salary+=reward
        else:
            print("Employee not found")


    @staticmethod
    def calculate_lateness( moveHour, velocity, distance, targetHour=9) :
        arrival = moveHour + (distance/velocity)
        if arrival > targetHour:
            return True
        else: 
            return False
        
    def check_lateness(self,emp_id,moveHour):
        emp = self.get_employee(emp_id)
        if emp:
            late_status = Office.calculate_lateness(moveHour,emp.car.velocity,emp.distanceToWork )
            if late_status:
                self.deduct(emp_id,10)
            else: 
                self.reward(emp_id,10)

    @classmethod
    def change_emps_num(cls,num):
        cls.employeesNum = num


    def to_dict(self):
        return {
            "name": self.name,
            "employeesNum": self.employeesNum,
            "employees": [emp.to_dict() for emp in self.employees]
        }





# 4. Car Class:
# - attributes (name, fuelRate, velocity)
# -methods (run, stop)

# - run (velocity, distance): Method in Car Class (When invoked it decreases the fuelRate and change the velocity to
# the input parameter of velocity . 
# And it invoke the stop method and give it the remain distance
# (It is possible to stop before arrive the destination because fuelRate become 0).

# - stop ():
# - Method in Car Class (Stop make the velocity changed to 0 and print notification with the
# remain distance or that you arrive the destintation )

# - Velocity Property: must be between 0 to 200.
# - Fuel Rate Property: must be between 0 to 100.


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





# Write a program that generate a file that contains a structured email message


import yagmail

def send_mail( sender_email,receiver_email, subject, msg, receiver_name):
    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", receiver_email):
        raise ValueError("Invalid receiver email!")

    body = (
        f"From: {sender_email}\n"
        f"To: {receiver_email}\n"

        f"Hi, {receiver_name}\n"
        f"{msg}\n"
        f"Thanks\n"
    )

    try:
        yag = yagmail.SMTP(sender_email, "pyrv ocdy gqmd pqku")
        yag.send(to=receiver_email, subject=subject, contents=body)
        print("Email sent")
    except Exception as e:
        print(f"Failed {e}")


send_mail("mohamed.abdelhaqgp@gmail.com","mohamed.abdelhaq99@gmail.com", "testtSubject","Hello from the other siiiide", 'MO')