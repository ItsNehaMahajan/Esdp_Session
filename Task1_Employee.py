class Employee:
    def __init__(self,id ,name):
        self.id=0
        self.name=""
        self.salary=0
       
        
    def work(self):
        print("Employee Work")
        print("finish the within deadline")
        
        
    def getSalary(self,salary):
        self.salary=salary
        print("Employee Salary is",self.salary) 
         
    
class HRManager(Employee):

    def work(self):
        print("HRManager Work")
        print("finish the within deadline")
        
        
    def getSalary(Employee):
         salary=input("enter the salary")
         super().getSalary(salary)
         
    def AddEmployee():
        id=input("Enter Employee id")
        name=input("enter Employee name")
        print("Employee ID",id)
        print("Employee name",name)             

id=int(input("Enter the id of Employee "))     
name=input("enter the employee name")   
obj=HRManager(id,name)
obj.getSalary()
obj.AddEmployee()     