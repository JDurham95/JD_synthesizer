#Jacob Durham
#CS 361 Software Engineering I Fall 2025

from sine_osc import SineOscillator
from wav_to_file import wav_to_file
import itertools
import winsound
from wave_adder import WaveAdder


"""
Sources and references:

Description: Referenced for help with winsound
Source URL:https://docs.python.org/3/library/winsound.html
Date Accessed: 10/26/2025

Description: Referenced for help with Abstract Base Classes
Source URL:https://www.geeksforgeeks.org/python/abstract-classes-in-python/
Date Accessed: 10/26/2025

Description: Code for creating the sine oscillator adapted from
Source URL:https://python.plainenglish.io/making-a-synth-with-python-oscillators-2cb8e68e9c3b
Date Accessed: 10/26/2025

Description: Referenced for creating tool tips in the tkinter UI
Source URL: https://pypi.org/project/TkToolTip/
Date Accessed: 10/20/2025

Description: Referenced for help with Tkinter sticky attribute
Source URL: https://www.tutorialspoint.com/python/tk_grid.htm
Date Accessed: 10/19/2025

Description: Referenced tutorial on TKinter grid and widget spacing
Source URL: https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
Date Accessed: 10/19/2025

Description: Referenced when images I was importing were not displaying properly
Source URL: https://www.reddit.com/r/Tkinter/comments/q6wv2x/why_are_the_pictures_displayed_just_white/
Date Accessed: 10/19/2025

Description: Source of key numbers and frequencies for A0 - C8
Source URL: https://en.wikipedia.org/wiki/Piano_key_frequencies#/media/File:Piano_key_frequencies.png
Date Accessed: 10/19/2025

Description: Code for creating Tkinter frames
Source URL: https://www.pythonguis.com/tutorials/use-tkinter-to-design-gui-layout/
Date Accessed: 10/19/2025

Description: Code for creating Tkinter labels
Source URL: https://www.geeksforgeeks.org/python/python-tkinter-label/
Date Accessed: 10/19/2025

Description: Code for changing the BG color of Tkinter windows
Source URL: https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python
Date Accessed: 10/19/2025

Description: Code for creating/ handling events using lambda in tkinter
Source URL: https://www.geeksforgeeks.org/python/using-lambda-in-gui-programs-in-python/
Date Accessed: 10/19/2025

Description: Code for changing TKinter button colors after use
Source URL: https://www.geeksforgeeks.org/python/change-color-of-button-in-python-tkinter/
Date Accessed: 10/19/2025
"""

import tkinter as tk
from tkinter import PhotoImage
from UI import create_ui

# ui = create_ui()
#
# # create Sine wave image
# sine_wave_img = PhotoImage(file=r"images/sine_wave.png")
# sine_wave_label = tk.Label(ui, image=sine_wave_img,highlightthickness=0, bg="#333333")
# sine_wave_label.grid(row=13, column=0,)
#
# ui.mainloop()

gen = SineOscillator(frequency=440)
iter(gen)
wav = [next(gen) for _ in range (44100 * 4)]
wav_to_file(wav)

winsound.PlaySound("temp.wav", winsound.SND_FILENAME)