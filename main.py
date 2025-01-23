from user import *
import os
def user_selection(customer):
    while True:
         print(f'\t\t\t\t  User Selection Tab')
         print(f'\t\t\t\t======================')
         print(f'\t\t\t  For Depositing Money Choose________________1')
         print(f'\t\t\t  For Withdrawing Money Choose_______________2')
         print(f'\t\t\t  For Checking Balance Choose________________3')
         print(f'\t\t\t  For Checking Transaction History Choose____4')
         print(f'\t\t\t  For taking Loan Choose_____________________5')
         print(f'\t\t\t  For Transfer Money Choose__________________6')
         print(f'\t\t\t  For Exit Choose____________________________7')
         ch=int(input("\t\t\t  Enter Your Choice:"))
         if ch==1:
            os.system('cls')
            amount=int(input("\t\t\tEnter deposit amount:"))
            customer.deposit_money(amount)
            char=input("\t\t\tPress Enter.....")
            os.system('cls')
         elif ch==2:
             os.system('cls')
             amount=int(input("\t\t\tEnter Withdraw amount:"))
             customer.withdraw_money(amount)
             char=input("\t\t\tPress Enter.....")
             os.system('cls')
         elif ch==3:
             os.system('cls')
             customer.get_balance()
             char=input("\t\t\tPress Enter.....")
             os.system('cls')
         elif ch==4:
             os.system('cls')
             customer.transaction_history()
             char=input("\t\t\tPress Enter.....")
             os.system('cls')
         elif ch==5:
             os.system('cls')
             amount=int(input("\t\t\tEnter Loan amount:"))
             customer.request_loan(amount)
             char=input("\t\t\tPress Enter.....")
             os.system('cls')
         elif ch==6:
              os.system('cls')
              acc_no=int(input("\t\t\tEnter Receiver Account Number:"))
              amount=int(input("\t\t\tEnter Transfer amount:"))
              customer.money_transfer(acc_no,amount)
              char=input("\t\t\tPress Enter.....")
              os.system('cls')
         elif ch==7:
             return


def user_interface():
    while True:
         print(f'\t\t\t\t   User Interface')
         print(f'\t\t\t\t======================')
         print(f'\t\t\t  For Creating Account Choose_________________________1')
         print(f'\t\t\t  If You already have an account choose_______________2')
         print(f'\t\t\t  For Exit Choose_____________________________________3')
         ch=int(input("\t\t\t  Enter Your Choice:"))
         if ch==1:
             os.system('cls')
             print(f'\t\t\tPlease give some information:')
             name=input("\t\t\tFull Name:")
             email=input("\t\t\tEmail Address:")
             address=input("\t\t\tAddress:")
             account_type=input("\t\t\tAccount Type(Savings/Current):")
             admin.add_user(name,email,address,account_type)
             char=input("\t\t\tPress Enter.....")
             os.system('cls')
         elif ch==2:
              os.system('cls')
              acc_no=int(input("\t\t\tEnter Your Account Number:"))
              flag=False
              for user in users:
                 if user.account_no==acc_no:
                     os.system('cls')
                     user_selection(user)
                     flag=True
              if flag==False:
                 print(f'\t\t\tAccount does not exist!')
              os.system('cls')
                
         elif ch==3:
             return
        

                   
         
                     
             
             
             
             


admin=Admin()
# bank=Bank()
while True:
    print(f'\t\t\t\tBank Management System')
    print(f'\t\t\t\t======================')
    print(f'\t\t\t  For User Interface Choose_____1')
    print(f'\t\t\t  For Admin Interface Choose____2')
    print(f'\t\t\t  For Exit Choose_______________3')
    choice=int(input("\t\t\t  Enter Your Choice:"))
    if choice==1:
        os.system('cls')
        user_interface()
        os.system('cls')

    




