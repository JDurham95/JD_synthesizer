
from oscillators.sine_osc import SineOscillator
from oscillators.triangle_osc import TriangleOscillator
from oscillators.square_osc import SquareOscillator
from oscillators.saw_osc import SawOscillator
from sound_methods.wav_to_file import wav_to_file
import os



def ready_sound(frequency, amplitude, osc_name):
    """readies a sound for playing"""

    frequency = int(frequency)
    amplitude = float(amplitude) / 100

    if osc_name == "sine":
        generator = SineOscillator(frequency, amplitude)
        iter(generator)
        wav = [next(generator) for _ in range(44100 * 4)]
        wav_to_file(wav)

    if osc_name == "triangle":
        generator = TriangleOscillator(frequency, amplitude)
        iter(generator)
        wav = [next(generator) for _ in range(44100 * 4)]
        wav_to_file(wav)

    if osc_name == "saw":
        generator = SawOscillator(frequency, amplitude)
        iter(generator)
        wav = [next(generator) for _ in range(44100 * 4)]
        wav_to_file(wav)

    if osc_name == "square":
        generator = SquareOscillator(frequency, amplitude)
        iter(generator)
        wav = [next(generator) for _ in range(44100 * 4)]
        wav_to_file(wav)

    if os.path.exists("sounds/temp.wav"):
        os.remove("sounds/temp.wav")

    os.rename("temp.wav", "sounds/temp.wav")

