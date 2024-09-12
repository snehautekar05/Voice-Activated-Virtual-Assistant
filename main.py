import speech_recognition as sr
import pyttsx3

# Initialize the speech recognizer
r = sr.Recognizer()
r.energy_threshold = 300  # Adjust for silence detection
r.dynamic_energy_threshold = True

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Function for listen the input-voice & recognition it
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        print("Listening...")
        audio = r.listen(source, timeout=5, phrase_time_limit=10)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio) # Use the speech recognizer to convert speech to text
        print(f"You said --> {command}.")
    except Exception as e:
        print("Sorry, I didn't catch that. Please try again!")
        return ""
    
    return command

# Function for speak the text response
def speak(response):
    # To change the voice in male/female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)

    # To adjust the speaking speed
    engine.setProperty('rate', 170)

    engine.say(response)
    engine.runAndWait()

# Function for process the commands or function for features
def process_command(command):
    print(command)

# Main loop
if(__name__=="__main__"):
    print("Initializing Devox...")
    speak("Initializing Devox")
    speak("I am your personal assistant. How can I help you today!")

    while True:
        word = listen()

        if("devox" in word.lower()):
            print("Devox activated...")
            speak("Devox activated")

            command = listen()
            process_command(command)
        elif("stop devox" in word.lower()):
            break