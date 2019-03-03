# Made by Joshua Hillis
import re
import time
while True:

    global tax
    global price

    print ("Made by Joshua Hillis")
    time.sleep(.5)

    tax = input("What is the tax rate we must apply to the item?")
    price = input("What's the price of the item?")

    tax = float(tax)
    price = float(price)
    print = str(format((round((float(tax) / 100 + 1) * float(price), 2)), '.2f'))

    if re.search('[^\d\.$]', str(tax)) or re.search('[^\d\.$%]', str(price)):
        print ("please enter valid response")
        time.sleep(1)
    else:
        re.sub('[^\d\.]', '', str(tax))
        re.sub('[^\d\.]', '', str(price))

        if tax > (100):
            tax = (tax / 100)

        total = price + (price * tax)
        total = round(total, 2)

        print(total)
    while True:
        answer = input("Repeat? (y/n:)").lower()

        if answer == "y" or answer == "n":
            if answer == "y":
                tax = input("What is the tax rate we must apply to the item?")
                price = input("What's the price of the item?")

            if re.search('[^\d\.$]', str(tax)) or re.search('[^\d\.$%]', str(price)):
                print("please enter valid response")
                time.sleep(1)
            else:
                re.sub('[^\d\.]', '', str(tax))
                re.sub('[^\d\.]', '', str(price))
            tax = float(tax)
            price = float(price)
            print = str(format((round((float(tax) / 100 + 1) * float(price), 2)), '.2f'))
        else:
            print("Goodbye.")
            break
