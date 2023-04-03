import sys
import time

class MainCharacter():
    def __init__(self):
        self.items = inventory
        self.health = 100
        self.strength = 6
        self.dexterity = 8
        self.stealth = 4
        self.cultivation_realm = None
        self.cultivation_realm_level = 0
        self.past_clues = []


def MainStory1():
    print("[You decide to stick your head outside of your cell and look around.]")
    time.sleep(2)
    print("[When you try to push on the cell, it doesn't budge an inch. It's sealed shut. As you look around the cell, you find a lock on the side of the cell.]")
    time.sleep(6)
    print("[A key is required to proceed]")
    time.sleep(1)
    if 'small mysterious key' in inventory:
        print("[You pull out the small key from your pocket and place it in a lock to see if it fits and surprisingly it fits and works!]")
        time.sleep(5)
        print("(Wait what? Why does the key I found in the butterfly pendant open the prison cell's lock? What's going on?)")
        time.sleep(4)
        print("[You decide to think about this later as you open your prison cell's door and exit it.]")
        time.sleep(3)
        print("[As you look around the run down prison, you realize that all the walls of the prison are made of stone, implying you might be underground.]")
        time.sleep(5)
        print("[But before you can think too hard about this, a wild Russian Bear from Western Russia breaks through the wall infront of you and charges at you, crashing through your prison cell and biting your head off]")
        time.sleep(9)
        print("[Dead]")
        time.sleep(1)
        print("[Hope you enjoyed the beta version of the game and the random ending. Check back soon!]")
        sys.exit()
    else:
        print("[A wild Russian Bear from Western Russia breaks through the wall infront of your prison cell and charges at you, crashing through your prison cell and biting your head off]")
        time.sleep(7)
        print("[Dead]")
        time.sleep(1)
        print("[Hope you enjoyed the beta version of the game and the random ending. Check back soon!]")
        sys.exit()

def Choice_Something_Else():
    print("[What would you like to do?]")
    print("[Choices:]\n[1)look outside my cell]")
    story_choice_starter = input()
    if story_choice_starter.lower() in ["look outside the cell","1"]:
        MainStory1()
    else:
        print("please choose from the choices provided")
        print("[Choices:]\n[1)look outside my cell]")
        story_choice_starter = input()

def ScenarioPrep1():
    print("[You decide to head over to your bed and search it]")
    time.sleep(2)
    print("[You searched throughout the whole bed and managed to find nothing.]")
    time.sleep(2)
    print("[Would you like to search the bed again or do something else?]")
    print("[Choices:]\n[1)bed]\n[2)something else]")
    search_choice3_stoneprisoncell = input()
    if search_choice3_stoneprisoncell.lower() in ["bed","1"]:
        print("[You search through the bed again but still find nothing.]")
        time.sleep(3)
        print("[Would you like to search the bed again or do something else?]")
        print("[Choices:]\n[1)something else]\n[2)bed again]")
        search_choice4_stoneprisoncell = input()
        if search_choice4_stoneprisoncell.lower() in ["something else","1"]:
            Choice_Something_Else()
        if search_choice4_stoneprisoncell.lower() in ["bed again","2"]:
            print("[This time you decide to search the bottom of the bed but unfortunetly still didn't manage to find anything]")
            time.sleep(4)
            print("[Would you like to search the bed again or do something else?]")
            print("[Choices:]\n[1)bed one more time]\n[2)something else]")
            search_choice5_stoneprisoncell = input()
            if search_choice5_stoneprisoncell.lower() in ["bed one more time","1"]:
                print("[This time, you decide to stick your hand underneath the bed to feel around for something.]")
                time.sleep(4)
                print("[As you stick your hand further under the bed and move it around, you fortunately managed to feel a wooden box near the corner]")
                time.sleep(6)
                print("[You pull the box out and open it to see what's inside.]")
                time.sleep(2)
                print("[Inside you manage to find a book that seems like a martial arts manual and as you look aat the cover, it says:]")
                time.sleep(3)
                print("['Universal Harmonic Technique']")
                inventory.append("universal harmonic martial arts manual")
                print("[Now what would you like to do]")
                print("[Choices:]\n[1)learn the cultivation manual(learn)]\n[2)something else]")
                major_decision1 = input()
                if major_decision1.lower() in ["learn","1"]:
                    print("[You open the manual and read the lines:]")
                    time.sleep(1)
                    print("'I am all but all is I, everywhere but nowhere, I am the 5 elements as they are me, and through their balance, Yin and Yang become balanced and I become the universe as it becomes one with me. For I am all and all is me.' You chant the chant on the first page of the manual with your eyes closed, focusing on it.")
                    time.sleep(8)
                    print("[When you finish reading the chant and open your eyes, you feel full of life, as if you are overflowing with strength and vitality, as if the universe's energy is flowing into you.]")
                    time.sleep(5)
                    mc.health = mc.health + 10
                    mc.strength = mc.strength + 5
                    mc.dexterity = mc.dexterity + 6
                    mc.stealth = mc.stealth + 11
                    mc.cultivation_realm = "Qi Gathering Realm"
                    mc.cultivation_realm_level = mc.cultivation_realm_level + 1
                    print("[Current Stats]:")
                    print("Vitality: " ,(mc.health))
                    print("Strength: " ,(mc.strength))
                    print("Dexterity: " ,(mc.dexterity))
                    print("Stealth: " ,(mc.stealth))
                    print("Cultivation Realm: " ,(mc.cultivation_realm))
                    print("Cultivation Realm(Level): " ,(mc.cultivation_realm_level))
                    print("Items: " ,(mc.items))
                    time.sleep(5)
                    print("What would you like to do now?")
                    print("[Choices:]\n[1) read more of the book]\n[2)something else]")
                    major_decision2 = input()
                    if major_decision2.lower() in ["read more of the book","1"]:
                        print("[You try to read the second page of the book but you get hit with a painful headache as you read through it.]")
                        time.sleep(4)
                        print("[hint: Maybe increasing your cultivation realm or level may allow you to comprehend more of the book]")
                        time.sleep(3)
                        print("What would you like to do instead?")
                        print("[Choices:]\n[1)something else]")
                        major_decision3 = input()
                        if major_decision3.lower() in ["something else","1"]:
                            Choice_Something_Else()
                    if major_decision2.lower() in ["something else","2"]:
                        Choice_Something_Else()
                if major_decision1.lower() in ["something else","2"]:
                    Choice_Something_Else()
        if search_choice5_stoneprisoncell.lower() in ["something else","2"]:
            Choice_Something_Else()
    if search_choice3_stoneprisoncell.lower() in ["something else","2"]:
        Choice_Something_Else()

