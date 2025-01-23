from user import *
# admin = Admin()
# customer1 = admin.add_user("Alice Smith", "alice@example.com", "123 Elm Street", "Savings")
# customer2 = admin.add_user("Bob Johnson", "bob@example.com", "456 Maple Avenue", "Current")
# # print(admin.get_bankrupt)
# customer1.deposit_money(1000)
# # admin.set_bankrupt(True)
# customer1.withdraw_money(500)
# customer1.transaction_history()

# # print(admin.get_bankrupt())
# admin.view_user_list()
# customer1.money_transfer(202501, 200)
# customer1.transaction_history()
# customer2.transaction_history()
# # customer2.get_balance()
# # admin.set_loan_activation()
# # admin.set_loan_activation(False)
# customer1.request_loan(5000)
# customer1.request_loan(5000)
# customer1.request_loan(5000)
# customer2.request_loan(5000)

# admin.view_user_list()
# admin.total_available_balance()
# admin.total_loan_amount()
# admin.remove_user(202501)
# # # admin.view_user_list()
# # # admin.list_all_users()
# # # admin.calculate_total_balance()
# # # admin.toggle_loan_availability()
def user_interface():
    while True:
         print(f'\t\t\t\t   User Interface')
         print(f'\t\t\t\t======================')
         print(f'\t\t\t  For Creating Account Choose________________1')
         print(f'\t\t\t  For Depositing Money Choose________________2')
         print(f'\t\t\t  For Withdrawing Money Choose_______________3')
         print(f'\t\t\t  For Checking Balance Choose________________4')
         print(f'\t\t\t  For Checking Transaction History Choose____5')
         print(f'\t\t\t  For taking Loan Choose_____________________6')
         print(f'\t\t\t  For taking Loan Choose_____________________6')
         print(f'\t\t\t  For Transfer Money Choose__________________7')
         print(f'\t\t\t  For Exit Choose____________________________8')
         ch=int(input("\t\t\t  Enter Your Choice:"))
         
         if ch==1:
             print(f'\t\t\tPlease give some information:')
             name=input("\t\t\tFull Name:")
             email=input("\t\t\tEmail Address:")
             address=input("\t\t\tAddress:")
             account_type=input("\t\t\tAccount Type(Savings/Current):")
             customer=admin.add_user(name,email,address,account_type)
         elif ch==2:
            amount=int(input("\t\t\tEnter deposit amount:"))
            customer.deposit_money(amount)
             
             


admin=Admin()
customer=None
while True:
    print(f'\t\t\t\tBank Management System')
    print(f'\t\t\t\t======================')
    print(f'\t\t\t  For User Interface Choose_____1')
    print(f'\t\t\t  For Admin Interface Choose____2')
    print(f'\t\t\t  For Exit Choose_______________3')
    choice=int(input("\t\t\t  Enter Your Choice:"))
    if choice==1:
        user_interface()




