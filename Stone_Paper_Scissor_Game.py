import random
import time
import pyttsx3

computer=None
num=random.randint(1,3)

if num==1:
    computer="stone"
elif num==2:
    computer="paper"
else:
    computer="scissor"

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voices",voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def game(user,computer):
    if user==computer:
        speak("Game Drawn")
        print("\n\n*** Game Drawn ***")
    if user=="stone" and computer=="paper":
        speak("Computer won the game")
        print(f"\n\n*** Computer won the game ****")
    elif user=="stone" and computer=="scissor":
        speak(f"{name} won the game")
        print(f"\n\n*** {name} won the game ****")
    elif user=="paper" and computer=="stone":
        speak(f"{name} won the game")
        print(f"\n\n*** {name} won the game ***")
    elif user=="paper" and computer=="scissor":
        speak("Computer won the game")
        print(f"\n\n*** Computer won the game ****")
    elif user=="scissor" and computer=="stone":
        speak("Computer won the game")
        print(f"\n\n*** Computer won the game ****")
    elif user=="scissor" and computer=="paper":
        speak(f"{name} won the game ")
        print(f"\n\n*** {name} won the game ****")

if __name__=="__main__":
    speak("Please enter your good name")
    name=input("Please enter your good name:\n")

    speak(f"Welcome to the Game {name}")
    print(f"\n*** Welcome to the Game {name} ***")
    while True:
        speak("Your options are on screen")
        print("\n\nYour options are:\n\t- stone\n\t- paper\n\t- scissor\n\t- exit")
        time.sleep(2)

        speak(f"{name} Please enter your option")
        user=input(f"\n\n{name}, Please enter your option:\n")

        if user=="exit":
            speak(f"{name} exits the game")
            exit()

        elif user=="stone" or user=="paper" or user=="scissor":
            speak(f"{name} Selected {user}!")
            print(f"\n\n{name} Selected - {user}! ")

            speak("Wait, Computer selecting it's option")
            print("\n\nWait, Computer selecting it's option...")
            time.sleep(2)

            speak(f"Computer selected {computer}")
            print(f"\n\nComputer selected- {computer}!")
            game(user,computer)
        
        else:
            speak("Please choose the right option from List...")
            print("\n\nPlease choose the right option from List...")
