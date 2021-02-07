class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = 'default'

    def remaining(self):
        print(f"""The coffee machine has:
{self.water} of water
{self.milk} of milk
{self.beans} of coffee beans
{self.cups} of disposable cups
${self.money} of money
        """)

    def change_values(self, water=0, milk=0, beans=0, cups=1, money=0):
        self.water -= water
        self.milk -= milk
        self.beans -= beans
        self.cups -= cups
        self.money += money
        print("I have enough resources, making you a coffee!")

    def buy(self):
        kind = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        if kind == '1':
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                self.change_values(water=250, beans=16, money=4)
        elif kind == '2':
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                self.change_values(water=350, milk=75, beans=20, money=7)
        elif kind == '3':
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough disposable cups!")
            else:
                self.change_values(water=200, milk=100, beans=12, money=6)
        else:
            pass

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0

    def handler(self):
        while True:
            if self.state == 'default':
                action = input("Write action (buy, fill, take, remaining, exit): ")
                self.state = action
                continue
            elif self.state == 'buy':
                self.buy()
                self.state = 'default'
                continue
            elif self.state == 'fill':
                self.fill()
                self.state = 'default'
                continue
            elif self.state == 'take':
                self.take()
                self.state = 'default'
                continue
            elif self.state == 'remaining':
                self.remaining()
                self.state = 'default'
                continue
            else:
                break


test = CoffeeMachine()
test.handler()
