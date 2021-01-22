# This is a demo app "GUESS THE NUMBER"

from random import randint


class GuessNumberGame:
    secret = None
    attempts = 20

    @staticmethod
    def print_title():
        print("GUESS THE NUMBER FROM 1 TO 100\nYou have only 20 attempts.")

    def print_attempts_value(self):
        print(f"You have {self.attempts} attempts!")

    def set_new_secret(self):
        self.secret = randint(1, 101)
        print("New secret created!")

    def compare_value(self, value):
        if value > self.secret:
            print('Secret number is less than your value\n')
            return False
        elif value < self.secret:
            print('Secret number is more than your value\n')
            return False
        return True

    def attempts_available(self):
        if self.attempts != 0:
            return True
        else:
            return False

    def decrease_attempts_value(self):
        self.attempts -= 1


def start():
    game_finished = False
    game_status = None
    game = GuessNumberGame()
    game.set_new_secret()
    game.print_title()

    while not game_finished:
        value = int(input("Enter value: "))
        result = game.compare_value(value)
        if not result:
            game.decrease_attempts_value()
            if not game.attempts_available():
                game_status = 'lose'
                print("You have no attempts!")
                break
            game.print_attempts_value()
        else:
            game_status = 'won'
            break

    print(f"You {game_status}! Secret number equals {game.secret}.")


if __name__ == '__main__':
    start()
