import time
from sys import stdout
import stattrak

def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.02)

def cred():
    delay_print("*You awake in a cold grey room with large metal bars blocking the exit.*")
    time.sleep(1)
    delay_print("\n*A man stands waiting for you to wake up from the other side of the bars*")
    time.sleep(1)
    delay_print("\nYou realise how fucking much you cost me kid? By destroying my park? How about a little reminder eh?")
    time.sleep(1)
    delay_print("\nSo your rampage started with you getting drunk and ruining my sons birthday party by smashing his cake")
    time.sleep(1)
    delay_print("\nYou then decided that wasnt enough and proceeded to go fight a roller coaster by throwing a fucking stick on the tracks.")
    time.sleep(1)
    delay_print("\nYou're lucky nobody comes to this hellhole anymore or else people could've been seriously hurt")
    time.sleep(1)
    if stattrak.points >= 5:
        delay_print("\nToday though? You're in luck. My insurance came through surprisingly so now I'm free of that god forsaken park")
        time.sleep(1)
        delay_print("\nWhat does this mean for you? Well I have no reason to keep you trapped here so let me go find your parents")
        time.sleep(1)
        delay_print("\nWait here. No funny business")
        time.sleep(1)
    elif stattrak.points >= 3:
        delay_print("\nYou're lucky that you're a minor and can't be trialed as an adult as I'd have you for life along with that stupid fucking barkeep Bahls")
        time.sleep(1)
        delay_print("\n")


def wallwrite():
    delay_print("\n*The man leaves and you go look at some etchings on a nearby wall, they read*")
    delay_print("\nIntro: Dexter Harris")
    delay_print("\nBarkeep: Dexter Harris, Antony Borji")
    delay_print("\nCaterpillar King: Dexter Harris")
    delay_print("\nDragon fight: Matt Singleton")
    delay_print("\nBarkeep fight: Martin Fanshawe")
    delay_print("\nEnding: Matt Singleton")
    delay_print("\nCredits: Dexter Harris")
    delay_print("\nStoryboarding: Antony Borji, Dexter Harris, Martin Fanshawe, Matt Singleton")
    epilogue()

def epilogue():
    if stattrak.points >= 5:
        delay_print("\nThe \"hero\" then lived on a fairly peaceful life with very faint memories of what happpened on that day")
        time.sleep(1)
        delay_print("\nThis was the best outcome as it could've ended much worse for our hero but they lived and that's all that matters")
        time.sleep(1)
        delay_print("\nThe kids at the birthday party got a new Collin the Caterpillar cake thanks to the insurance money from the parks damage")
        time.sleep(1)
        delay_print("\nBahls managed to rekindle his marriage with his wife however he moved away from working in the service industry and decided to travel")
        time.sleep(1)
        delay_print("\nWith Bahls resigning Richard relocated his Tavern to another theme park and called it Dicks Drinks")
    elif stattrak.points >= 3:
        delay_print("\n The \"hero\" was sent to a juvenile detention centre for a while however it was hard to make charges stick due to them being a drunk minor")
        time.sleep(1)
        delay_print("\nThe birthday that you sabotaged was eventually replanned elsewhere however it wasn't a Colin the Caterpillar Cake they could only afford a Cuthbert.")
        time.sleep(1)

    else:
        delay_print("")
