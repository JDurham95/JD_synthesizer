import winsound
from sound_methods.ready_sound import ready_sound

def play_sound(frequency, amplitude, osc_name, duration):

    ready_sound(frequency, amplitude, osc_name, duration)
    winsound.PlaySound("sounds/temp.wav", winsound.SND_FILENAME)



