import tkinter as tk
from idlelib.configdialog import font_sample_text
from tkinter import PhotoImage

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

    canvas.create_oval(coordinates, fill=fill_color, outline=fill_color)

def update_toggle_state(event, canvas,button_state):
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
    # main_window.rowconfigure(25, weight=1)
    # for row in range(rows):
    #     main_window.rowconfigure(row, weight=1)

    #create the text entry for key
    key_field = tk.Entry(main_window, width=8, justify="center", font=("inter", 10, "bold"))
    key_field.grid(row=18, column=1, sticky="n", pady=(0,2))
    key_field.insert(0, "C4")

    #create the UI title for the key text entry
    key_field_label = tk.Label(main_window, text="Key", bg="#333333",fg="#1539EE", font=("inter", 12, "bold"))
    key_field_label.grid(row=19, column=1, sticky="n")


    #create the text entry for frequency
    freq_field = tk.Entry(main_window, width=8, justify="center",font=("inter", 10, "bold"))
    freq_field.grid(row=18, column=2, sticky="n", pady=(0,2))
    freq_field.insert(0, "261.63")

    #create UI title for frequency text entry
    frequency_field_label = tk.Label(main_window, text = "Frequency\n(Hz)", bg="#333333",fg="#1539EE", font=("inter", 12, "bold"))
    frequency_field_label.grid(row=19, column=2, sticky="n")

    #create the blue frame for the play button
    play_frame = tk.Frame(main_window, borderwidth=3, bg="#1539EE")
    play_frame.grid(row=23, column=10)

    #create the play button widget
    play_button = tk.Button(play_frame, text= "Play", font= ("inter", 16, "bold"), fg="#1539EE", bg="#333333", relief="flat")
    play_button.grid(row=23, column=10)

    #create the sine wave toggle buttom
    sw_state = tk.BooleanVar(value=True)

    sw_frame = tk.Frame(main_window, borderwidth=0, bg="#333333")
    sw_frame.grid(row=16, column=2)

    sw_canvas = tk.Canvas(sw_frame, width=20, height=20, highlightthickness=0, bg="#333333")
    sw_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(5,5))
    sw_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(event, sw_canvas,sw_state))

    update_toggle_color(sw_canvas,sw_state)
    #create the tool tips toggle button
    tt_state = tk.BooleanVar(value=True)

    tt_frame= tk.Frame(main_window, borderwidth=0, bg="#333333")
    tt_frame.grid(row=23, column=0,pady=(0,2), sticky="s")

    tt_canvas = tk.Canvas(tt_frame, width=20, height=20, bg="#333333", highlightthickness=0)
    tt_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    tt_canvas.bind("<Button-1>",
                   lambda event: update_toggle_state(event,tt_canvas,tt_state))

    update_toggle_color(tt_canvas,tt_state)

    tt_title = tk.Label(main_window, text="Toggle Tooltips", bg="#333333", fg="#1539EE", font=("inter", 8, "bold"))
    tt_title.grid(row=24, column=0, sticky="n")

    #create the toggle key matching button
    tkm_state = tk.BooleanVar(value=True)

    tkm_frame = tk.Frame(main_window, borderwidth=0, bg="#333333")
    tkm_frame.grid(row=21, column=0, pady=(0,2), sticky="s")

    tkm_canvas = tk.Canvas(tkm_frame, width=20, height=20, bg="#333333", highlightthickness=0)
    tkm_canvas.pack(side=tk.LEFT, padx=(5,5), pady=(0,2))
    tkm_canvas.bind("<Button-1>",
                    lambda event: update_toggle_state(event,tkm_canvas,tkm_state))

    update_toggle_color(tkm_canvas,tkm_state)

    tkm_title = tk.Label(main_window, text= "Toggle Key Matching", bg="#333333", fg="#1539EE", font=("inter", 8, "bold"))
    tkm_title.grid(row=22, column=0, sticky="n")



    return main_window

