import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set properties for controlling speech features
voices = engine.getProperty('voices')


# Adjust speech rate and volume
engine.setProperty('rate', 160)  # Speed of speech
engine.setProperty('volume', 9.0)  # Volume (0.0 to 1.0)

# Add text to be synthesized
text = "Hello, this is a sample text for speech synthesis"

# Synthesize and speak the text
engine.say(text)
engine.save_to_file(text,"test.mp3")
engine.runAndWait()
