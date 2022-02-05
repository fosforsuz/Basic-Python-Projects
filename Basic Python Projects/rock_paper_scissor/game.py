import random


class Game:
    def check(self, pc, user):
        options = {
            'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
            'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
            'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
            'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
            'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
            'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
            'fire': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
            'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
            'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
            'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
            'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
            'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
            'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
            'paper': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
            'air': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper']
        }
        if pc in options[user]:
            return False
        return True

    def __init__(self, name, rating, user_list):
        self.name = name
        self.rating = rating
        self.user_list = user_list

    def main(self):
        print("Okay, let's start")
        while True:
            random.seed()
            pc_choice = self.user_list[random.randint(0, len(self.user_list) - 1)]
            user_input = input()
            if user_input == "!rating":
                print(f"Your rating: {self.rating}")
            elif user_input == "!exit":
                print("Bye!")
                break
            elif user_input not in self.user_list:
                print("Invalid input")
            else:
                self.control(pc_choice, user_input)

    def control(self, pc, user):
        if pc == user:
            self.rating += 50
            print(f"There is a draw ({user})")
        elif self.check(pc, user):
            print("Well done. The computer chose {} and failed".format(pc))
            self.rating += 100
        else:
            print("Sorry, but the computer chose {}".format(pc))


def get_data():
    data_list = []
    with open('rating.txt', 'r') as file:
        for line in file:
            data_list.append(line.split())
    return data_list


if __name__ == "__main__":
    game = None
    user_name = input("Enter your name: ")
    print(f"Hello, {user_name}")
    user_limit = input()
    data = {}
    for key, value in get_data():
        data[key] = value
    if len(user_limit) != 0:
        limit = [item for item in user_limit.split(',')]
        if user_name in data:
            game = Game(user_name, int(data[user_name]), limit)
        else:
            game = Game(user_name, 0, limit)
    else:
        if user_name in data:
            game = Game(user_name, int(data[user_name]), ['rock', 'paper', 'scissors'])
        else:
            game = Game(user_name, 0, ['rock', 'paper', 'scissors'])
    game.main()
