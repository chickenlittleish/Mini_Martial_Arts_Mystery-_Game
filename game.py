import sys
import time

class MainCharacter():
    def __init__(self):
        self.items = possessed_items

#def Scenario1Main():
    print()
def Scenario1Alternative():
    print("[You search your clothes and body for a book or anything that can tell you about your past]")
    time.sleep(5)
    print("[You thought your search was useless until you put your hand in your pockets and found something]")
    time.sleep(5)
    print("[You managed to find a pendant with a jade butterfly attached to it.]")
    time.sleep(5)
    possessed_items.append("jade butterfly pendant")
    print("[Where else would you like to search?]")
    print("[Choices:\n][1)bed]")
    #search_choice2_stoneprisoncell = input()
    #if search_choice2_stoneprisoncell.lower() == "bed":
        #Scenario1Main()
if __name__ == "__main__":
    while True:
        print("'You must live no matter what, ∆µœåøŒ◊, as the successor of the--' A strange woman said as she bled out")
        time.sleep(3)
        print(".\n.\n.")
        time.sleep(1)
        print("'Keep up young master, we've almost escaped from them, soon, we should be able to leave his domain.' The old man you were walking with said.")
        time.sleep(3)
        print(".\n.\n.")
        time.sleep(1)
        print("'Young master, *cough* *cough*, I don't have much time left, listen carefully, take this, it's the technique the lord entrusted to me to give to you, you must protect it with your life.' He said as he handed you a book and pulled out his sword.")
        time.sleep(5)
        print(".\n.\n.")
        time.sleep(1)
        print("'Go! You must escape no matter what! Go! Go!' He yelled as he stayed back to fight against the pursuers and you ran past him.")
        time.sleep(6)
        print(".\n.\n.")
        time.sleep(1)
        print("'Finally I caught you, you bastard. You thought you could escape me, now that she's gone, all that's left is to get rid of you now and I'll be the only successor.' A strange young man said as he laughed madly")
        time.sleep(7)
        print(".\n.\n.")
        time.sleep(1)
        print("'Han Jue, abolish this guys cultivation and leave him somewhere on the streets to die like the rat he is.' He said to one of the guards.")
        time.sleep(8)
        print(".\n.\n.")
        time.sleep(1)
        print("[You wake up suddenly in a cold sweat feeling disoriented by the confusing dream.]")
        time.sleep(3)
        print("[You look around your surroundings confused as you realize that you're in some strange prison cell.]")
        time.sleep(3)
        print("[The walls are made of rock as if someone carved a room into a mountain. There's an old and worn out bed in the corner.]")
        time.sleep(4)
        print("[As you try to recall the confusing dream you had, you realize a disturbing fact. You have no clue who you are]")
        time.sleep(4)
        print("[You try your hardest to remember who you are? where are you from? But each time you try to remember your past, you get hit with a painful headache.]")
        time.sleep(4)
        print("[You decide to stop trying to remember your past for now and instead try to find that strange book you were given in your dream.]")
        time.sleep(5)
        print("(That wasn't just a dream, that felt too real to be a dream. That book must be here somewhere, it's the only link to my past.)")
        time.sleep(8)
        print("[Where are you going to search for the book?]")
        print("[Choices:]\n[1)bed]\n[2)yourself]")
        search_choice1_stoneprisoncell = input()
        mc = MainCharacter()
        possessed_items = []
        #if search_choice1_stoneprisoncell.lower() == "bed":
            #Scenario1Main()
        if search_choice1_stoneprisoncell.lower() == "yourself":
            Scenario1Alternative()