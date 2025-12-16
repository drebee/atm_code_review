# start with 1 million dollars
balance = 1000000
while True:
   response = input("ATM at your service")
   if response == "Check":
       print(balance)
   if response == "Withdraw":
       withdrawal = int(input("How much would you like to withdraw?"))
       if withdrawal < balance and withdrawal > 0:
           balance = balance - withdrawal
       if withdrawal < 0:
           print("Error")
       if withdrawal > balance:
           print("Error")
   if response == "Deposit":
       deposit = int(input("How much would you like to deposit?"))
       if deposit > 0:
           balance = balance + deposit
       if deposit < 0:
           print("Error")
   qwerty = input("Exit?")
   if qwerty == "Yes":
       break