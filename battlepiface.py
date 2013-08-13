import time
import sys
import random
import os
import time
import piface.pfio

piface.pfio.init()

led1 = piface.pfio.LED(1)
led2 = piface.pfio.LED(2)
led3 = piface.pfio.LED(3)
led4 = piface.pfio.LED(4)
led5 = piface.pfio.LED(5)
led6 = piface.pfio.LED(6)
led7 = piface.pfio.LED(7)

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
        cycleleds(1)
        time.sleep(.05)
        print '\b.....' * 5,
        sys.stdout.flush()
    print '\nThe fight is finished!'
    #raw_input("Press Enter to Continue.")
    print "\n"
    print "Name:" + " " + pokemon1.upper() + "   " + "Power:" + " " + str(pokepower1)
    print "Name:" + " " + pokemon2.upper() + "   " + "Power:" + " " + str(pokepower2)
    print "\n"
    if pokepower1 == pokepower2:
        print " " * 30 +  "It's a tie!"
    elif pokepower1 > pokepower2:
        print " " * 30 + pokemon1.upper() +  " " + "WINS THE BATTLE!"
    else:
        print " " * 30 + pokemon2.upper() +  " " + "WINS THE BATTLE!"

    print "\n"
    print "Enter 'B' to battle again, or 'E' to exit"
    if raw_input().lower() == "b":
        os.system("clear")
        battle(10)
    else:
        exit

def cycleleds(argv):
    cnt = 0
    loop = 0
    while loop < argv:
        for cnt in range(2, 8):
            led = piface.pfio.LED(cnt)
            led.turn_on()
            time.sleep(.05)
            led.turn_off()
            loop += 1
#cycleleds(100)
battle(10)

