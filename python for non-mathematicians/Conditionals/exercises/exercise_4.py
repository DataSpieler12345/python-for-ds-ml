# exercise 4
#Create a program that simulates an ATM with an initial balance of 2000 euros, with the following menu: 

#1. Money deposit
#2. Withdraw money
#3. Show money
#4. Exit
   
balance = 2000
print("1. deposit money")
print("2. withdraw money")
print("3. show money")
print("4. exit")

selection = int(input("Please select an option: "))

if selection ==1:
   deposit = float(input("amount to be deposited: "))
   balance += deposit
   print(f"your new balance is {balance}")
elif selection == 2:
   output=float(input("Money amount: "))
   if output>balance:
      print("insufficient balance")
   else:
      balance -= output
      print(f"New balance available: {balance}")
elif selection == 3:
   print(f"balance available: {balance}")
elif selection == 4:
   print("End")
else:
   print("Data entry error")

   
   