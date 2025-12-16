# start with 1 million dollars
balance = 1000000


while True:
   UInput = input("Enter Action: ").lower().replace(" ","")
   if(UInput == "checkbalance"):
       print(f"Your balance is :{balance}")
   elif(UInput == "withdraw"):
       try:
           howmuch = int(input("how much to withdraw? "))
       except TypeError:
           print("must be an integer!")
       else:
           if(balance>=howmuch and howmuch>=0):
               balance = balance - howmuch
               print(f"You widthdrew {howmuch} & have {balance} left.")
           else:
               print("Negitive or greater than balance")
   elif(UInput=="deposit"):
       try:
           howmuch = int(input("how much to deposit? "))
       except TypeError:
           print("must be an integer!")
       else:
           if(howmuch>=0):
               balance = balance + howmuch
               print(f"You deposited {howmuch} & have {balance} left.")
           else:
               print("howmuch must be postive!")
   elif(UInput == "exit"):
       quit()
   else:
       print(f"unrecognized input: {UInput}. Try checkbalance, deposit, or withdraw")