# taylor
# Made by Joshua Hillis
import re
import time
while True:
    # i'm stupid so we have to do this again
    def inputFromUser():
        global tax
        global price

    print ("Made by Joshua Hillis")
    time.sleep(.5)

    tax = float(input("What is the tax rate we must apply to the item?"))
    price = float(input("What's the price of the item?"))

    if tax > 1:
        tax = (tax / 100)


    if re.search('[^\d\.$]', tax) or re.search('[^\d\.$%]', price):
        print ("please enter valid response")
        time.sleep(1)
    else:
        re.sub(('[^\d\.]', '', str(tax))
        re.sub(('[^\d\.]', '', str(price))

        if tax > (100):
            tax = (tax / 100)

        total = price + (price * tax)
        total = round(total, 2)

        print(total)
    while True:
        answer = input("Repeat? (y/n:)")
        if answer in ("y","n").lower():
            break
        print ("trying to break my program, bro?")
        if answer == "y":
            continue
        else:
            print ("Goodbye.")
            break
