# class student:
#     def __init__(self,name,age,percentage):
#         self.name=name
#         self.age=age
#         self.percentage=percentage
        
#     def showinfo(self):
#         print("Name: ",self.name)
#         print("age: ",self.age) 
#         print("percentage: ",self.percentage)
       
# name=input("enter the name")
# age=input("enter the age")
# percentage=input("enter the percentage")
# s=student(name,age,percentage)
# s.showinfo()           


class Team:
    def __init__(self,country_name,nameofplayer,age,noofmatches,battingavg,bollingavg):
        self.country_name=country_name
        self.nameofplayer=nameofplayer
        self.age=age
        self.noofmatches=noofmatches
        self.battingavg=battingavg
        self.bollingavg=bollingavg
    
    def showinfo(self):
        print("Country_Name ",self.country_name)  
        print("Name_of_player ",self.nameofplayer)
        print("Age ",self.age)
        print("No of Matches ",self.noofmatches)
        print("Batting Average ",self.battingavg)
        print("Bolling Average ",self.bollingavg)
        

    
for i in range(5): 
    countryname=input("enter the country ")
    nameofplayer=input("enter te name of player ")
    age=input("enter the age of player ")
    noofmatches=input("enter the no of matches ")
    battingavg=input("enter the batting average ")
    bollingavg=input("enter the bolling average \n\n")
    
    t=Team(countryname,nameofplayer,age,noofmatches,battingavg,bollingavg) 
    t.showinfo()       