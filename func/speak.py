import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')

# Function for speak the text response
def speak(response):
    # To change the voice in male/female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id) # 0 for male & 1 for female

    # To adjust the speaking speed
    engine.setProperty('rate', 175)

    engine.say(response)
    engine.runAndWait()