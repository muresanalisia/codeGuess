import game
from game.game import Game


class Ui:

    def __init__(self,game):
        self.game=game

    def intro(self):
        print("Hello and welcome to the game menu. The rules are simple. You must guess a code made of 4 distinct digits")


    def command(self):
        secret_number=self.game.generate_secret_number()
        print(f"The secret number is {secret_number}")
        while True:
            code=input("Enter code: ")
            if not code.isdigit():
                print("Invalid code")
            else:
                code=int(code)
                if code == 8086:
                    print(f"You entered the cheat code number. The code is: {secret_number}. Lucky!")
                    break
                else:
                    if not self.game.validate_code(code):
                        print("Invalid code")
                    if code==secret_number:
                        print(f"Correct! You guessed the correct code - {secret_number}! Good job!")
                        break
                    else:
                        print(f"Computer reports {self.game.count_codes(number=code, secret_number=secret_number)} codes and {self.game.count_runners(number=code, secret_number=secret_number)} runners")
















