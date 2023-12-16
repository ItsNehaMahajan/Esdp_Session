class BankAccount:
    
    def __init__(self,Name_of_depositor,account_number,type_of_account,balance):
        self .Name_of_depositor=Name_of_depositor
        self.account_number=account_number
        self.type_of_account=type_of_account
        self.balance=balance
        
        
    def values(self):
           depositor=self.Name_of_depositor
           print("Name of the depositor ", depositor)
           accountno=self.account_number
           print("Account number ", accountno)
           account_type=self.type_of_account
           print("Account Type ",  account_type)
           balance=self.balance
           print("Balance ", balance)
           
    def deposit(self):
         res=int(input("enter the deposit amount"))
         self.balance=self.balance+res
         print("Balance after deposit",self.balance)
        
        
    def withdraw(self):
         res=int(input("enter the withdraw amount"))
         self.balance=self.balance-res
         print("Balance after withdraw\n",self.balance)
        
    def display(self):
        
        print("Name of the depositor", self.Name_of_depositor)
        print("Current Balance",self.balance)
        

class SavingsAccount(BankAccount):
    def withdraw(self):
        if balance<=1000:
            print("You have Insufficient Balance, Sorry! you cannot withdraw money ")
        else:    
          super.withdraw()
    
    
    
name=input("Enter the name of Depositor")
accountno=int(input("Enter the Account No"))
accounttype=input("Enter the Account Type")
balance=int(input("Enter the Balance"))
b=BankAccount(name,accountno,accounttype,balance)
   
print("\n***********************Menu***********************")
print("\n1: Print Account Information")   
print("2: Deposit")   
print("3: Withdraw")   
print("4: Name & balance\n")   
while(True):
    ch=int(input("\nEnter the Choice"))
    if ch==1:
        b.values()
    elif ch==2:
        b.deposit()
    elif ch==3:
        s=SavingsAccount(name,accountno,accounttype,balance)
        b.withdraw()
    elif ch==4:
        b.display()        
       
     