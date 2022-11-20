import timer
import tkinter as tk
from tkinter import messagebox

def start_recording():
    pass

def end_recording():
    pass

def window_close():
    root.withdraw()
    answer = messagebox.askokcancel("warning", "Are you sure you want to quit? \n Make sure to hit 'end' first")
    if answer:
        end_recording()
        root.destroy()
    else:
        root.deiconify()

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