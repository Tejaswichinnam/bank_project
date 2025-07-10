print("-----".center(80,"*"))
print("! Welcome to BHARATH BANK !".center(80))
print("-----".center(80,"*"))
#predefining some customers,pins&balances
cus_names=["suresh","tejaswi","khaathvik","sonysree"]
cus_pins=["1807","2209","1709","2101"]
cus_balance=[25000,20000,5000,8000]
#initially set to "0"..to use later 
deposit_amount=0
withdraw_amount=0
balance=0
#counter_1,counter_2 are used to track number of customers
counter_1=1
counter_2= len(cus_names)
#i is used to store the number of new customers currently
i=0
#using a string to display the options to customer
o='''
  1.New Account
  2.Deposit
  3.Withdraw
  4.Balance Enquiry
  5.Close Bank Account
  6.Modify Account
  7.Exit
'''
#using While to run continuously
while True:
    print("Select the Option from the below Menu..")
    print("\n")
    print(o)
    option=input("Enter the option You want to choose: ")
    if option=="1":
        print("You Choose To Create New Account !")
        print("-----".center(80,"*"))
        #asking the customer to give input of how many accounts to be create
        #eval reads input as number..we can also give int in that place
        num_of_cus=eval(input("Enter How Many Accounts You Want To Create:"))
        i = i + num_of_cus
        #now we want to control the num_of_accounts count
        #don't allow accounts more than 5
        if i>len(cus_names):
            print("Customer Registration Exceeded!")
            i = i - num_of_cus
        else:
            #using while loop to run continuously for num_of_cus
            while counter_1 <= i:
                #receiving inputs from customer and creates account
                print(f"Enter Details For customer {counter_1}")
                name=input("Enter Your FullName: ").lower()
                pin=str(input("Enter Your Pin: "))
                deposit=eval(input("Deposit Some Amount To Create New Account: "))
                #saving the new account
                cus_names.append(name)
                cus_pins.append(pin)
                balance=0
                balance = balance + deposit
                cus_balance.append(balance)
                #printing account details
                print("\nName =", end=" ")
                print(cus_names[-1])
                print("\nPin =",end=" ")
                print(cus_pins[-1])
                print("\nBalance =",end=" ")
                print(cus_balance[-1],end=" ")
                print("-/Rs")
                counter_1 = counter_1 + 1 #increasing by one for every new customer 
                counter_2 = counter_2 + 2
                print("\n Your Account Created Successfully !!")
                print("***".center(80,"-"))
                print("Check Below: ")
                print(cus_names)
                print("\nNOTE!! Remember Your Name and Pin..")
                print("-----".center(80,"*"))
                #enter for main menu to select other option
        mainMenu= input("Press Enter To go Back to mainMenu or Exit")
    elif option=="2":
        print("You Selected To Deposit the Amount! ")
        n=0
        while n<1:
            k = -1
            name=input("Enter your Name: ").lower()
            pin=input("Enter your pin: ")
            #using while loop to find correct user
            while k < len(cus_names) -1:
                k = k + 1
                #if name,pin matched to existing name,pin
                if name==cus_names[k] and pin==cus_pins[k]:
                    n = n + 1
                    balance = cus_balance[k]
                    #depositing and adding new amount to old amount
                    deposit_amount = eval(input("Enter The Amount You Want to DEPOSITE: "))
                    balance = balance + deposit_amount
                    cus_balance[k] = balance
                    print("Amount Deposited Successfully!!")
                    print("***".center(80,"-"))
                    print("Your Total Balance After Deposit is: ",end=" ")
                    print(balance,end=" ")
                    print("-/Rs")
                    print("***".center(80,"-"))
        if n<1: #if n < 1 means name and pin wrong.name and pin correct means n increses by 1
            print("Invalid Name and pin...")
            break #so break
        #enter to go to main menu for another option
        mainMenu= input("Press Enter To go Back to mainMenu or Exit")
    elif option=="3":
        l=0
        print("You Choose to Withdraw the Amount: ")
        #using while loop to perform action only when name&pin matches
        while l<1: #runs continuosly until l<1 false
            k = -1
            name=input("Enter Your Name: ").lower()
            pin=str(input("Enter Your Pin: "))
            while k < len(cus_names) -1:
                k = k + 1
                if cus_names[k]==name and cus_pins[k]==pin:
                    l = l + 1 #if name ,pin matches increase l by 1
                    withdraw_amount=eval(input("Enter The Amount To WITHDRAW: "))
                    #when entering amount is greater than balance we can not withdraw
                    if withdraw_amount > balance :
                        print("***".center(80,"-"))
                        print("Your balance is LESS than the amount you ENTERED: ")
                        print("Your Balance Is: ",balance,"-/Rs")
                        print("Enter less amount than balance OR Deposit some amount and then withdraw!")
                        print("***".center(80,"-"))
                    else: #when entered amount less than balance
                        balance = balance - withdraw_amount
                        cus_balance[k] = balance
                        print("Withdraw Successful!!")
                        print(" Please Collect your Cash")
                        print("***".center(80,"-"))
                        print("Your Available balance After withdraw is: ",end=" ")
                        print(balance,"-/Rs")
                        print("***".center(80,"-"))
            if l < 1:
                print("Invalid Name and Pin..Try again..")   
                break
            mainMenu= input("\nPress Enter To go Back to mainMenu or Exit")
    elif option=="4":
        print("You Choose to Balance Enquiry!!")
        j=0
        while j < 1:
            k = -1
            name=input("Enter Your Name: ").lower()
            pin=str(input("Enter Your pin: "))
            while k < len(cus_names) - 1:
                k = k + 1
                if name==cus_names[k] and pin==cus_pins[k]:
                    j = j + 1
                    print("***".center(80,"-"))
                    print("Available Balance for the User:",cus_names[k]," is",end=" ")
                    print(cus_balance[k],"-/Rs")
                    print("***".center(80,"-"))
                
        if j < 1:
            print("Invalid input!! OR please Check Your Credentials") 
            break 
        mainMenu= input("\nPress Enter To go Back to mainMenu or Exit") 
    elif option=="5":
        print("You Choose To Close The Account!!")
        cnf=input("Please Confirm Once Again..to CLOSE press YES or NO: ").lower()
        if cnf=="yes":
            m=0
            while m < 1:
                k = -1
                name=input("Enter Your Name: ")
                pin=str(input("Enter Your Pin: "))
                while k < len(cus_names) -1:
                    k = k + 1
                    if name==cus_names[k] and pin==cus_pins[k]:
                        m = m + 1
                        cus_names.pop(k)
                        cus_pins.pop(k)
                        cus_balance.pop(k)
                        print("***".center(80,"-"))
                        print("Your Account has Closed Successfully!!")
                        print("***".center(80,"-"))
                        print("Updated Customer list is: ",cus_names)
                        print("***".center(80,"-"))

            if m < 1:
                print("Invalid Inputs!!")
                break
        else:
            print("\nYou Choose to Continue...")
        mainMenu= input("\nPress Enter To go Back to mainMenu or Exit") 
    elif option=="6":
        print("***".center(80,"-"))
        print("You Choose to Modify Your Account: ")
        s=0
        while s < 1:
            k = -1
            name=input("Enter Your Name: ").lower()
            pin=str(input("Enter Your Pin: "))
            while k < len(cus_names) - 1:
                k = k + 1
                if name==cus_names[k] and pin==cus_pins[k]:
                    s = s + 1
                    opt=input("\nType name to modify name,type pin to modify pin\n")
                    if opt=="name":
                        new_name=input("Enter The Name you Prefer: ").lower()
                        cus_names[k] = new_name
                        print("***".center(80,"-"))
                        print("Your name Updated Succesfully!!")
                        print("***".center(80,"-"))
                        print("Your New name is: ",cus_names[k])
                        print("***".center(80,"-"))
                    elif opt=="pin":
                        new_pin=input("Enter The PIN you Prefer: ")
                        cus_pins[k] = new_pin
                        print("***".center(80,"-"))
                        print("Your PIN Updated Succesfully!!")
                        print("***".center(80,"-"))
                        print("Your New name is: ",cus_pins[k])
                        print("***".center(80,"-"))
                    else:
                        print("\nInvalid Input!")
        if s < 1:
            print("Invalid Name and Pin!!")
            break
        mainMenu= input("\nPress Enter To go Back to mainMenu or Exit") 
    elif option=="7":
        print("You Choose To EXIT..")
        print("***".center(80,"-"))
        print("Thank You For Visiting!!")
        print("-----".center(80,"*"))
        print("! BHARATH BANK !".center(80))
        print("-----".center(80,"*"))
        print("Have a Greatday!!")
        break
    else:
        print("***".center(80,"-"))
        print("Invalid Option..Please Try Again!!")
        print("***".center(80,"-"))
        mainMenu= input("\nPress Enter To go Back to mainMenu or Exit") 








        







    

    