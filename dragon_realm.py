
import random
import time
friendName=''

def displayIntro():
    print('''You are in a land full of dragons. In front of you, 
you will see two caves. In one cave is a dragon that is friendly and will
share its treause with you. The other cave has a dragon that will eat you up. ''')
    print()

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print('which cave will you go into? (1 or 2)')
        cave = input()

    return cave

def checkCave(chosenCave):
    print ('you approch the cave...')
    time.sleep(2)
    print('its dark and spooky...')
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure')
    else:
        print('Gobbles you down in one bite')

def main():
    print('hi friend... what is your name')
    friendName=input()
    displayIntro()
    caveNumber=chooseCave()
    checkCave(caveNumber)
    playAgain='yes'
    while playAgain=='yes' or playAgain=='y':
        displayIntro()
        caveNumber=chooseCave()
        checkCave(caveNumber)
        print(friendName,',do you wanna play again')
        playAgain=input()

    print(friendName,',bye then....')
if __name__ == "__main__":
    main()