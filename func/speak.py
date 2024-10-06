import pyttsx3
import threading
import queue

# Initialize the text-to-speech engine once at the global level
engine = pyttsx3.init('sapi5')

# Create a queue to hold speech requests
speech_queue = queue.Queue()

# Function for processing speech queue
def speech_worker():
    while True:
        response = speech_queue.get()  # Get speech text from the queue
        if response is None:
            break  # Exit the loop if a None value is received (used to stop the worker)
        engine.say(response)
        engine.runAndWait()
        speech_queue.task_done()  # Mark the task as done

# Start a dedicated thread for speech processing
speech_thread = threading.Thread(target=speech_worker, daemon=True)
speech_thread.start()

# Function for adding text to the speech queue
def speak(response):
    speech_queue.put(response)  # Add the response text to the queue

# Call this when you're done to safely stop the speech worker
def stop_speech_worker():
    speech_queue.put(None)  # Send a stop signal to the speech worker
    speech_thread.join()

