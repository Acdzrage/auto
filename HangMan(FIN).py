import random

List = '''mountainous
vest
car
mailbox
gag
plastic
deranged
kindly
cable
cork
brush
beef
past
shorten
fry
functional
yell
develop
soggy
start
dapper
sink
overjoyed
amusement
splendid
questionable
useless
ragged
toothsome
even
laborer
greedy
draw
handsomely
girl
trust
regular
impel
makeshift
street'''
List = list(List.split('\n'))


def Start_App():
    print('Hi, Would you like to start your App?')
    start_cmd = input('> ')
    while start_cmd.lower() != 'yes' and start_cmd.lower() != 'quit':
        print('''ok let me know when you're ready''')
        start_cmd = input('> ')
    if start_cmd.lower() == 'quit':
        print('OK Bye!')
        quit()
    else:
        App()

def Try_again():
    Try = input(f'''wanna play again?
> ''')
    if Try.lower() == 'yes':
        App()
    else:
        Start_App()

def App():
    turns = 10
    word = random.choice(List)
    guesses = []
    while turns > 0:
            missing = 0
            for char in word:
                if char in guesses:
                    print(char, end='')
                else:
                    print('_', end='')
                    missing += 1
            if missing == 0:
                print('\nyou won')
                Try_again()
                break
            guess = input('''\nmake your guess
> ''')
            guesses.append(guess)
            if guess.lower() == 'quit':
                Start_App()
                break
            if guess not in word:
                turns -= 1
                print(f'Wrong, You have {turns} left')
                if turns == 0:
                    print(f'you failed, the word was [{word}]')
                    Try_again()
            












if __name__ == "__main__":
    Start_App()