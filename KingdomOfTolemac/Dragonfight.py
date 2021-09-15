import os
import random
import time
from sys import stdout

class Stats():
    def __init__(self, name, max_hp, strength, elixir, drunk):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.elixir = elixir
        self.elixir_level = drunk
        self.alive = True
        
hero = Stats("Hero", 100, 25, 1, 50)
dragon = Stats("Dragon", 150, 20, 0, 0)


def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.02)

def dragonevent():
    start()

def start():
    os.system("cls")
    delay_print("\nFat Knight 1: Hello there young one. Your abit small to be a Knight.\n")
    time.sleep(1)
    delay_print("\nFat Knight 2: HAHAHAHAAA... Iv seen stable boys larger than you little one.\n")
    time.sleep(1)
    input("\nPress Enter to continue:")
    os.system("cls")
    delay_print("\nYou look at the Fat Knight's and you say.....\n")
    time.sleep(1)
    print("\n1.) Your abit fat to be a knight...\n")
    time.sleep(1)
    print("\n2.) Dont worry i will grow into my armor...\n")
    time.sleep(1)
    print("\n3.) There is a naked woman around the corner...\n")
    time.sleep(1)
    options()

def options():
    option = input("\nChoose Your Response:")
    if option == "1":
        delay_print("\nFat Knight 1: You cheeky little shit!!! Get out of here before i feed you to the Dragon!\n")
        options()
    elif option == "2":
        delay_print("\nFat Knight 2: That maybe so but i can not let you pass, am sorry young one.\n")
        options()
    elif option == "3":
        os.system("cls")
        delay_print("\nFat Knight's with there tonge's out: OMG we have to see this.....\n")
        time.sleep(1)
        delay_print("\nThe Fat Knight's wobble away looking for the naked ladys.\n")
        time.sleep(1)
        input("\npress Enter to continue:")
        os.system("cls")
        delay_print("\nFrom inside the entrance of the cave all you can hear is the roar of the Mighty Dragon!\n")
        time.sleep(1)
        delay_print("\nChills run down your spine, children screem from within the cave.\n")
        time.sleep(1)
        delay_print("\nAs you look back to get help, the Knight's are gone and you are alone.\n")
        time.sleep(1)
        delay_print("\nYou say to yourself, Too small for my armor they said... I will show them who is too small...\n")
        time.sleep(1)
        input("\nPress Enter to continue:")
        os.system("cls")
        delay_print("\nAs you enter the cave, stick in hand, you feel the heat from the Mighty Dragon.\n")
        time.sleep(1)
        delay_print("\nYou say to yourself..\n")
        time.sleep(1)
        delay_print("\nHero: I think am about to shit myself!\n")
        time.sleep(1)
        delay_print("\nBut all of a sudden from out of nowhere the ground begins to shake!!!\n")
        time.sleep(1)
        delay_print("\nThe Mighty Dragon comes from the sky and knocks you off your feet.\n")
        time.sleep(1)
        delay_print("\nHero: You MOTHERF********\n")
        time.sleep(1)
        input("\nPress Enter to continue:")
        fight()
    else:
        options()





