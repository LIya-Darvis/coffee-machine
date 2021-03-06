def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    coffee = input()
    
    while True:
        if coffee == '1':
            if water >= 250 and beans >=16 and disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                print("")
                water -= 250
                beans -= 16
                disposable_cups -= 1
                money += 4
            else:
                if water < 250:
                    print("Sorry, not enough water!")
                    print("")
                if beans < 16:
                    print("Sorry, not enough beans!")
                    print("")
                if disposable_cups < 1:
                    print("Sorry, not enough cups!")
                    print("")
            break

        elif coffee == '2':
            if water >= 350 and milk >= 75 and beans >= 20 and disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                print("")
                water -= 350
                milk -= 75
                beans -= 20
                disposable_cups -= 1
                money += 7
            else:
                if water < 350:
                    print("Sorry, not enough water!")
                    print("")
                if milk < 75:
                    print("Sorry, not enough milk!")
                    print("")
                if beans < 20:
                    print("Sorry, not enough beans!")
                    print("")
                if disposable_cups < 1:
                    print("Sorry, not enough cups!")
                    print("")
            break
            
        elif coffee == '3':
            if water >= 200 and milk >= 100 and beans >= 12 and disposable_cups >= 1:
                print("I have enough resources, making you a coffee!")
                print("")
                water -= 200
                milk -= 100
                beans -= 12
                disposable_cups -= 1
                money += 6
            else:
                if water < 200:
                    print("Sorry, not enough water!")
                    print("")
                if milk < 100:
                    print("Sorry, not enough milk!")
                    print("")
                if beans < 12:
                    print("Sorry, not enough beans!")
                    print("")
                if disposable_cups < 1:
                    print("Sorry, not enough cups!")
                    print("")
            break
        elif coffee == 'back':
            break

##----------------------------------------##
        
def fill():
    print("Write how many ml of water do you want to add:")
    water_extra = int(input())
    print("Write how many ml of milk do you want to add:")
    milk_extra = int(input())
    print("Write how many grams of coffee beans do you want to add:")
    beans_extra = int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups_extra = int(input())
    print("")
    
    water += water_extra
    milk += milk_extra
    beans += beans_extra
    disposable_cups += disposable_cups_extra

##----------------------------------------##

def take():
    print(f"I gave you $ {money}")
    print("")
    money = 0

##----------------------------------------##

def remaining():
    
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")
    print("")

##----------------------------------------##

water = 400
milk = 540
beans = 120
disposable_cups = 9
money = 550

##----------------------------------------##

while True:
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        print("")
        buy()
    elif action == "fill":
        print("")
        fill()
    elif action == "take":
        print("")
        take()
    elif action == "remaining":
        print("")
        remaining()
    elif action == "exit":
        break
