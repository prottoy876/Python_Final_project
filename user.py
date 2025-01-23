from abc import ABC
import random
bankrupt=False
loan_activation=True
users=[]
loans=[]          
class User(ABC):
    acount_count=202500
    def __init__(self,name,email,address,account_type):
        self.name=name
        self.email=email
        self.address=address
        self.account_type=account_type
        self.balance=0
        self.account_no=User.acount_count
        User.acount_count+=1
        self.current_balance=0
        self.transactions=[]
        self.loan_count=0
    def deposit_money(self,amount):
        self.current_balance+=amount
        self.transactions.append(f'Deposited: {amount}')
        print(f"\t\t\t{amount} deposited Successfully!")
        print(f'\t\t\tCurrent Balance is: {self.current_balance}')
    
    def withdraw_money(self,amount):
        if bankrupt==False:
            if amount>self.current_balance:
                  print(f'Withdrawal amount exceeded!')
            else:
                 self.current_balance-=amount
                 self.transactions.append(f'Withdrawn: {amount}')
                 print(f"\t\t\t{amount} Withdrawn Successfully!")
                 print(f'\t\t\tCurrent Balance is: {self.current_balance}')
        else:
            print(f'\t\t\tThe Bank is Bankrupt!')

    def get_balance(self):
        print(f'\t\t\tCurrent Balance: {self.current_balance}')
    
    def transaction_history(self):
        print(f'\t\t\tTransaction History of {self.account_no} account number:')
        for transaction in self.transactions:
            print(f'\t\t\t{transaction}')
    def request_loan(self,amount):
        if loan_activation==True:
             if self.loan_count>=2:
                 print(f'\t\t\tLoan Limit Exceeded!')
             else:
                 self.current_balance+=amount
                 self.loan_count+=1
                 self.transactions.append(f'Loan token: {amount}')
                 print(f'\t\t\tLoan amount {amount} accepted!')
                 loans.append((self.account_no,amount))
                 print(f'\t\t\tCurrent Balance: {self.current_balance}')
        else:
            print(f'\t\t\tLoan sanction is currently off.Please Try again later!')
    
    def money_transfer(self,recipient_acc_no,amount):
        if bankrupt==False:
            if amount>self.current_balance:
                print(f'\t\t\tInsufficient balance!')
            else:
                for user in users:
                    if recipient_acc_no==user.account_no:
                          user.current_balance+=amount
                          self.current_balance-=amount
                          self.transactions.append(f'Money Transfer: {amount}')
                          user.transactions.append(f'Money Received: {amount}')
                          print(f'\t\t\tTransaction amount:{amount}.Transaction Successful!')
                          print(f'\t\t\tCurrent Balance: {self.current_balance}')
                          return
                print(f'\t\t\tRecipient does not exist!')


class Admin:
    def __init__(self):
       pass
    
    def add_user(self,full_name,email,address,account_type):
        user=User(full_name,email,address,account_type)
        users.append(user)
        print(f'\t\t\tUser Name:{full_name} registered successfully.\n\t\t\tAccount number: {user.account_no}')
        return user
    
    def remove_user(self,account_number):
        flag=False
        for user in users:
            if account_number==user.account_no:
                users.remove(user)
                flag=True
                print(f'User {user.name} removed!')
        if flag==False:
            print(f'User does not exist!')

    def view_user_list(self):
        print(f'All Users:')
        for user in users:
            print(f'User Name: {user.name},Account Number: {user.account_no},Balance: {user.current_balance}, Account Type: {user.account_type}')
    def total_available_balance(self):
        total=0
        for user in users:
            total+=user.current_balance
        print(f'Total Available balance in the Bank: {total}')
    def total_loan_amount(self):
        total=0
        for loan in loans:
            total+=loan[1]
        print(f'Total Loan Amount: {total}')
    def set_bankrupt(self,toggle):
        global bankrupt
        bankrupt=toggle
    def set_loan_activation(self,toggle):
        global loan_activation
        loan_activation=toggle
    @property
    def get_bankrupt(self):
        return bankrupt
    @property
    def get_loan_activation(self):
        return loan_activation

