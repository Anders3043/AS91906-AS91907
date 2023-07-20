from tkinter import *


# Function to run everything
def main():
    global main_window
    main_window = Tk()
    main_window.geometry("1500x750")
    main_window.config(bg="#094074")
    setup()
    main_window.resizable(False, False)
    main_window.mainloop()


# Function for quit button for main window
def leave():
    main_window.destroy()


# Function for quit button for first enter screen
def leave1():
    enter1.destroy()


# Function for entering new details
def enter():
    global enter1
    main_window.destroy()
    enter1 = Tk()
    enter1.geometry("1500x750")
    enter1.config(bg="#094074")
    Button(enter1, text="QUIT", command=leave1, height=3, width=30, bg="#edae49").place(x=1138, y=550)

# Setups for the buttons
def setup():
    Button(main_window, text="QUIT", command=leave, height=3, width=30, bg="#edae49").place(x=1138, y=550)
    Button(main_window, text="ENTER NEW MATCH DETAILS", command=enter, height=5, width=50, bg="#edae49").place(x=200, y=400)
    Button(main_window, text="VISIT OLD MATCH DETAILS", height=5, width=50, bg="#edae49").place(x=1000, y=400)


main()
