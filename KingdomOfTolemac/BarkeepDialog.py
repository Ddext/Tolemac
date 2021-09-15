#Imports
import time
from sys import stdout
import stattrak
import CatepillaKing
import gamestart
import barfight
import finale
import Dragonfight
import Ending

#Variables to save
drinkatt = 0
lossmethod = 0
barpplmet = 0


#Code
def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.002)

def startintro():
    gamestart.begin()


def gameover():
    time.sleep(1)
    global deathcount
    if lossmethod == 1:
        delay_print("Really? You got drunk as fuck and hugged Bahl's? I mean the guy is going through a rough divorce but you barely know the guy.")
        time.sleep(1)
        delay_print("\nAnyways I'd say I'm merciful so I'll send you back to the bar. This time don't be such a fucking idiot.")
        global drunk
        drunk = 4
        stattrak.deathcount +=1
        doforu()

def introtobar():
    delay_print("\nAs you enter the bar you look around to see various shady individuals engaged in conversation with each other")
    time.sleep(1) 
    delay_print("\nWhile examining the room the Barkeep calls you over")
    time.sleep(1)
    delay_print("\nWelcome to Richard and Bahl's stranger. You're not from around here are you?")
    time.sleep(1)
    delay_print("\nDon't answer that it's obvious based on your face")
    time.sleep(1)
    doforu()

def welcomebak():
    delay_print("\nOh! Welcome back stranger. Did you finish the quest I sent you on?")
    time.sleep(1)
    delay_print("\nIt doesn't matter if you did as I have more pointless tasks to send you on. Gotta pass time somehow right? Otherwise this game would be really short")
    doforu()

def doforu():
    delay_print("\nSo, what can I do for you?")
    time.sleep(1)
    print("\nQuest: 1")
    print("Drink: 2")
    print("What's for sale?: 3")
    print("Anywhere to sleep?: 4")     #No fuck off
    print("Ask about people in the bar: 5")
    if stattrak.drunk >= 5:
        print("Can I have a hug?: 6")
    ans = int(input())
    if ans == 1:
        questdiag()
    elif ans == 2:
        drinkdiag()
    elif ans == 3:
        delay_print("I'm for sale if you have enough money ;)")
        time.sleep(1)
        delay_print("\n*You quickly assure the barkeep you are not interested. He seems disappointed*")
        doforu()
    elif ans == 4:
        delay_print("No fuck off.")
        time.sleep(1)
        doforu()
    elif ans == 5:
        time.sleep(1)
        barppl()
    elif ans == 6 and stattrak.drunk >= 5:
        delay_print("*Bahl's hugs you softly and you slowly pass out*\n")
        global lossmethod
        lossmethod = 1
        gameover()

def questdiag():
    if stattrak.caterpillarfight == True:
        delay_print("So you slayed the Caterpillar King?!?!?!?!? Wow you're impressive.")
        time.sleep(1)
        delay_print("\nHowever! I bet you can't conquer the Dragon Flyer though!")
        time.sleep(1)
        delay_print("\nHere, take this it'll help you with your courage.")
        time.sleep(1)
        delay_print("\nBahl's gives you an elixir of courage")
        global elixir
        stattrak.elixir += 1
        Dragonfight.dragonevent()
    else:
        delay_print("So you're looking for a quest? Alright how about this. I hear tales of a mighty tyrant known as The Caterpillar King")
        time.sleep(1)
        delay_print("\nHe resides in his own lair. Any knight to ever attempt to challenge him has never returned")
        time.sleep(1)
        delay_print("\nTo find his lair you'll need to head out of here, turn left and walk for about 20 minutes, there it'll be on your immediate right. You can't miss it.")
        time.sleep(1)
        delay_print("\nYou leave the tavern and start to travel towards The Lair of The Caterpillar King")
        CatepillaKing.catepilla()

def drinkdiag():
    global drinkatt
    if stattrak.drunk >= 5:
        delay_print("Nice try but no.")
        time.sleep(1)
        doforu()
    elif stattrak.drunk >= 4 and drinkatt >= 4:
        delay_print("Fine. You've twisted my ear. One more drink but you're done after this any more and I'll call the guards.")
        stattrak.drunk += 1
        doforu()
    elif stattrak.drunk >= 4 and drinkatt >= 3:
        delay_print("This is the last time I'll say it. I'm not serving you any more.")
        drinkatt += 1
        doforu()    
    elif stattrak.drunk >= 4 and drinkatt >= 2:
        delay_print("Seriously stop.")
        drinkatt += 1
        doforu()
    elif stattrak.drunk >= 4 and drinkatt >= 1:
        delay_print("Look I said no more. Stop asking.")
        drinkatt += 1
        doforu()    
    elif stattrak.drunk >= 4:
        delay_print("Sorry mate no more you've had way too much.")
        drinkatt += 1
        doforu()
    else:
        delay_print("Here you go lad one pint of mead")
        stattrak.drunk +=1
        doforu()

def barppl():
    global barpplmet
    if barpplmet == 0:
        delay_print("See that guy over there dressed in a green shirt and white tights?")
        time.sleep(1)
        delay_print("\nI don't know his name but comes in every day. Doesn't say much just makes weird yells like \"HYAH\" and pays with these weird gems")
        time.sleep(1)
        delay_print("\nDunno where they come from but feels more valuable than what I'm usually getting and he gives me a lot")
        barpplmet +=1
    elif barpplmet == 1:
        delay_print("Have you met the italian man dressed in that weird white coat in the corner?")
        time.sleep(1)
        delay_print("\nHe's apparently from italy. Dunno why he's here but apparently he has a mission here.")
        time.sleep(1)
        barpplmet +=1
    elif barpplmet == 2:
        delay_print("See the man in the far corner back there with a dog and a pencil? Don't mess with him at all and especially do NOT touch his dog")
        time.sleep(1)
        delay_print("\n*You look at the man confused as to why*")
        time.sleep(1)
        delay_print("\nIf you even try I can guarantee that dragons and kings will be the least of your worries")
        time.sleep(1)
        barpplmet +=1
    elif barpplmet == 3:
        delay_print("The guy with the big sword? Yeah I got no clue how he carries that around it's nearly as big as him")
        time.sleep(1)
        delay_print("Really fucking serious too despite looking like he's from some sort of drawing")
        time.sleep(1)
        barpplmet +=1
    else:
        delay_print("Oh so you spotted the guy trying to hide in the shadows? Not many people do.")
        time.sleep(1)
        delay_print("\nDunno where he's from but he seems really obsessed with bats and finding out about some sort of clown?")
        time.sleep(1)
        delay_print("\nPays really well though and keeps quiet so I have no problem with him just find it all a bit weird")
        time.sleep(1)
    doforu()    

def returntobar():
    barfight.talking()

def leaving():
    Ending.draggedout()

def credits():
    finale.cred()

startintro()
introtobar()
welcomebak()
returntobar()
leaving()
credits()