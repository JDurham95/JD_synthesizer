import tkinter as tk
from tktooltip import ToolTip
from sound_methods.ready_sound import ready_sound
from sound_methods.key_to_freq import key_to_freq
from sound_methods.freq_to_key import freq_to_key
from sound_methods.play_sound import play_sound
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

duration_text_box_coords = [2,18]
duration_label_coords = [2,19]

amp_text_box_coords = [3,18]
amp_label_coords = [3,19]

tkm_button_coords =[0,21]
tkm_label_coords =[0,22]

tt_button_coords =[0,23]
tt_label_coords =[0,24]

play_button_coords =[6,23]
ready_button_coords =[5,23]
sound_ready_label_coords = [4,23]
sound_ready_oval_coords = [4,22]

reset_button_coords = [1,23]


dict_of_tooltips = {}
dict_of_oscillator_buttons= {}
array_oscillator_button_names = ["sw_button",
                                 "tw_button",
                                 "sq_button",
                                 "saw_button"]
dict_of_fields= {}
dict_of_settings_buttons= {}


def amplitude_enter_function(event = None):
    """Happens when the return key is pressed after a new amplitude has been entered."""
    field_obj = dict_of_fields["amp_field"]
    amp_val = field_obj.get()

    if not amp_val.isdigit():
        amp_val = "100"
    else:
        amp_val = int(amp_val)
        if amp_val > 100:
            amp_val = "100"
        elif amp_val < 0:
            amp_val = "0"
    field_obj.delete(0, tk.END)
    field_obj.insert(0, str(amp_val))

    field_obj.master.focus_set()

def key_enter_function(event = None):
    """happens when the return key is pressed after a new key has been entered. """
    field_obj = dict_of_fields["key_field"]
    key_val = field_obj.get()
    key_val = key_val.upper()
    freq_field = dict_of_fields["freq_field"]

    pattern_a = r"^[a-gA-G][#]?[0-8]$"
    if not re.fullmatch(pattern_a, key_val):
        field_obj.delete(0, tk.END)
        field_obj.insert(0, "N/a")

        freq_field.delete(0, tk.END)
        freq_field.insert(0, "N/a")
        field_obj.master.focus_set()
        return

    new_freq = key_to_freq(key_val)

    if new_freq:
        freq_field.delete(0, tk.END)
        freq_field.insert(0,str(new_freq))

        field_obj.delete(0, tk.END)
        field_obj.insert(0, key_val)
    else:
        freq_field.delete(0,tk.END)
        freq_field.insert(0,"261")

        field_obj.delete(0, tk.END)
        field_obj.insert(0, "C4")

    field_obj.master.focus_set()

def frequency_enter_function(event = None):
    """happens when the return key is pressed after a new frequency has been entered. """
    field_obj = dict_of_fields["freq_field"]
    freq_val = int(field_obj.get())
    tkm_obj = dict_of_settings_buttons["tkm_state"]
    tkm_val = tkm_obj.get()
    key_field = dict_of_fields["key_field"]

    if tkm_val:
        key_freq_pair = freq_to_key(freq_val)
        key_val = key_freq_pair[0]
        key_field.delete(0, tk.END)
        key_field.insert(0,str(key_val))
        field_obj.delete(0,tk.END)
        field_obj.insert(0,str(key_freq_pair[1]))
    else:
        field_obj.delete(0,tk.END)
        field_obj.insert(0,str(freq_val))
        key_field.delete(0,tk.END)
        key_field.insert(0,"N/a")

    field_obj.master.focus_set()

def duration_enter_function(event = None):
    field_obj = dict_of_fields["dur_field"]
    dur_val = field_obj.get()

    if not dur_val.isdigit():
        dur_val = "2"

    dur_val = int(dur_val)

    if dur_val < 1:
        field_obj.delete(0,tk.END)
        field_obj.insert(0,"1")
    elif dur_val > 10:
        field_obj.delete(0,tk.END)
        field_obj.insert(0,"10")
    else:
        field_obj.delete(0,tk.END)
        field_obj.insert(0,str(dur_val))

    field_obj.master.focus_set()


