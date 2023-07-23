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


# Function for entering new details
def enter():
    global enter1, team_a, team_b, date, location
    main_window.destroy()
    enter1 = Tk()
    enter1.geometry("1500x750")
    enter1.config(bg="#094074")
    # Entries
    team_a = Entry(bg="#306383")
    team_a.place(x=300, y=200, width=300, height=80)
    team_b = Entry(bg="#306383")
    team_b.place(x=930, y=200, width=300, height=80)
    date = Entry(bg="#306383")
    date.place(x=300, y=450, width=300, height=80)
    location = Entry(bg="#306383")
    location.place(x=930, y=450, width=300, height=80)
    # Labels
    Label(enter1, font="bold", text="Please enter name of team 1", bg="#094074", fg="white").place(x=300, y=150)
    Label(enter1, font="bold", text="Please enter name of team 2", bg="#094074", fg="white").place(x=930, y=150)
    Label(enter1, font="bold", text="Please enter the date of the game", bg="#094074", fg="white").place(x=300, y=400)
    Label(enter1, font="bold", text="Please enter the location of the game", bg="#094074", fg="white").place(x=930, y=400)
    # Submit button
    Button(enter1, text="Submit", command=sub1, height=3, width=30, bg="#edae49").place(x=930, y=600)


# Submit button for the first page
def sub1():
    enter1.destroy()
    enter2 = Tk()
    enter2.geometry("1500x750")
    enter2.config(bg="#094074")


# Setups for the buttons
def setup():
    Button(main_window, text="QUIT", command=leave, height=3, width=30, bg="#edae49").place(x=1138, y=550)
    Button(main_window, text="ENTER NEW MATCH DETAILS", command=enter, height=5, width=50, bg="#edae49").place(x=200, y=400)
    Button(main_window, text="VISIT OLD MATCH DETAILS", height=5, width=50, bg="#edae49").place(x=1000, y=400)
    Label(main_window, font='bold', text="Welcome to this program made to store sports games details", bg="#094074").place(x=500, y=200)


main()
