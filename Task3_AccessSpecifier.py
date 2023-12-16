# class Example:
#     def __init__(self):
#         self.public_variable="I am Public"
        
#     def public_method(self):
#         return "I am Public method"
    
# obj=Example()
# print(obj.public_variable)        
# print(obj.public_method())        


# class Example:
#     def __init__(self):
#         self.__private_variable="I am Private"
        
#     def __private_method(self):
#         return "I am Private method"
    
# obj=Example()
# print(obj._Example__private_variable)        
# print(obj._Example__private_method())        

# class Example:
#     def __init__(self):
#         self.__protected_variable="I am protected"
        
#     def _protected_method(self):
#         return "I am protected method"
    
# obj=Example()
# print(obj._protected_variable)        
# print(obj._protected_method())     




# *********************** abstract Class *****************

from abc import ABC, abstractmethod
class Rcpit(ABC):
    @abstractmethod
    def student_details(self):
        pass
    
    @abstractmethod
    def student_assignment(self):
        pass
    
    @abstractmethod
    def student_marks(self):
        pass
    
class comp_c(Rcpit):
    def student_details(self):
        return "I will try to return the student details of computer c" 
    
    def student_assignment(self):
        return "I will try to return the assignment of computer c"
       
    def student_marks(self):
        return "I will try to return the marks of computer c"
       
    
    
cc=comp_c()   
print(cc.student_details())
print(cc.student_assignment())
print(cc.student_marks()) 

    