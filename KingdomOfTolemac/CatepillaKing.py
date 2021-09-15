
import random
import time
from sys import stdout
import stattrak

def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.02)

bobbypins = 0
locknum = (0,20)
approach = 0
lossmethod = 0

def catepilla():
    delay_print("\n*You approach the door to The Lair of The Caterpillar King. Behind it you hear screams and yelling*")
    time.sleep(1)
    doorlock = input("\nDo you try to open it? [Y/N] ")
    global lossmethod
    if doorlock == "Y" or doorlock == "y":
        delay_print("*Upon trying to open the door you notice it is locked*")
        time.sleep(1)
        catepilla2()
    elif doorlock == "N" or doorlock == "n":
        delay_print("*Nothing happens so you eventually try to open the door")
        time.sleep(1)
        catepilla2()
    else:
        delay_print("You stand absentmindedly for hours doing nothing ")
        lossmethod = 1
        gameover()

def gameover():
    time.sleep(1)
    if lossmethod == 1:
        delay_print("\n*Slow Clap*")
        time.sleep(1)
        stattrak.deathcount +=1
        delay_print("\nReally thought that the door would magically open without trying anything? Nah not happening. Try again.")
        time.sleep(1)
        catepilla()
    elif lossmethod == 2:
        delay_print("\nY'know the list has 2 options right? I know you're pretty dumb but c'mon dude.")
        time.sleep(1)
        delay_print("\nWhatever though I'm not gonna make you replay all this shit again. It's already painful enough to watch you play this let alone this awful dialog.")
        time.sleep(1)
        catelair()

def catepilla2():
        lookaroundcat = (input("\nWould you like to look around? [Y/N] "))
        global bobbypins
        if lookaroundcat == "Y" or lookaroundcat == "y":
            delay_print("On the floor you find three lockpicks\n")
            time.sleep(1)
            bobbypins += 3
            lockpick()
        else:
            delay_print("*You stand around looking like an idiot until you eventually notice three lockpicks under your shoe*")
            time.sleep(1)
            bobbypins += 3
            lockpick()

def lockpick():
    global bobbypins
    if bobbypins == 0:
        delay_print("\n*Defeated you realise you are out of lockpicks as you slump to the floor a fellow knight approaches you*")
        time.sleep(1)
        delay_print("\nHail sir Knight are you aiming to challenge the Caterpillar King? You're in luck for I have the key")
        time.sleep(1)
        delay_print("\n*The knight unlocks the door for you and leaves you alone to battle the Caterpillar king and free the peasants from his rule*")
        time.sleep(1)
        catelair()
    else:
        delay_print("You attempt to unlock the door")
        time.sleep(1)
        if stattrak.drunk >= 4:
            locknum = random.randint(0,100)
            if locknum in range(10,20):
                delay_print("\nYou unlock the door")
                time.sleep(1)
                catelair()
            else:
                locksleft()
        elif stattrak.drunk >= 3:
            locknum = random.randint(0,80)
            if locknum in range(10,20):
                delay_print("\nYou unlock the door")
                time.sleep(1)
                catelair()
            else:
                locksleft()
        elif stattrak.drunk >= 2:
            locknum = random.randint(0,60)
            if locknum in range(10,20):
                delay_print("\nYou unlock the door")
                time.sleep(1)
                catelair()
            else:
                locksleft()
        elif stattrak.drunk >= 1:
            locknum = random.randint(0,40)
            if locknum in range(10,20):
                delay_print("\nYou unlock the door")
                time.sleep(1)
                catelair()
            else:
                locksleft()
        else:
            locknum = random.randint(0,20)
            if locknum in range(10,20):
                delay_print("\nYou unlock the door")
                time.sleep(1)
                catelair()
            else:
                locksleft()

def locksleft():
    global bobbypins
    bobbypins -= 1
    print(f"\nYou fail to unlock the door, losing a lockpick in the process. You have {bobbypins} lockpicks left")
    time.sleep(1)
    if bobbypins >= 1:
        delay_print("*You try again*\n")
        time.sleep(1)
    lockpick()



def catelair():
    delay_print("""\n*As you enter The Lair of The Caterpillar King you immediately notice multiple fallen knights laying on the ground defeated.
Unperturbed you immediately lock eyes with the Caterpillar King*""")
    time.sleep(1)
    print("""\n    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
    @@@@@@@@@@@@... .@@@@@,..   @@@@@@@@@@@@
    @@@@@@@@@@.....   .,......    @@@@@@@@@@
    @@@@@@@@@@......  .........   @@@@@@@@@@
    @@@@@@@@@@@.,,,... ........  @@@@@@@@@@@
    @@@@@@@@(........,..,...       @@@@@@@@@
    @@@@@@*.....*%%%%,.*%%%##....    @@@@@@@
    @@@@@.....,#%%%%%%#%%%%%##( ..     %@@@@
    @@@@......##%%%%%%%%%%%%%%%(...      @@@
    @@@.......,##%%%%%#%%##%##(...  .     @@
    @@@....,,,.....,,..,,,,,.......,...   @@
    @@@....,,.............         .,,.  @@@
    @@@@@..,,.............      .......@@@@@
    @@@@@@@@@@@*,,,..,*//**.  ....(@@@@@@@@@
    @@@@@@@@@@@@@@@@#,****,. .@@@@@@@@@@@@@@
    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@""")
    time.sleep(7)
    delay_print("*He stands alone atop a royal podium towards the centre of the room unguarded.")
    time.sleep(1)
    if stattrak.drunk >= 3:
        delay_print("\nYou rush towards the Caterpillar King screaming gibberish in a mad dash to strike him down")
        time.sleep(1)
        delay_print(f"\nAs you finally reach his podium you slam your mighty {stattrak.weapon} down crushing the once mighty Caterpillar King")
        time.sleep(1)
        delay_print("\nUpon your victory one of the peasants helps you escape The Lair of The Caterpillar King allowing you to return to the potion vendor")
        time.sleep(1)
        stattrak.caterpillarfight = True
    else:
        delay_print("\nWould you like to sneak towards the Caterpillar King or charge head first?")
        time.sleep(1)
        delay_print("\nStealth: 1")
        delay_print("\nCharge head first: 2\n")
        approach = int(input())
        if approach == 1:
            delay_print("You quietly sneak towards the Caterpillar Kings podium")
            time.sleep(1)
            delay_print(f"\nYou quietly sneak behind him and pierce his abdomen with your {stattrak.weapon}")
            time.sleep(1)
            delay_print("\nWith the Caterpillar King defeated you quietly sneak out worried about any potential guards finding out what you did to their ruler")
            time.sleep(1)
            stattrak.points += 2
            stattrak.caterpillarfight = True
        elif approach == 2:
            delay_print("Rushing towards the Caterpillar King you think about the fallen warriors surrounding you")
            time.sleep(1)
            delay_print(f"\nUpon reaching the Caterpillar King you lunge your {stattrak.weapon} straight through his face immediately ending his tyranical rule")
            time.sleep(1)
            delay_print("\nAs the Caterpillar King lays defeated before you from the corner of your eye you notice knights in black and green approaching you.")
            time.sleep(1)
            delay_print("\nKnowing these are NOT the knights of Tolemac you hastily exit The Lair of The Caterpillar King and return to the barkeep")
            stattrak.points += 1
            stattrak.caterpillarfight = True
        else:
            delay_print("\nOkay smartass for that you get noticed by The Caterpillar King who immediately summons his guards who kill you")
            global lossmethod
            lossmethod = 2
            gameover()
