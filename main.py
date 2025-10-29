#Jacob Durham
#CS 361 Software Engineering I Fall 2025

"""
Sources and references:

Description: Referenced for help deleting from a Key field tkinter widget when putting in a new value
Source URL: https://www.geeksforgeeks.org/python/how-to-clear-the-entry-widget-after-button-press-in-tkinter/
Date Accessed: 10/29/2025

Description: Referenced for help with getting a function to execute when the enter key is used
while the text box is selected.
Source URL: https://stackoverflow.com/questions/56702270/how-do-i-use-the-entry-widget-on-tkinter-to-execute-a-function-by-inputting-para
Date Accessed: 10/29/2025

Description: Referenced for help with moving files from one directory to another.
Source URL: https://stackoverflow.com/questions/8858008/how-do-i-move-a-file-in-python
Date Accessed: 10/29/2025

Description: Additional help with tkinter button lambda events that happen when the button is clicked.
Source URL: https://stackoverflow.com/questions/70406400/understanding-python-lambda-behavior-with-tkinter-button
Date Accessed: 10/29/2025

Description: Referenced for help with TKinter Entry widgets
Source URL: https://www.geeksforgeeks.org/python/python-tkinter-entry-widget/
Date Accessed: 10/29/2025

Description: Referenced for help with Tkinter button attributes
Source URL: https://www.tutorialspoint.com/python/tk_button.htm
Date Accessed: 10/28/2025

Description: Referenced for help with winsound
Source URL:https://docs.python.org/3/library/winsound.html
Date Accessed: 10/26/2025

Description: Referenced for help with Abstract Base Classes
Source URL:https://www.geeksforgeeks.org/python/abstract-classes-in-python/
Date Accessed: 10/26/2025

Description: Code for creating Oscillator ABC, Sine Oscillator, Triangle Oscillator, Square Oscillator, 
Saw Oscillator, and wave_adder, copied and adapted from
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

#coordinates for UI images. Element 0 is column, element 1 is row
sine_img_coords = [0,13]
tri_img_coords = [1,13]
sqr_img_coords = [2,13]
saw_img_coords = [3,13]

ui = create_ui()

# create Sine wave image
sine_wave_img = PhotoImage(file=r"images/sine_wave.png")
sine_img_label = tk.Label(ui, image=sine_wave_img,highlightthickness=0, bg="#333333")
sine_img_label.grid(row=sine_img_coords[1], column=sine_img_coords[0])

#create the triangle wave image
tri_wave_img = PhotoImage(file=r"images/triangle_wave.png")
tri_img_label = tk.Label(ui, image=tri_wave_img,highlightthickness=0, bg="#333333")
tri_img_label.grid(row=tri_img_coords[1], column=tri_img_coords[0])

#create the square wave image
sqr_wave_img = PhotoImage(file=r"images/square_wave.png")
sqr_img_label = tk.Label(ui, image=sqr_wave_img,highlightthickness=0, bg="#333333")
sqr_img_label.grid(row=sqr_img_coords[1], column=sqr_img_coords[0])

#create the saw wave image
saw_wave_img = PhotoImage(file=r"images/saw_wave.png")
saw_img_label = tk.Label(ui, image=saw_wave_img,highlightthickness=0, bg="#333333")
saw_img_label.grid(row=saw_img_coords[1], column=saw_img_coords[0])

ui.mainloop()