def pendant():
    print("[You search your clothes and body for a book or anything that can tell you about your past]")
    time.sleep(4)
    print("[You thought your search was useless until you put your hand in your pockets and found something]")
    time.sleep(4)
    print("[You managed to find a pendant with a jade butterfly attached to it.]")
    time.sleep(3)
    print("[Would you like to pick it up or not?]")
    print("[hint: This may provide you with a link to your past if used correctly]")
    print("[Choices:]\n[1)yes]\n[2)no]")
    pickup_pendant_1 = input()
    ScenarioPrep1_1(pickup_pendant_1)

def ScenarioPrep1_1(pickup_pendant_1):
    if pickup_pendant_1.lower() in ["yes","1"]:
        print("[You decide to pick up the pendant and wear it around your neck]")
        inventory.append("jade butterfly pendant")
        mc.past_clues = mc.past_clues.append("jade butterfly pendant")
    if pickup_pendant_1.lower() in ["no","2"]:
        print("[You decide to throw away the pendant thinking its probably nothing much.]") 
        time.sleep(2)
        print("[As you throw it away on the ground, it shatters and reveals a small key in it.]")
        time.sleep(3)
        print("[You pick it up and decide to bite the key to make sure its real and not one of those fake chocolate keys you saw on Youtube like 60 years ago.]")
        time.sleep(6)
        print("[How many times would you like to bite the key?]")
        bite = input()
        bite = int(bite)
        time.sleep(2)
        bite_counter = 1
        for bite_counter in range(bite_counter, bite + 1):
            bite_counter = str(bite_counter)
            print("[You bit the key " +bite_counter+ " times]")
            bite_counter = int(bite_counter)
            time.sleep(1)
        bite = str(bite)
        print("[After biting the key " +bite+ " times, you finally confirm it isn't chocolate and place it in your pocket")
        inventory.append("small mysterious key")
        mc.past_clues = mc.past_clues.append("small mysterious key")
        time.sleep(5)
    print("[Would you like to search the bed or do something else?]")
    print("[Choices:]\n[1)bed]\n[2)something else]")
    search_choice2_stoneprisoncell = input()
    if search_choice2_stoneprisoncell.lower() in ["bed","1"]:
        ScenarioPrep1()
    if search_choice2_stoneprisoncell.lower() in ["something else","2"]:
        Choice_Something_Else()

if __name__ == "__main__":
    while True:
        print("'You must live no matter what, ∆µœåøŒ◊, as the successor of the--' A strange woman said as she bled out")
        time.sleep(3)
        print(".\n.\n.")
        time.sleep(1)
        print("'Keep up young master, we've almost escaped from them, soon, we should be able to leave his domain.' The old man walking with you said.")
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
        print("'Han Jue, erase this guy's memory and send him to Song Rye, till him we're keeping our part of the deal so he should keep his.' He said to one of the guards.")
        time.sleep(8)
        print(".\n.\n.")
        time.sleep(1)
        print("[You wake up suddenly in a cold sweat feeling disoriented by the confusing dream.]")
        time.sleep(3)
        print("[You look around your surroundings confused as you realize that you're in some strange prison cell.]")
        time.sleep(3)
        print("[The walls are made of rock as if your underground somewhere. There's an old and worn out bed in the corner.]")
        time.sleep(4)
        print("[As you try to recall the confusing dream you had, you realize a disturbing fact. You have no clue who you are!]")
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
        inventory = []
        mc = MainCharacter()
        if search_choice1_stoneprisoncell.lower() in ["bed","1"]:
            ScenarioPrep1()
        if search_choice1_stoneprisoncell.lower() in ["yourself","2"]:
            pendant()


#Ask Bowman to fix the for loop that starts at 0 not 1