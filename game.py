import sys
import time



#ASK BOWMAN ABOUT TIMER AND HOW
def countdown_timer(t):
     #https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/
    while t:
        t = 60
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    if t == 0:
         rage_scene_1()


class Player():
    #This is where the data related to the player like their name, their status, and etc
    def __init__(self):
            self.name = name
            self.alive = True
            self.age = age

if __name__ == "__main__":
    while True:
        #ADD CAPTION
        print("[You wake up and cover your barely opened eyes from the bright light in your face].")
        time.sleep(2)
        print("[As you're confused about your current situation, you hear a door behind you open.]")
        time.sleep(2)
        print("[As you try to stand up to look behind, you realized you're currently handcuffed to the table.]")
        time.sleep(4)
        print("[A man enters the room and sits down in the chair infront of you.]")
        time.sleep(3)
        print("What's your name?\n")
        name = input()


        print("[You see the man pull out a notebook and write in it.]")
        time.sleep(5)
        print("What's your age?\n")
        age = input()


        print(" ")
        time.sleep(3)

        #aggressiveness reaches ten, beats you up till your almost done security comes and he walks out and tells them to take you away