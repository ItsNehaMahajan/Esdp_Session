# class Time:
#     def __init__(self,time):
#         self.time=time
    
#     def dis_time(self):
#          print("Time is ",self.time) 
           
           
# time=input("enter the time")
# t=Time(time)  
# t.dis_time()
         
         
# class Date:
#     def __init__(self,date):
#         self.date=date
    
#     def dis_date(self):
#          print("Time is ",self.date) 
           
           
# date=input("enter the time")
# t=Date(date)  
# t.dis_date()         


# class Person:
#     def __init__(self,name,mob_no):
#         self.name=name
#         self.mob_no=mob_no
    
#     def dis_info(self):
#          print("Name is ",self.name)
#          print("mMob_no  is ",self.mob_no) 
           
           
# name=input("enter the name")
# mob_no=input("enter the mob_no")
# t=Person(name,mob_no)  
# t.dis_info()    

# class Student:
#     def __init__(self,name,mob_no):
#         self.name=name
#         self.mob_no=mob_no
    
#     def dis_info(self):
#          print("Name is ",self.name)
#          print("mMob_no  is ",self.mob_no) 
           
           
# name=input("enter the name")
# mob_no=input("enter the mob_no")
# t=Student(name,mob_no)  
# t.dis_info()    


# class Fan:
#     def __init__(self,company):
#         self.company=company
        
#     def dis_info(self):
#          print(" Company Name is ",self.company)
           
           
# company=input("enter the name of company")
# t=Fan(company)  
# t.dis_info()    

# class Point:
#     def __init__(self,no):
#         self.no=no
        
    
#     def dis_info(self):
#          print("Point no is ",self.no)
           
           
# no=input("enter the no of points")
# t=Point(no)  
# t.dis_info()    
 
 
# class Box:
#     def __init__(self,size):
#         self.size=size
        
    
#     def dis_info(self):
#          print("Box size  is ",self.size)
           
           
# size=input("enter the size of box (small/big)")
# t=Box(size)   
# t.dis_info()    
 
# class MyPython(object):
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#         self.d=40
        
#     def func(self):
#         del self.d
          
# m=MyPython()
# print(m.__dict__)
# m.fun()
# print(m.__dict__)
# del m.c
# print(m.__dict__)