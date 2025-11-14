import pyttsx3
import speech_recognition as sr
import eel

def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening....")
        eel.displayMessage("listening....")   # FIXED
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)

    try:
        print("recognizing...")
        eel.displayMessage("recognizing...")  # FIXED
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")
        eel.displayMessage(query)             # FIXED
        speak(query)

    except Exception as e:
        eel.displayMessage("Sorry, I didn't catch that.")
        print(e)
        return ""

    return query.lower()
