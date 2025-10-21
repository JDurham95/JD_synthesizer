import tkinter as tk
from tktooltip import ToolTip
import re

#coordinates for tkinter elements on 24x24 grid. list element 0 is column, list element 1 is row
sine_label_coords=[0,14]
sine_button_coords=[0,15]

key_text_box_coords = [0,18]
key_label_coords = [0,19]

freq_text_box_coords =[1,18]
freq_label_coords = [1,19]

tkm_button_coords =[0,21]
tkm_label_coords =[0,22]

tt_button_coords =[0,23]
tt_label_coords =[0,24]

play_button_coords =[10,23]

dict_of_tooltips = {}


def update_toggle_color(canvas,button_state):
    """method used for changing the button color on the tool tips toggle"""
    canvas.delete("all")
    is_on = button_state.get()

    button_radius, center = 5, 10
    coordinates = (center - button_radius, center - button_radius,
                   center + button_radius, center + button_radius)

    if is_on:
        fill_color = "#1539EE"
    else:
        fill_color = "white"

    canvas.create_oval(coordinates, fill=fill_color, outline="white", )

def update_toggle_state(root, event, canvas,button_state):
    """
    Method used for changing the state of the tool tips toggle between True and False. Calls
    the update_tt_color function
    """
    is_on = button_state.get()

    if is_on:
        button_state.set(False)
    else:
        button_state.set(True)

    update_toggle_color(canvas,button_state)
    if canvas.winfo_name() == "tt_button":
        toggle_tool_tips(root, button_state)


def toggle_tool_tips(root, event_status):
    """Toggles the tool tips on and off"""
    on = event_status.get()
    for name, tooltip in dict_of_tooltips.items():
        if on:
            tooltip.delay = 0
        else:
            tooltip.delay = 99999


def create_ui():
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



    main_window.rowconfigure(1, weight=1)
    main_window.rowconfigure(17, weight=1)
    main_window.rowconfigure(20, weight=1)

    # main_window.rowconfigure(25, weight=1)
    # for row in range(rows):
    #     main_window.rowconfigure(row, weight=1)

    #create the text entry for key
    key_field = tk.Entry(main_window, width=8, justify="center", font=("inter", 10, "bold"), name="key_field")
    key_field.grid(row=key_text_box_coords[1], column=key_text_box_coords[0], sticky="n", pady=(0,2))
    key_field.insert(0, "C4")

    #create the UI title for the key text entry
    key_field_label = tk.Label(main_window, text="Key", bg="#333333",fg="#1539EE",
                               font=("inter", 12, "bold"), name="key_field_label")
    key_field_label.grid(row=key_label_coords[1], column=key_label_coords[0], sticky="n")

    #create tool tip for key text entry and button
    dict_of_tooltips["key_field_tt"] = ToolTip(key_field, msg="Enter a key here (A0 - C8)", delay= 2, name="key_field_tt")
    dict_of_tooltips["key_label_tt"] = ToolTip(key_field_label, msg="Enter a key here (A0 - C8)", delay=2,
                                               name="key_label_tt")


    #create the text entry for frequency
    freq_field = tk.Entry(main_window, width=8, justify="center",font=("inter", 10, "bold"), name="freq_field")
    freq_field.grid(row=freq_text_box_coords[1], column=freq_text_box_coords[0], sticky="n", pady=(0,2))
    freq_field.insert(0, "261.63")


    #create UI title for frequency text entry
    frequency_field_label = tk.Label(main_window, text = "Frequency\n(Hz)", bg="#333333",fg="#1539EE",
                                     font=("inter", 12, "bold"), name="freq_field_label")
    frequency_field_label.grid(row=freq_label_coords[1], column=freq_label_coords[0], sticky="n")

    #create

    #create the blue frame for the play button
    play_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE", name="play_frame")
    play_frame.grid(row=play_button_coords[1], column=play_button_coords[0])

    #create the play button widget
    play_button = tk.Button(play_frame, text= "Play", font= ("inter", 16, "bold"),
                            fg="#1539EE", bg="#333333", relief="flat", name="play_button")
    play_button.grid(row=play_button_coords[1], column=play_button_coords[0])

    #create the sine wave toggle button
    sw_state = tk.BooleanVar(value=True)

    sw_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name="sw_frame")
    sw_frame.grid(row=sine_button_coords[1], column=sine_button_coords[0])

    sw_canvas = tk.Canvas(sw_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="sw_button")
    sw_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    sw_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(event, sw_canvas,sw_state))

    update_toggle_color(sw_canvas,sw_state)

    #create SINE wave label
    sw_label = tk.Label(main_window, text="SINE", fg="#1539EE", bg="#333333",
                        font=("inter", 12, "bold"), name="sw_label")
    sw_label.grid(row=sine_label_coords[1], column=sine_label_coords[0], sticky="n")

    #create the tool tips toggle button
    tt_state = tk.BooleanVar(value=True)

    tt_frame= tk.Frame(main_window, borderwidth=0, bg="#333333", name="tt_frame")
    tt_frame.grid(row=tt_button_coords[1], column=tt_button_coords[0],pady=(0,2), sticky="s")

    tt_canvas = tk.Canvas(tt_frame, width=20, height=20, bg="#333333", highlightthickness=0,
                          name="tt_button")
    tt_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    tt_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(main_window,event,tt_canvas,tt_state))

    update_toggle_color(tt_canvas,tt_state)

    tt_title = tk.Label(main_window, text="Toggle Tooltips", bg="#333333", fg="#1539EE",
                        font=("inter", 8, "bold"), name="tt_title")
    tt_title.grid(row=tt_label_coords[1], column=tt_label_coords[0], sticky="n")

    #create the toggle key matching button
    tkm_state = tk.BooleanVar(value=True)

    tkm_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name="tkm_frame")
    tkm_frame.grid(row=tkm_button_coords[1], column=tkm_button_coords[0], pady=(0,2), sticky="s")

    tkm_canvas = tk.Canvas(tkm_frame, width=20, height=20, bg="#333333", highlightthickness=0,
                            name="tkm_button")
    tkm_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    tkm_canvas.bind("<Button-1>",
                    lambda event: update_toggle_state(main_window, event,tkm_canvas,tkm_state))

    update_toggle_color(tkm_canvas,tkm_state)

    tkm_title = tk.Label(main_window, text= "Toggle Key Matching", bg="#333333", fg="#1539EE",
                         font=("inter", 8, "bold"), name="tkm_title")
    tkm_title.grid(row=tkm_label_coords[1], column=tkm_label_coords[0], sticky="n")

    return main_window

