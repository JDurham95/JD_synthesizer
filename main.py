#Jacob Durham
#CS 361 Software Engineering I Fall 2025

"""
Sources and references:

Description: Referenced tutorial on TKinter grid and widget spacing
Source URL: https://www.activestate.com/resources/quick-reads/how-to-position-widgets-in-tkinter/
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
from tkinter import ttk

def update_tt_color(canvas,button_state):
    """method used for changing the button color on the tool tips toggle"""
    canvas.delete("all")
    is_on = button_state.get()

    button_radius, center = 8, 10
    coordinates = (center - button_radius, center - button_radius,
                   center + button_radius, center + button_radius)

    if is_on:
        fill_color = "#1539EE"
    else:
        fill_color = "white"

    canvas.create_oval(coordinates, fill=fill_color, outline=fill_color)

def update_tt_state(event, canvas,button_state):
    """
    Method used for changing the state of the tool tips toggle between True and False. Calls
    the update_tt_color function
    """
    is_on = button_state.get()

    if is_on:
        button_state.set(False)
    else:
        button_state.set(True)

    update_tt_color(canvas,button_state)


#Establish the main synth window
main_window = tk.Tk()
main_window.title("JDsynth")
main_window.config(bg="#333333")
main_window.geometry("1200x400")
main_window.resizable(False, False)

columns = 24
rows = 24

for column in range(columns):
    main_window.columnconfigure(column, weight=1)

for row in range(rows):
    main_window.rowconfigure(row, weight=1)

#create the text entry for key
key_field = tk.Entry(main_window, width=8, justify="center")
key_field.grid(row=18, column=1)
key_field.insert(0, "C4")

#create the UI title for the key text entry
key_field_label = tk.Label(main_window, text="Key", bg="#333333",fg="#1539EE", font=("inter", 12, "bold"))
key_field_label.grid(row=19, column=1)


#create the text entry for frequency
freq_field = tk.Entry(main_window, width=8, justify="center")
freq_field.grid(row=18, column=2)
freq_field.insert(0, "261.63")

#create UI title for frequency text entry
frequency_field_label = tk.Label(main_window, text = "Frequency\n(Hz)", bg="#333333",fg="#1539EE", font=("inter", 12, "bold"))
frequency_field_label.grid(row=19, column=2)

#create the blue fram for the play button
play_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE")
play_frame.grid(row=23, column=10)

#create the play button widget
play_button = tk.Button(play_frame, text= "Play", font= ("inter", 16, "bold"), fg="#1539EE", bg="#333333", relief="flat")
play_button.grid(row=23, column=10)

#create the tool tips toggle button
tt_state = tk.BooleanVar(value=False)

tt_frame= tk.Frame(main_window, borderwidth=0, bg="#333333")
tt_frame.grid(row=23, column=0)

tt_canvas = tk.Canvas(tt_frame, width=20, height=20, bg="#333333", highlightthickness=0)
tt_canvas.pack(side=tk.LEFT)
tt_canvas.bind("<Button-1>",
               lambda event: update_tt_state(event,tt_canvas,tt_state))

update_tt_color(tt_canvas,tt_state)

tt_title = tk.Label(main_window, text="Toggle Tooltips", bg="#333333", fg="#1539EE", font=("inter", 12, "bold"))
tt_title.grid(row=24, column=0)

main_window.mainloop()