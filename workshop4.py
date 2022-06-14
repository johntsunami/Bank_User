class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self,name):
        if 2 < len(name)< 10: 
            self.name = name
        else:
            print('Name needs to be between 2-10 characters')
            return False
        
    def change_pin(self,new_pin):
        if len(str(new_pin)) == 4:
            if new_pin == self.pin:
                print("New PIN cannot be the same as previous PIN number.")
            else:
                self.pin = new_pin
        else:
            print("Pin Must be 4 characters long")


    def change_password(self,password):
        if 4 < len(password)< 12: 
            if ' ' in password:
                print('No spaces allowed in password.')
            else:
                self.password = password
        else:
            print('Password needs to be between 4-12 characters')
         

class BankUser(User):
    def __init__(self,name,pin,password):
        super().__init__(name, pin, password)
        # self.balance = float(0)
        self.balance = 0
        on_hold = False

    def show_balance(self):  
        print(self.name , 'has an account balance of:',format(self.balance, '.2f'))  #formats balance to string with two decimal spaces
                                                        
    def deposit(self,amount):
        if amount < 0 :                            
            print("Error: Amount must be over 0 ")
            return False
        self.balance = self.balance + amount
        
    def withdraw(self,amount):
        if amount < 0 :                      
            print("Error: Amount must be over 0 ")
            return False
        if self.balance - amount > 0:
            self.balance = self.balance - amount
        else:
            print("You can not withdraw more than your balance.")
            print("Current balance is",format(self.balance, '.2f'))  #formats balance to string with two decimal places

    def transfer_money(self,amount,user):
        if amount < 0 :                         
            print("Error: Amount must be over 0 ")
            return False
        
        if amount > self.balance:
            print("You cannot transfer more money than you have in your balance.")
            return False

        print('Authorization Required to transfer money')
        inputted_pin = input(("Enter your pin: "))
        if int(inputted_pin) == self.pin:
            self.balance = self.balance - amount
            user.balance = user.balance + amount
            print('Transfer Authorized')
            print('Transferring',format(amount, '.2f'),'to',user.name)  #formats the amount to to hundreds place
            return True
        else:
            print('Invalid Pin. Transaction canceled')
            return False

    def request_money(self,amount,user):
        if amount < 0 :      
            print("Error: Amount must be over 0 ")
            return False

        if amount > user.balance:
            print("You cannot transfer more money than they have in their balance.")
            return False

        inputted_pin = input(("Authorization is required to request money. Please enter your pin: "))
        if int(inputted_pin) == self.pin:
            input_password = input("Enter Password")
            if input_password == self.password:
                self.balance = self.balance + amount
                user.balance = user.balance - amount
                print("Requested:",format(amount, '.2f'),'from',user.name)
                return True
            else:
                print('Invalid password.  Transaction canceled')
                return False
        else:
            print('Invalid Pin. Transaction canceled')
            return False


    #### Driver Code for Task 5 ###
user1 = BankUser('bob', 1234, 'password')
user2 = BankUser('john', 4260, 'winwin')
user1.show_balance()
 

user2.deposit(5000.533)
user2.show_balance()
user1.show_balance()
user2.transfer_money(500,user1)
user1.show_balance()
user2.show_balance()
user2.request_money(100, user1)
user1.show_balance()
user2.show_balance()





#         ### Driver code for task 3 ###
# bank1 = BankUser('Bob',1234,'password')
# bank1.deposit(100)
# # bank1.withdraw(50)
# bank1.show_balance()
 


        ### Driver Code for Task 3 ###
# bank1 = BankUser('Bob','1234','password')
# print(bank1.name,bank1.pin,bank1.password,bank1.balance)


        ### Driver Code for Task 2 ###
# user1 = User('bob',1234,'password')
# print(user1.name,user1.pin,user1.password)
# user1.change_pin('Billy')
# print(user1.name,user1.pin,user1.password)


            ### Driver Code for Task 1 ###
# user1 = User('bob',1234,'password')
# print(user1.name,user1.pin,user1.password)

