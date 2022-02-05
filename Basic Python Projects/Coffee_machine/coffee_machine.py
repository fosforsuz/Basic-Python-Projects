class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cups = 9
        self.money = 550

    def __str__(self):
        return '\nThe coffee machine has:\n' + str(self.water) + ' of water\n' + \
               str(self.milk) + ' of milk\n' + str(self.coffee) + ' of coffee beans\n' + \
               str(self.cups) + ' of cups\n$' + str(self.money) + ' of money\n'

    def buy(self):
        choice = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino back - to main menu:\n")
        if choice == 'back':
            return None
        choice = int(choice)
        if choice == 1:  # Espresso
            if min(self.water // 250, self.coffee // 16) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.coffee -= 16
                self.money += 4
                self.cups -= 1
            else:
                self.control(1)
        elif choice == 2:  # Latte
            if min(self.water // 350, self.milk // 75, self.coffee // 20) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.coffee -= 20
                self.money += 7
                self.cups -= 1
            else:
                self.control(2)
        elif choice == 3:  # cappuccino
            if min(self.water // 200, self.milk // 100, self.coffee // 12) >= 1:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.coffee -= 12
                self.money += 6
                self.cups -= 1
            else:
                self.control(3)

    def control(self, type_coffee):
        if type_coffee == 1:
            control_water = self.water // 250
            control_coffee = self.coffee // 16
        elif type_coffee == 2:
            control_water = self.water // 350
            control_coffee = self.coffee // 20
            control_milk = self.milk // 75
        elif type_coffee == 3:
            control_water = self.water // 200
            control_milk = self.milk // 100
            control_coffee = self.coffee // 12
        self.print_control(control_water, control_milk, control_coffee)

    def print_control(self, c_water, c_milk, c_coffee):
        if c_water == 0:
            print("Sory, not enough water!")
        elif c_milk == 0:
            print("Sory, not enough milk!")
        elif c_coffee == 0:
            print("Sory, not enought coffee!")

    def fill(self):
        self.water += int(input("Write how many ml of water do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk do you want to add:\n"))
        self.coffee += int(input("Write how many grams of coffee beans do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

    def take(self):
        print(f"I gave you ${self.money}")
        self.money = 0


machine = CoffeeMachine()
while True:
    choice = input("Write action (buy, fill, take, remaining, exit):\n")
    print("\n")
    if choice == "remaining":
        print(machine)
    elif choice == "buy":
        machine.buy()
    elif choice == "fill":
        machine.fill()
    elif choice == "take":
        machine.take()
    elif choice == "exit":
        break