def fight():                                                                       #Battle logic                                                           
    os.system("cls")
    print       (f"""                {hero.name}      vs      {dragon.name}                                                                                  --^^^#####/        \#####^^^--_
        {hero.name}'s HP {hero.hp}/{hero.max_hp}        {dragon.name}'s HP {dragon.hp}/{dragon.max_hp}                                                                   -^##########/  (    )  \##########^-_
        Elixir's {hero.elixir}                                                                                                   -############/   |\^^/|   \############-
                                                                                                                   _/############/    (@::@)    \############\_
                                                                                                                  /#############(      \  /      )#############
    1.) Attack                                                                                                   -###############\     (oo)     /###############-
    2.) Drink elixir                                                                                            -#################\   / VV \   /#################-
    3.) Shout at the Dragon                                                                                    -###################\ /      \ /###################-
                                                                                                              _#/|##########/\######(   /\   )######/\##########|\#_
                                                                                                              |/ |#/\#/\#/\/  \#/\##\  |  |  /##/\#/  \/\#/\#/\#| \|
                                                                                                              `  |/  V  V  `   V  \#\| |  | |/#/  V   '  V  V  \|  '
                                                                                                                 `   `  `      `   / | |  | | \   '      '  '   '
                                                                                                                                  (  | |  | |  )
                                                                                                                                 __\ | |  | | /__
                                                                                                                                (vvv(VVV)(VVV)vvv)""")
    option = input("What will you do??? Enter a command:")
    if option == "1":
        print("Line113")
        time.sleep(2)
        attack()
    elif option == "2":
        drink_elixir()
    elif option == "3":
        os.system("cls")
        delay_print("\nHero: You have a small cock for a dragon.")
        time.sleep(2)
        os.system("cls")
        delay_print("\nMighty Dragon: WELL YOUR MUM LOVED IT.")
        time.sleep(3)
        fight()
    else:
        print("Line 125")
        time.sleep(2)
        attack()


evade = (0,20)

def attack():                                                                       #Hero AI
    evade = random.randint(0, 20)                     
    PAttack = random.randint(hero.strength/ 1, hero.strength)
    EAttack = random.randint(dragon.strength/ 1, dragon.strength)
    os.system("cls")
    if evade in range(10, 20):
        print("\nYou missed")
        print("")
        input("\nPress Enter to continue:")
        os.system("cls")                                 
    else:
        os.system("cls")
        dragon.hp -= PAttack                                                
        print(f"\nYou Deal {hero.strength} damage")
        print("")
        input("\npress Enter to continue:")
        os.system("cls")
    if dragon.hp <=0:
        win()
                                                                                    #Dragon AI  
    evade = random.randint(0, 20)                                                 
    
    if evade in range(10, 20):
        print("\nThe Mighty Dragon missed")
        print("")
        input("\nPress Enter to continue:")
        os.system("cls")
    else:
        hero.hp -= EAttack
        print(f"\nThe Mighty Dragon deals {dragon.strength} damage\n")
        input("\npress Enter to continue:")
        os.system("cls")
    if hero.hp <=0:
        death()
    else:
        fight()

#Elixir logic

def drink_elixir():
    os.system("cls")
    if hero.elixir == 0:
        delay_print("You have none left")
        time.sleep(1)
    else:
        hero.hp += 50
        hero.elixir -= 1
        delay_print("You have some more courage")
        time.sleep(1)
        os.system("cls")
        delay_print("Mighty Dragon: MWAHAHAHA YOU DRINK LIKE A LITTLE GIRL")
        time.sleep(3)
    if hero.hp > hero.max_hp:
        hero.hp = hero.max_hp
    fight()

#Win condition

def win():
    hero.hp = hero.max_hp
    dragon.hp = dragon.max_hp
    hero.elixir +=1
    delay_print("\nThe Mighty Dragon crys out, You see your chance to give the final blow\n")
    time.sleep(1)
    delay_print("\nYou thow your stick at the Mighty Dragon..\n")
    time.sleep(1)
    delay_print("\nThe Mighty Dragon falls to the ground, The ground shakes as the Mighty Dragon hits the floor\n")
    time.sleep(1)
    delay_print("\nThe dust settles, You hear the crys of the people that was in the cave..\n")
    time.sleep(1)
    delay_print("\nHero: Don't worry your saviour is here... You say with pride\n")
    time.sleep(1)
    delay_print("\nBut from behind you, you can hear a voice.....\n")
    time.sleep(1)
    delay_print("\nHAVE YOU LOST YOUR MIND... DO YOU HAVE ANY IDEA WHAT YOU HAVE JUST DONE?????\n")
    time.sleep(1)
    input("\nPress Enter to continue:")



#Lose condition

def death():
    hero.hp = hero.max_hp
    dragon.hp = dragon.max_hp
    hero.elixir +=1
    delay_print("\nCall yourself a Knight... More like chicken feed. Your dead NOOB, Try again")
    print("")
    input("\nPress Enter to continue:")
    start()













