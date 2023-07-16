from tkinter import *


def main():
    global main_window
    main_window = Tk()
    main_window.geometry("1500x750")
    setup()
    size()
    main_window.resizable(False, False)
    main_window.mainloop()


def size():
    width = 1500
    height = 750

    screen_width = main_window.winfo_screenwidth()  # Width of the screen
    screen_height = main_window.winfo_screenheight() # Height of the screen

    # Calculate Starting X and Y coordinates for Window
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)

    main_window.geometry('%dx%d+%d+%d' % (width, height, x, y))


def leave():
    main_window.destroy()


def setup():
    Button(main_window, text="Quit", command=leave).grid(column=1, row=0)


main()
