import time
from sys import stdout


def delay_print(s):
    for c in s:
        stdout.write(c)
        stdout.flush()
        time.sleep(0.02)

def begin():
    delay_print("*You wake up to a familiar rocking back and forth. It's hard and abrupt but then quickly stops*")
    time.sleep(1)
    delay_print("\nHey you, you're finally awake")
    time.sleep(1)
    delay_print("\nYou were caught trying to cro- Wait no that's the other guy. You just passed out on this pirate ship.")
    time.sleep(1)
    delay_print("\nDon't worry the ride's over now but you seem lost as ever you should head over to Richard and Bahl's they'll set you straight")
    time.sleep(1)
    delay_print("\nI forgot to ask you. What's your name stranger?")
    input(" ")
    time.sleep(1)
    delay_print("That's a stupid name I'll just call you Hero. My name is Antony by the way. It won't come up again I just felt like sharing it for some reason")
    time.sleep(1)
    delay_print("\nAnyways you should head over to Richard and Bahl's and meet Bahl. He's a nice guy just don't get him started on")
    time.sleep(1)
    delay_print("\n*You leave the Pirate Ship and head towards Richard and Bahl's*")
    time.sleep(1)
    delay_print("\n*While on the way to Richard and Bahl's you find a big stick and for some reason decide to pick it up*")