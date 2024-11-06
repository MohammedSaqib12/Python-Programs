import speech_recognition as sr

# Specify the audio file
AUDIO_FILE = "SpeechText.wav"

# Initialize Recognizer
r = sr.Recognizer()

# Use the audio file as the source
with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)  # Read the entire audio file

# Recognize the audio and handle exceptions
try:
    print("Audio file contains: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio.")
except sr.RequestError:
    print("Couldn't get the result from Google Speech Recognition.")

