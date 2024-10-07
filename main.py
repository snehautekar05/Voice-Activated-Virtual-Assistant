from func.listen import listen
from func.speak import speak
# from func.processCommand import processCmd

# Starting point of the program
if(__name__=="__main__"):
    speak("Initializing Alexa...")
    print("Alexa Initialized")
    speak("How can I help you today!")

    # Main Loop
    while True:
        word = listen()
        if("stop alexa"==word.lower() or "stop"==word.lower() or word.lower().startswith("stop")):
            print("Have a nice day!")
            speak("Thankyou, I am always ready to help you. Have a nice day!")
            break
        # elif("hello alexa"==word.lower() or "hey alexa"==word.lower() or "alexa"==word.lower()):
        #     print("Activated...")
        #     speak("I am listening.")

        command = listen()
        # processCmd(command)

input("Press Enter to STOP!")