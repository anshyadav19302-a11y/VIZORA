from playsound import playsound
import eel

# playing assistant sound function

@eel.expose
def playassistantsound():
    music_dir = "C:\\Users\\SPIDE\\VIZORA\\www\\assets\\audio\\welcome_sir_1_sec.mp3"
    playsound(music_dir)