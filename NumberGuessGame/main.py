import random

MIN = 1
MAX = 100
attempts = 5
win = False

number = random.randint(MIN, MAX)
last_hint = f"{'EVEN' if number % 2 == 0 else 'ODD'}"


def game_start():
    print(f"Please Guess any number between {MIN} and {MAX} within {attempts} attempts: ")
    input("Press ENTER to start game")


def game_play():
    global number, attempts, last_hint, win
    while attempts > 0:
        print()
        print(f"You have {attempts} {'attempts' if attempts > 1 else 'attempt'} left.")

        if attempts == 1:
            print(f"This is your last try. So the last hint is: {last_hint}")
        while True:
            try:
                guess = int(input("enter a lucky guess number:"))
                if guess in range(MIN, MAX+1):
                    break
                else:
                    print(f"Enter number between {MIN} and {MAX} inclusively.")
            except ValueError:
                print("Please input only numbers.")

        if guess == number:
            win = True
            break
        if attempts == 1:
            break
        if guess > number:
            if guess - number > 5:
                print("Too greater. Try smaller number.")
            else:
                print("Come on man! You are very close. Just a bit smaller and you will guess it.")
        else:
            if number - guess > 5:
                print("Too smaller. Try greater number.")
            else:
                print("Come on man! You are very close. Just a bit greater and you will guess it.")
        attempts -= 1


def game_finish(win):
    if win:
        print("Congratulations. You guessed it right. WINNER! WINNER! WINNER!")
    else:
        print(f"The lucky number is {number}.\nSorry You lost. Better luck next time.")


if __name__ == '__main__':
    game_start()
    game_play()
    game_finish(win)
