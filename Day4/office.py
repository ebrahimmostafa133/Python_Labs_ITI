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
