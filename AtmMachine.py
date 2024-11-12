class Atm:
    def __init__(self):
        self.__pin=""   # '__' for privet variable ,here '__pin' is automatically convert in to '_sbi__pin'.
        self.__balance=0

        print(id(self))

        self.__menu()  #here automatically call 'menu()' method because its present in constructer.
        

    def get_pin(self):
        return self.__pin  #getter funcation for get pin :
     

    def set_pin(self,new_pin): #setter funcation for set pin :
        if type(new_pin)==str:
           self.__pin=new_pin
           print("pin changed:")
        else:
            print("Not Allowed")
    
    def __menu(self):
        user_input=input('''
                   hello,what would you like to proceed.
                   1.Enter 1 to create pin.1
                   2.Enter 2 to deposite amount.
                   3.Enter 3 to withdraw amount.
                   4.Enter 4 to check balance.        
        
        ''')
        if user_input=='1':
            self.create_pin()
        elif user_input=='2':
            self.deposite_amount()
        elif user_input=='3':
            self.withdraw_amount()
        elif user_input=='4':
            self.check_balance()
    
    def create_pin(self):
        self.__pin=input("\n choice your pin :")
        print("CREATE PIN SUCSSESFUL.")

    
    def deposite_amount(self):
        temp=input("Enter your pin .")
        if temp==self.__pin:
            amount=int(input("Enter amount for deposite ."))
            self.__balance=self.__balance+amount
            print("\n Amount deposite succesful.")
        else:
            print("invalid pin :")
            self.__deposited_amount()

    def __deposited_amount(self):
        temp=input("Please Re-Enter your pin .")
        if temp==self.__pin:
            amount=int(input("Enter amount for deposite ."))
            self.__balance=self.__balance+amount
            print("\n Amount deposite succesful.")
        else:
            print("invalid pin :")
            self.__deposited_amount()

    def withdraw_amount(self):
        temp=input("\n Enter the pin")
        if temp==self.__pin:
            amount=int(input("\n Enter the amount :"))
            if amount<self.__balance:
                self.__balance=self.__balance-amount
                print("\n amount withhdraw successful")
            else:
                print("insuficiant amount.")
        else:
            print("invalide pin .")
            
    def check_balance(self):
        temp=input("\n Enter your pin :")
        if temp==self.__pin:
            print(f"balance={self.__balance}")
        else:
            print("invalide pin :")



a=Atm()

#nothing can truely privet in python 