def get_active_osc():
    """Returns the oscillator that is currently active"""
    for name, button in dict_of_oscillator_buttons.items():
        if button["state"].get():
            return button["name"]
    return -1


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
            tooltip.delay = 2
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


def reset(root,event =None):
    """Resets the synth to the default parameters"""

    update_toggle_state(root,dict_of_oscillator_buttons["sine_wave_button_group"]["button"],
                        dict_of_oscillator_buttons["sine_wave_button_group"]["state"])


    field_obj = dict_of_fields["amp_field"]
    amp_val = "100"
    field_obj.delete(0,tk.END)
    field_obj.insert(0,amp_val)

    field_obj = dict_of_fields["dur_field"]
    dur_val = "2"
    field_obj.delete(0,tk.END)
    field_obj.insert(0,dur_val)

    field_obj = dict_of_fields["key_field"]
    key_val = "C4"
    field_obj.delete(0,tk.END)
    field_obj.insert(0,key_val)

    field_obj.master.focus_set()

    key_enter_function(None)

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
    key_field.bind("<Return>", lambda event: key_enter_function(event))

    dict_of_fields["key_field"] = key_field

    #create the UI title for the key text entry
    key_field_label = tk.Label(main_window, text="Key", bg="#333333",fg="#1539EE",
                               font=("inter", 12, "bold"), name="key_field_label")
    key_field_label.grid(row=key_label_coords[1], column=key_label_coords[0], sticky="n")

    #create tool tip for key text entry and button
    dict_of_tooltips["key_field_tt"] = ToolTip(key_field, msg="Enter a key here (A0 - C8)", delay= 2, name="key_field_tt")
    dict_of_tooltips["key_label_tt"] = ToolTip(key_field_label, msg="Enter a key here (A0 - C8). Type a new key and use"
                                                                    "the return key.", delay=2,
                                               name="key_label_tt")


    #create the text entry for frequency
    freq_field = tk.Entry(main_window, width=8, justify="center",font=("inter", 10, "bold"), name="freq_field")
    freq_field.grid(row=freq_text_box_coords[1], column=freq_text_box_coords[0], sticky="n", pady=(0,2))
    freq_field.insert(0, "261")
    freq_field.bind("<Return>", lambda event: frequency_enter_function(event))

    dict_of_fields["freq_field"] = freq_field

    #create label for frequency text entry
    frequency_field_label = tk.Label(main_window, text = "Frequency\n(Hz)", bg="#333333",fg="#1539EE",
                                     font=("inter", 12, "bold"), name="freq_field_label")
    frequency_field_label.grid(row=freq_label_coords[1], column=freq_label_coords[0], sticky="n")

    #create the tool tips for the frequency widgets
    dict_of_tooltips["freq_field_tt"] = ToolTip(freq_field, msg="Enter a frequency here (28 Hz - 4186 Hz). Type a new "
                                                                "frequency and use the return key. Frequencies outside "
                                                                "of the normal range may not produce a sound.", delay=2)
    dict_of_tooltips["freq_label_tt"] = ToolTip(frequency_field_label, msg="Enter a frequency here (28 Hz - 4186 Hz). Type a new "
                                                                "frequency and use the return key. Frequencies outside "
                                                                "of the normal range may not produce a sound.", delay=2)

    #create the amplitude text entry label
    amp_field_label = tk.Label(main_window, text="Amplitude", bg="#333333",fg="#1539EE",
                               font=("inter", 12, "bold"), name="amp_field_label")
    amp_field_label.grid(row=amp_label_coords[1], column=amp_label_coords[0], sticky="n")

    #create the text entry for amplitude
    amp_field = tk.Entry(main_window, width=8, justify="center", name="amp_field",
                         font=("inter", 10, "bold"))
    amp_field.grid(row = amp_text_box_coords[1], column = amp_text_box_coords[0], sticky="n")
    amp_field.insert(0, "100")
    amp_field.bind("<Return>", lambda event: amplitude_enter_function(event))

    dict_of_fields["amp_field"] = amp_field

    #create the tool tips for the amplitude widgets
    dict_of_tooltips["amp_field_tt"] = ToolTip(amp_field, msg="Enter a amplitude value here (0 - 100). Type a new value "
                                                              "and then use the return key. A value of "
                                                              "0 will not produce a sound.", delay=2)
    dict_of_tooltips["amp_label_tt"] = ToolTip(amp_field_label, msg="Enter a amplitude value here (0 - 100). Type a new "
                                                                    "value and then use the return key. A value of "
                                                              "0 will not produce a sound.", delay=2)

    #create the duration text entry label
    dur_field_label = tk.Label(main_window, text="Duration\n(s)", bg="#333333",fg="#1539EE",
                               font=("inter", 12, "bold"), name="dur_field_label")
    dur_field_label.grid(row=duration_label_coords[1], column=duration_label_coords[0], sticky="n")

    #create the duration text entry
    dur_field = tk.Entry(main_window, width=8, justify="center", name="dur_field",
                         font=("inter", 10, "bold"))
    dur_field.grid(row=duration_text_box_coords[1], column = duration_text_box_coords[0], sticky="n")
    dur_field.insert(0, "2")
    dur_field.bind("<Return>", lambda event: duration_enter_function(event))

    dict_of_fields["dur_field"] = dur_field

    #create the tool tips for the duration widgets
    dict_of_tooltips["dur_field_tt"] = ToolTip(dur_field, msg="Enter a duration value here (1 - 10 seconds). Values "
                                                              "outside of that range are not allowed.", delay=2)
    dict_of_tooltips["dur_label_tt"] = ToolTip(dur_field_label, msg="Enter a duration value here (1 - 10 seconds). Values "
                                                              "outside of that range are not allowed.", delay=2)


    #create the sine wave toggle button
    sw_state = tk.BooleanVar(value=True)

    sw_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name="sw_frame")
    sw_frame.grid(row=sine_button_coords[1], column=sine_button_coords[0])

    sw_canvas = tk.Canvas(sw_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="sw_button")
    sw_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    sw_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(event, sw_canvas,sw_state))

    update_toggle_color(sw_canvas, sw_state)

    #create the tool tip for the sine wave widget
    dict_of_tooltips["sw_canvas_tt"] = ToolTip(sw_canvas, msg="Select the sine wave here. Only one wave may be selected"
                                                        " at a time.", delay=2)

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

    #create the tool tip for the triangle wave widgets here
    dict_of_tooltips["tw_canvas_tt"] = ToolTip(tw_canvas, msg="Select the triangle wave here. Only one wave may be selected"
                                                        " at a time.", delay=2)

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

    #create tool tip for the square wave widget
    # dict_of_tooltips["sqw_frame_tt"] = ToolTip(sqw_frame, msg="Select the square wave here. Only one wave be selected"
    #                                                     " at a time.")
    dict_of_tooltips["sqw_canvas_tt"] = ToolTip(sqw_canvas, msg="Select the square wave here. Only one wave may be "
                                                                "selected at a time.", delay=2)
    #create the saw wave toggle button
    saww_state = tk.BooleanVar(value=False)
    saww_frame= tk.Frame(main_window, borderwidth=0, bg="#333333", name="saww_frame")
    saww_frame.grid(row= sawtooth_button_coords[1], column=sawtooth_button_coords[0])

    saww_canvas = tk.Canvas(saww_frame, width=20, height=20, highlightthickness=0, bg="#333333", name="saw_button")
    saww_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    saww_canvas.bind("<Button-1>",
                     lambda event: update_toggle_state(event, saww_canvas,saww_state))

    update_toggle_color(saww_canvas, saww_state)

    #create the tool tips for the saw wave widget
    dict_of_tooltips["saww_canvas_tt"] = ToolTip(saww_canvas, msg="Select the saw tooth wave here. Only one wave be "
                                                                  "selected at a time.", delay=2)

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
    dict_of_settings_buttons["tkm_state"] = tkm_state

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

    # #create the sound ready label and oval
    # sound_ready_title = tk.Label(main_window, text="Sound Ready", bg="#333333", fg="#1539EE",
    #                              font=("inter", 8, "bold"), name="sound_ready_title")
    # sound_ready_title.grid(row=sound_ready_label_coords[1], column=sound_ready_label_coords[0])
    #
    # sound_ready_frame = tk.Frame(main_window, borderwidth=0, bg="#333333", name = "sound_ready_frame")
    # sound_ready_frame.grid(row = sound_ready_oval_coords[1], column = sound_ready_oval_coords[0], sticky = "s",
    #                        pady=(0,2))
    # sound_ready_canvas = tk.Canvas(sound_ready_frame, width=20, height=20, bg="#333333", highlightthickness=0,
    #                                name="sound_ready_oval")
    # sound_ready_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    # sound_ready_canvas.create_oval((5,5,15,15), fill= "white", outline= "white")

    # #create the ready button frame and button widget
    # ready_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE", name= "ready_frame")
    # ready_frame.grid(row = ready_button_coords[1], column = ready_button_coords[0])
    #
    # ready_function = lambda :ready_sound(freq_field.get(),amp_field.get(), get_active_osc())
    #
    # ready_button = tk.Button(ready_frame, text="Ready", font=("inter", 16, "bold"), fg="#1539EE",
    #                          bg="#333333", relief="flat", name="ready_button",
    #                          activebackground="#333333", activeforeground="#1539EE", command=ready_function)
    # ready_button.grid(row = ready_button_coords[1], column = ready_button_coords[0])

    #create the blue frame for the play button
    play_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE", name="play_frame")
    play_frame.grid(row=play_button_coords[1], column=play_button_coords[0])

    play_function = lambda :play_sound(freq_field.get(),amp_field.get(),get_active_osc(), dur_field.get())

    #create the play button widget
    play_button = tk.Button(play_frame, text= "Play", font= ("inter", 16, "bold"),
                            fg="#1539EE", bg="#333333", relief="flat", name="play_button",
                            activebackground= "#333333", activeforeground="#1539EE",
                            command=play_function)
    play_button.grid(row=play_button_coords[1], column=play_button_coords[0])

    #create the tool tips for the play button and frame
    dict_of_tooltips["play_button"] = ToolTip(play_button, msg="Click here to play the sound with the current settings.",
                                              delay=2)
    dict_of_tooltips["play_frame"] = ToolTip(play_frame, msg="Click here to play the sound with the current settings.",
                                             delay=2)

    #create the reset button widget.
    reset_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE", name="reset_frame")
    reset_frame.grid(row=reset_button_coords[1], column=reset_button_coords[0])

    reset_function = lambda :reset(main_window)
    reset_button = tk.Button(reset_frame, text= "Reset", font= ("inter", 16, "bold"),
                             fg="#1539EE", bg="#333333", relief="flat", name="reset_button",
                             activebackground= "#333333", activeforeground="#1539EE",
                             command=reset_function)
    reset_button.grid(row=reset_button_coords[1], column=reset_button_coords[0])


    #create the tool tips for the reset button and frame
    dict_of_tooltips["reset_button"] = ToolTip(reset_button, msg="Click here to reset synthesizer to default settings. "
                                                                 "Warning! Resetting cannot be undone!", delay=2)
    dict_of_tooltips["reset_frame"] = ToolTip(reset_frame, msg="Click here to reset synthesizer to default settings."
                                                               "Warning! Resetting cannot be undone!", delay=2)

    return main_window

