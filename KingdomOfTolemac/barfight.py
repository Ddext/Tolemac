import time
from sys import stdout
import stattrak

def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.02)
imp=""

def talking():
    shop()

def shop ():
    delay_print ("\nYou head back to the Richard and Bahls ready to turn in your quest as usual")
    time.sleep(1) # Sleep for 3 seconds
    delay_print ("\nAs you enter Richard and Bahls you make eye contact with Bahls")
    time.sleep(1)
    delay_print("\nYou ponder if he even moves as you've never even seen him move from his bar")
    time.sleep(1)
    delay_print("\nWhat do you want to do?")
    time.sleep(1)
    Imp = input ("\nDo you want to: A) Talk to Bahls the Barkeep? or B) Sit at a table and have a drink? [A/B]? : ")
    if Imp == "A" or imp== "a" :
        time.sleep(1)
        delay_print ("\nYou approach Bahls")
        time.sleep(1)
        delay_print("\nAs you sit at his bar you take a quick glance at his face but are just met with a look of disgust")
        time.sleep(1)
        delay_print("\nThe gods know what you have done you have commited too many crimes in this fair kingdom. The jarls knights will teach you a lesson!")
        guard_fight()
    elif Imp == "B" or imp=="b":
        time.sleep(1)
        delay_print("\nYou walk over to the table and you sit down you look around")
        time.sleep(1)
        delay_print("\nThe Barkeep approaches you")
        time.sleep(1)
        delay_print("\nYou ask him for a drink")
        time.sleep(1)
        delay_print("\nHe refuse to serve you")
        time.sleep(1)
        delay_print("\nNot after what you've done today you have caused so much trouble")
        guard_fight()
    else:
        delay_print("\nDumbass that's not an option. Start again")
        shop()

def guard_fight() :
    delay_print("\nSuddenly the bar door flies open and two of the kings men immediately approach you with their blades drawn")
    time.sleep(1)
    delay_print("\nIN ORDER OF THE KING STOP RIGHT THERE, YOU'VE COMMITED CRIMES AGAINST TOLEMAC AND HER PEOPLE WHAT SAY YOU IN YOUR DEFENCE!")
    time.sleep(1)
    delay_print("\nYou quickly grab a javelin that was hanging above the fireplace hurling it towards the guard knee immediately ending his adventuring career")
    time.sleep(1)
    delay_print("\nYou then move to the back of the bar where you find a set of armour and a sword, you quickly grab the sword and you face the last guard.")
    time.sleep(1)
    ack=input("\nHow do you attack?: Do you slash A) Do you stab B) [A/B]? : ")
    if  ack == "A" or ack == "a":
        delay_print("You slashed the guard and crit him dealing 20 damage, the Kings guards lay defeated. However you feel like you've now used up all your luck for today...")
        time.sleep(1)
        delay_print("\n*You drop the sword preferring the use of your stick*")
        time.sleep(1)
        delay_print("\nYou ran outside and encouter Richard, The Manager!")
        fight_intro()
    elif ack == "B" or ack == "b":
        delay_print("You stab the guard and he collapses to the ground")
        time.sleep(1)
        delay_print("*You drop the sword preferring the use of your stick*")
        time.sleep(1)
        delay_print("\nYou stumble outside almost falling over as you leave and then you see a ominous presence in front of you its the evil wizards")
        fight_intro()
    else:
        print("\nYou immediately fall over your stick and smash your head on the ground. You died. Try again?")
        time.sleep(1)
        stattrak.deathcount += 1
        shop()

def fight_intro():
    delay_print("\nLeave now or suffer the consequences!")
    time.sleep(1)
    delay_print("\nYou refuse to leave and get ready to battle")
    time.sleep(1)
    delay_print("\nSo be it \"hero\" Suddenly you feel a dark presence around")
    if stattrak.drunk==0 or stattrak.drunk==1 or stattrak.drunk==2:
        delay_print("\nYou see the manager morph into a evil wizard you've heard the guards talking about, the bring of death and ultimate power.")
        time.sleep(1)
        delay_print("\nThe wizard laughs at you and casts word scramble on you")
        fight()
    elif stattrak.drunk==3 or stattrak.drunk==4 or stattrak.drunk==5:
        delay_print("\nThe manager gives out a evil laugh as he and the bar tender morph together and reveal there true evil form.")
        time.sleep(1)
        fight()
    else:
        print("How the hell did you get this drunk and not die dirty cheater get back to the start and play the game properly")
        fight_intro()

def fight():
    Imp = input ("\n OCCXMOB:  A)Cox-Comb  B)Comb-Cox [A/B]? : ")
    if Imp == "A" or imp== "a":
        delay_print("\nNot bad for a child! However your efforts are in vain. My next attack will destroy you!")
        time.sleep(1)
        delay_print("\nYou laugh at his insults and strike him with your trusty stick dealing 10 damage!")
        time.sleep(1)
        delay_print("\nThe Wizard casts word scramble on you")
        stattrak.points += 1
        fight2()
    elif Imp == "B" or imp== "b":
        delay_print("\nHahaha you fool you lost on the easiest one now die like a fool")
        time.sleep(1)
        delay_print("\nThe wizard criticaly hits you for 999 damage!")
        time.sleep(1)
        delay_print("\nYou fall onto the floor unconscious!")
    else:
        print("\nDumbass that's not an answer go back and try agian")
        fight()

def fight2():
    Imp = input ("\n Mksarela:  A)Skamelar  B)Kamelars [A/B]? : ")
    if Imp == "A" or imp== "a":
        delay_print("\nHaha you think just because you got two right it will change anything?")
        time.sleep(1)
        delay_print("\nYou laugh at his insults and smash him in the face with your stick dealing 20 damage!")
        time.sleep(1)
        delay_print("\nThe Wizard casts word scramble on you")
        stattrak.points += 1
        fight3()
    elif Imp == "B" or imp== "b":
        delay_print("\nTold you I'd get your dumb ass this time!")
        time.sleep(1)
        delay_print("\nThe wizard criticaly hits you for 999 damage!")
        time.sleep(1)
        delay_print("\nYou fall onto the floor unconscious!")
    else:
        print("\Hey idiot that wasnt a answer go back and try again")
        fight2()

def fight3():
    Imp = input ("\n Orbes:  A)Sober  B)Robes [A/B]? : ")
    if Imp == "A" or imp== "a" or Imp == "B" or Imp == "b":
        delay_print("\nDoesn't matter what your answer was there. They're both correct but I'm tired of these stupid games.")
        time.sleep(1)
        delay_print("\nThe wizard critically hits you for 999 damage!")
        time.sleep(1)
        delay_print("\nYou fall onto the floor unconscious!")
    else:
        print("\nNice try but im still gonna kill you!")
        time.sleep(1)
        delay_print("\nThe wizard criticaly hits you for 999 damage!")
        time.sleep(1)
        delay_print("\nYou fall onto the floor unconscious!")

