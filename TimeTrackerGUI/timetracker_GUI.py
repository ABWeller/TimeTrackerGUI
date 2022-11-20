import timer
import tkinter as tk
from tkinter import messagebox

global start_time

def toggle_buttons():
    """
    switches the state of the 'start' and 'end' buttons, only allowing one to be active at a time
    :return:
    """
    if start_button["state"] == "normal":
        start_button["state"] = "disabled"
        end_button["state"] = "normal"
    else:
        start_button["state"] = "normal"
        end_button["state"] = "disabled"

def start_recording():
    """
    sets the first time and applies the 'RCORDING' label
    :return:
    """
    global start_time
    start_time = timer.report_time()

    record_label = tk.Label(root, text="RECORDING", bg="blue", fg="black", wraplength=740)
    record_label.place(x=220, y=50)

    toggle_buttons()

def end_recording():
    """
    sets the second time, calculates total time, calculates date, and saves the info to the .txt
    :return:
    """
    end_time = timer.report_time()

    record_label = tk.Label(root, text="RECORDED  ", bg="red", fg="black", wraplength=740)
    record_label.place(x=220, y=50)

    total_time = timer.calculate_total_time(start_time, end_time)
    dates = timer.calculate_date(start_time,end_time)
    comment = set_note(note.get())

    timer.save_to_file(dates, start_time, end_time, total_time, comment)

    toggle_buttons()

def window_close():
    """
    asks the user if they want to close the program and saves the time if the user has not done so already
    :return:
    """
    root.withdraw()
    answer = messagebox.askokcancel("warning", "Are you sure you want to quit? \n Make sure to hit 'end' first")
    if answer:
        if end_button["state"] == "normal":
            end_recording()
        root.destroy()
    else:
        root.deiconify()

def set_note(text):
    """

    :param text: input string from tk text entry box
    :return: empty string if the box is empty, comma separated string if there is a value
    """
    if text != "":
        return "," + text
    else:
        return text

# Placement of GUI objects

root = tk.Tk()
root.title("Time Tracker, By: Bridger")
root.protocol("WM_DELETE_WINDOW", window_close)

canvas = tk.Canvas(root, height=500, width=500, bg="#000000")
canvas.pack()

frame = tk.Frame(root, bg='grey')
frame.place(relwidth=1.0, relheight=1.0, relx=0.0, rely=0.1)

note = tk.StringVar('')
entry = tk.Entry(root, textvariable=note)
entry.place(x=180, y=300)

start_button = tk.Button(root, text="START", fg="white", bg="#0F4A16", command=start_recording, height=5, width=20)
start_button.place(x=180, y=100)

end_button = tk.Button(root, text="END", fg="white", bg="red", command=end_recording, height=5, width=20)
end_button.place(x=180, y=200)
end_button["state"] = "disabled"


root.mainloop()