class Sphere:
    def __init__(self,radius):
        self.radius=radius
         
    def calculate(self):
        area= 4*3.14*(self.radius*self.radius)  
        volume=(4/3)*3.14*(self.radius*self.radius*self.radius)
        print("area of sphere is ",area)
        print("area of sphere is ",volume)
   
         
 
radius1=int(input("Enter the radius"))       
s=Sphere(radius1) 
s.calculate()      
        
        
        