import time
import sys
import random
import os

os.system("clear")

def battle(n):
    pokemon1 = raw_input("Player 1's Pokemon Name? ")
    pokemon2 = raw_input("Player 2's Pokemon Name? ")
    pokepower1 = random.randint(1,100)
    pokepower2 = random.randint(1,100)
    print 'Pokemon are doing battle! \n',
    pokepower1 = random.randint(1,100)
    pokepower2 = random.randint(1,100)
    for i in range(n):
        time.sleep(.25)
        print '\b.....' * 5,
        sys.stdout.flush()
    print '\nThe fight is finished!'
    raw_input("Press Enter to Continue.")
    print "\n"
    print "Name:" + " " + pokemon1 + "   " + "Power:" + " " + str(pokepower1)
    print "Name:" + " " + pokemon2 + "   " + "Power:" + " " + str(pokepower2)
    print "\n"
    if pokepower1 == pokepower2:
        print "It's a tie!"
    elif pokepower1 > pokepower2:
        print pokemon1 +  " " + "WINS THE BATTLE!"
    else:
        print pokemon2 +  " " + "WINS THE BATTLE!"

    print "\n"
    print "Enter 'B' to battle again, or 'E' to exit"
    if raw_input().lower() == "b":
        os.system("clear")
        battle(10)
    else:
        exit

battle(10)

