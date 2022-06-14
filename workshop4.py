class User:
    def __init__(self,name,pin,password):
        self.name = name
        self.pin = pin
        self.password = password
    
    def change_name(self,name):
        self.name = name
        
    def change_pin(self,pin):
        self.pin = pin

    def change_password(self,password):
        self.password = password

class BankUser(User):
    def __init__(self,name,pin,password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self):  ### WHY DOESNT IT PRINT BALANCE
        print(self.name , 'has an account balance of:',self.balance)
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        
    def withdraw(self,amount):
        if self.balance - amount > 0:
            self.balance = self.balance - amount
        else:
            print("You can not withdraw more than your balance.")
            print("Current balance is",self.balance)

    def transfer_money(self,amount,user):
        print('Authorization Required to transfer money')
        inputted_pin = input(("Enter your pin: "))
        if int(inputted_pin) == self.pin:
            self.balance = self.balance - amount
            user.balance = user.balance + amount
            print('Transfer Authorized')
            print('Transferring',amount,'to',user.name)
            return True
        else:
            print('Invalid Pin. Transaction canceled')
            return False

    def request_money(self,amount,user):
        inputted_pin = input(("Authorization is required to request money. Please enter your pin: "))
        if int(inputted_pin) == self.pin:
            input_password = input("Enter Password")
            if input_password == self.password:
                self.balance = self.balance + amount
                user.balance = user.balance - amount
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
user2.deposit(5000)
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

