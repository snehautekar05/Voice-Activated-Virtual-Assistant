from flask import Flask, render_template, jsonify
from func.listen import listen  # Import the listen function
from func.speak import speak    # Import the speak function
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    print("Received request")  # Log to ensure the route is called
    user_input = listen()  # Listen for user input directly from the microphone
    print(f"User input: {user_input}")  # Log the user input for debugging
    response_text = f"You said: {user_input}"  # Here you can implement command processing logic
    speak(response_text)  # Speak the response
    return jsonify({"response": response_text})


if __name__ == '__main__':
    app.run(debug=True)  # Run the Flask app
