import tkinter as tk
from tktooltip import ToolTip
import re

#coordinates for tkinter elements on 24x24 grid. list element 0 is column, list element 1 is row
sine_text_label_coords=[0,14]
sine_button_coords=[0,15]

triangle_text_label_coords=[1,14]
triangle_button_coords=[1,15]

square_text_label_coords=[2,14]
square_button_coords=[2,15]

sawtooth_text_label_coords=[3,14]
sawtooth_button_coords=[3,15]

key_text_box_coords = [0,18]
key_label_coords = [0,19]

freq_text_box_coords =[1,18]
freq_label_coords = [1,19]

tkm_button_coords =[0,21]
tkm_label_coords =[0,22]

tt_button_coords =[0,23]
tt_label_coords =[0,24]

play_button_coords =[6,23]
ready_button_coords =[5,23]
sound_ready_label_coords = [4,23]
sound_ready_oval_coords = [4,22]


dict_of_tooltips = {}
dict_of_oscillator_buttons= {}
array_oscillator_button_names = ["sw_button",
                                 "tw_button",
                                 "sq_button",
                                 "saw_button"]


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

def update_toggle_state(root,canvas,button_state, osc_update = True):
    """
    Method used for changing the state of the buttons between True and False. Calls
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

    if canvas.winfo_name() in array_oscillator_button_names and osc_update:
        update_wave_selection(root, canvas)

def toggle_tool_tips(root, event_status):
    """Toggles the tool tips on and off"""
    on = event_status.get()
    for name, tooltip in dict_of_tooltips.items():
        if on:
            tooltip.delay = 0
        else:
            tooltip.delay = 99999

def update_wave_selection(root, canvas):
    """Toggles the old oscillator off when a new one is selected"""
    for name, oscillator_button_group in dict_of_oscillator_buttons.items():
        cur_state = oscillator_button_group["state"].get()
        if not oscillator_button_group["button"] == canvas and cur_state:
            state = oscillator_button_group["state"]
            cur_canvas = oscillator_button_group["button"]
            update_toggle_state(root, cur_canvas, state, False)
            break





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

    #create the ready button frame and button widget
    ready_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE", name= "ready_frame")
    ready_frame.grid(row = ready_button_coords[1], column = ready_button_coords[0])

    ready_button = tk.Button(ready_frame, text="Ready", font=("inter", 16, "bold"), fg="#1539EE",
                             bg="#333333", relief="flat", name="ready_button",
                             activebackground="#333333", activeforeground="#1539EE")
    ready_button.grid(row = ready_button_coords[1], column = ready_button_coords[0])

    #create the blue frame for the play button
    play_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE", name="play_frame")
    play_frame.grid(row=play_button_coords[1], column=play_button_coords[0])

    #create the play button widget
    play_button = tk.Button(play_frame, text= "Play", font= ("inter", 16, "bold"),
                            fg="#1539EE", bg="#333333", relief="flat", name="play_button",
                            activebackground= "#333333", activeforeground="#1539EE")
    play_button.grid(row=play_button_coords[1], column=play_button_coords[0])

    #create the sine wave toggle button
    sw_state = tk.BooleanVar(value=True)

    sw_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name="sw_frame")
    sw_frame.grid(row=sine_button_coords[1], column=sine_button_coords[0])

    sw_canvas = tk.Canvas(sw_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="sw_button")
    sw_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    sw_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(event, sw_canvas,sw_state))

    update_toggle_color(sw_canvas, sw_state)

    #add the sine wave state and canvas button to the dict of oscillator buttons
    dict_of_oscillator_buttons["sine_wave_button_group"] = {}
    dict_of_oscillator_buttons["sine_wave_button_group"]["button"] = sw_canvas
    dict_of_oscillator_buttons["sine_wave_button_group"]["state"] = sw_state
    dict_of_oscillator_buttons["sine_wave_button_group"]["name"] = "sine"

    #create the triangle wave toggle button
    tw_state = tk.BooleanVar(value=False)
    tw_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name="tw_frame")
    tw_frame.grid(row= triangle_button_coords[1], column=triangle_button_coords[0])

    tw_canvas = tk.Canvas(tw_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="tw_button")
    tw_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    tw_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(event, tw_canvas,tw_state))

    update_toggle_color(tw_canvas, tw_state)

    #add the triangle wave state and canvas button to the dict of oscillator buttons
    dict_of_oscillator_buttons["triangle_button_group"] = {}
    dict_of_oscillator_buttons["triangle_button_group"]["button"] = tw_canvas
    dict_of_oscillator_buttons["triangle_button_group"]["state"] = tw_state
    dict_of_oscillator_buttons["triangle_button_group"]["name"] = "triangle"

    #create the square wave toggle button
    sqw_state = tk.BooleanVar(value=False)
    sqw_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name="sqw_frame")
    sqw_frame.grid(row=square_button_coords[1], column=square_button_coords[0])

    sqw_canvas = tk.Canvas(sqw_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="sq_button")
    sqw_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    sqw_canvas.bind("<Button-1>",
                    lambda event: update_toggle_state(event, sqw_canvas,sqw_state))

    update_toggle_color(sqw_canvas, sqw_state)

    #add the square wave state and canvas button the dict of oscillator buttons
    dict_of_oscillator_buttons["square_button_group"] = {}
    dict_of_oscillator_buttons["square_button_group"]["button"] = sqw_canvas
    dict_of_oscillator_buttons["square_button_group"]["state"] = sqw_state
    dict_of_oscillator_buttons["square_button_group"]["name"] = "square"

    #create the saw wave toggle button
    saww_state = tk.BooleanVar(value=False)
    saww_frame= tk.Frame(main_window, borderwidth=0, bg="#333333", name="saww_frame")
    saww_frame.grid(row= sawtooth_button_coords[1], column=sawtooth_button_coords[0])

    saww_canvas = tk.Canvas(saww_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="saw_button")
    saww_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    saww_canvas.bind("<Button-1>",
                     lambda event: update_toggle_state(event, saww_canvas,saww_state))

    update_toggle_color(saww_canvas, saww_state)

    #add the saw wave button group to the dict of oscillator buttons
    dict_of_oscillator_buttons["sawtooth_button_group"] = {}
    dict_of_oscillator_buttons["sawtooth_button_group"]["button"] = saww_canvas
    dict_of_oscillator_buttons["sawtooth_button_group"]["state"] = saww_state
    dict_of_oscillator_buttons["sawtooth_button_group"]["name"] = "saw"




    #create SIN wave label
    sw_label = tk.Label(main_window, text="SIN", fg="#1539EE", bg="#333333",
                        font=("inter", 12, "bold"), name="sw_text_label")
    sw_label.grid(row=sine_text_label_coords[1], column=sine_text_label_coords[0], sticky="n")

    #create TRI wave label
    tri_text_label = tk.Label(main_window, text="TRI", fg="#1539EE", bg="#333333",
                        font=("inter", 12, "bold"), name="tri_text_label")
    tri_text_label.grid(row=triangle_text_label_coords[1], column=triangle_text_label_coords[0], sticky="n")

    #create SQR wave label
    sqr_text_label = tk.Label(main_window, text="SQR", fg="#1539EE", bg="#333333",
                        font=("inter", 12, "bold"), name="sqr_text_label")
    sqr_text_label.grid(row=square_text_label_coords[1], column=square_text_label_coords[0], sticky="n")

    #create SAW wave label
    saw_text_label = tk.Label(main_window, text="SAW", fg="#1539EE", bg="#333333",
                        font=("inter", 12, "bold"), name="saw_text_label")
    saw_text_label.grid(row=sawtooth_text_label_coords[1], column=sawtooth_text_label_coords[0], sticky="n")

    #create the tool tips toggle button
    tt_state = tk.BooleanVar(value=True)

    tt_frame= tk.Frame(main_window, borderwidth=0, bg="#333333", name="tt_frame")
    tt_frame.grid(row=tt_button_coords[1], column=tt_button_coords[0],pady=(0,2), sticky="s")

    tt_canvas = tk.Canvas(tt_frame, width=20, height=20, bg="#333333", highlightthickness=0,
                          name="tt_button")
    tt_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    tt_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(main_window,tt_canvas,tt_state))

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
                    lambda event: update_toggle_state(main_window,tkm_canvas,tkm_state))

    update_toggle_color(tkm_canvas,tkm_state)

    tkm_title = tk.Label(main_window, text= "Toggle Key Matching", bg="#333333", fg="#1539EE",
                         font=("inter", 8, "bold"), name="tkm_title")
    tkm_title.grid(row=tkm_label_coords[1], column=tkm_label_coords[0], sticky="n")

    #create the sound ready label and oval
    sound_ready_title = tk.Label(main_window, text="Sound Ready", bg="#333333", fg="#1539EE",
                                 font=("inter", 8, "bold"), name="sound_ready_title")
    sound_ready_title.grid(row=sound_ready_label_coords[1], column=sound_ready_label_coords[0])

    sound_ready_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name = "sound_ready_frame")
    sound_ready_frame.grid(row = sound_ready_oval_coords[1], column = sound_ready_oval_coords[0], sticky = "s",
                           pady=(0,2))
    sound_ready_canvas = tk.Canvas(sound_ready_frame, width=20, height=20, bg="#333333", highlightthickness=0,
                                   name="sound_ready_oval")
    sound_ready_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    sound_ready_canvas.create_oval((5,5,15,15), fill= "white", outline= "white")

    return main_window

