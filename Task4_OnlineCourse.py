# from abc import ABC, abstractmethod
# class Course(ABC):
    
#     def __init__(self,title,duration,price,programming_language,instructor):
#         self.title=""
#         self.duration=0
#         self.price=0
        
#     def Enroll(self): 
          
           
#       @abstractmethod
#       def Getdetails(self):
    
    
# class Programming_Course(Course):
#     def __init__(self,programming_language,instructor):
#         title=super.title
#         duration=super.duration
#         price=super.price
        
#         self.programming_language=programming_language
#         self.instructor=instructor
    
#     def Getdetails(self): 
#         self.title=input("Enter the Title")
#         print(self.title)
#         self.duration=int(input("Enter the Duration"))
#         print(self.duration)
#         self.price=int(input("Enter the Price "))
#         print(self.price) 
        
#         print("Title of the Course",title)    
#         print("Title of the Course",duration)    
#         print("Title of the Course",price)    
        
        
# p=Programming_Course() 
# p.Enroll()      
# p.Getdetails()        