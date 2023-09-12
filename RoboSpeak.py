import os
from win32com.client import Dispatch
import win32com.client


def speak(text):
    try:
        speaker = win32com.client.Dispatch('SAPI.SpVoice')

        speaker.Speak(text)

    except Exception as e:
        print("Error occurred:", e)


# Example usage
# text_to_speak = "Hello, I am deepak Rawat the creator"
# speak(text_to_speak)

if __name__ == '__main__':

    print("Welcome to RoboSpeaker 1.1. Created by Deepak rawat ")
    while True:
        speak("you are using the text to voice software verion 1.1 and this is created by deepak rawat lets start this converstation")
        x = input("Enter what you want to speak: ")
        if x == "q":
            speak("'bye bye friend its time to end this conversation'")
            break
        command = f"say {x}"
        speak(x)
        os.system(command)

