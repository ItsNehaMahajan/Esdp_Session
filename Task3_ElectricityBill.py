class Electricity_Bill():
    def __init__(self,name,units):
        self.name=name
        self.units=units
        
    def showinfo(self):
        print("name is",self.name)
        if (units<=30 ):
          print(" Your unit is",self.units)
          print("1.50/-per unit")
          amount=units*1.50
          print("Total amount of your bill is\n ",amount)
          
        elif (units>=31 and units<=200):
          print(" Your unit is",self.units)
          print("3.00/-per unit")
          amount=units*3.00
          print("your amount is\n",amount)
          if( amount>=500.00 ):
            amount1=15%amount
            print("Total amount of your bill is \n",amount1)
          
            
        elif (units>=300) :
          print(" Your unit is",self.units)
          print("4.25/-per unit")
          amount=units*4.25
          print("your amount is\n",amount)
          if( amount>=500.00 ):
            amount1=15%amount
            print("Total amount of your bill is \n",amount1)

for i in range(5):        
 name=input("\nEnter the name\n")
 units=int(input("Enter the units\n"))        
 bill=Electricity_Bill(name,units)
 bill.showinfo()