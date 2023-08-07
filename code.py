from tkinter import *


# Function to run everything
def main():
    global main_window
    main_window = Tk()
    main_window.geometry("1500x750")
    main_window.config(bg="#094074")
    Button(main_window, text="QUIT", command=leave, height=3, width=30, bg="#edae49").place(x=1138, y=550)
    Button(main_window, text="ENTER NEW MATCH DETAILS", command=enter, height=5, width=50, bg="#edae49").place(x=200, y=400)
    Button(main_window, text="VISIT OLD MATCH DETAILS", height=5, width=50, bg="#edae49").place(x=1000, y=400)
    Label(main_window, font='bold', text="Welcome to this program made to store sports games details", bg="#094074", fg="white").place(x=500, y=200)
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
    enter1.resizable(False, False)
    # Entries
    team_a = Entry(bg="#306383")
    team_a.place(x=300, y=200, width=300, height=80)
    team_b = Entry(bg="#306383")
    team_b.place(x=930, y=200, width=300, height=80)
    date = Entry(bg="#306383")
    date.place(x=300, y=450, width=300, height=80)
    date.insert(0, "Please put it in this format DAY/MONTH eg. 28/7")
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
    global team_a_mem1, team_b_mem1, enter2, team_a_goal, team_b_goal, team_a_box, team_b_box, date_box, location_box, \
        team_a_mem2, team_a_mem3, team_a_mem4, team_a_mem5, team_a_mem6, team_a_mem7, team_a_mem8, team_a_mem9, \
        team_a_mem10, team_a_mem11, team_b_mem2, team_b_mem3, team_b_mem4, team_b_mem5, team_b_mem6, team_b_mem7, \
        team_b_mem8, team_b_mem9, team_b_mem10, team_b_mem11
    # Creating variable for checking
    team_a_check = len(team_a.get())
    team_b_check = len(team_b.get())
    date_check = len(date.get())
    location_check = len(location.get())
    # Creating variable therefore it could be used for the next page
    team_a_box = team_a.get()
    team_b_box = team_b.get()
    date_box = date.get()
    location_box = location.get()
    # Checking if any of the entry are empty
    if team_b_check == 0 or team_a_check == 0 or date_check == 0 or location_check == 0 or date_box == "Please put it in this format DAY/MONTH eg. 28/7":
        Label(enter1, font="bold", text="Please make sure every box has been filled", fg='red', bg='#094074').place(x=570, y=350)

    # Running the new window
    else:
        # Setup new page
        enter1.destroy()
        enter2 = Tk()
        enter2.geometry("1500x750")
        enter2.config(bg="#094074")
        enter2.resizable(False, False)
        # Making new labels based on the entry
        Label(enter2, font='bold', text=team_a_box, bg='#003d5b', fg='white').place(x=300, y=160)
        Label(enter2, font='bold', text="Please enter team member on each side", bg='#094074', fg='white').place(x=580, y=240)
        Label(enter2, font='bold', text="Please enter goal scored on each side", bg='#094074', fg='white').place(x=600, y=520)
        Label(enter2, font='bold', text=team_b_box, bg='#003d5b', fg='white').place(x=1200, y=160)
        Label(enter2, font='bold', text=date_box, bg='#003d5b', fg='white').place(x=750, y=160)
        Label(enter2, font='bold', text=location_box, bg='#003d5b', fg='white').place(x=750, y=200)
        # Making the VS label
        vs = Label(enter2, font='bold', text='VS', bg='#094074', fg='red',)
        vs.config(font=('Helvetica bold', 70))
        vs.place(x=700, y=400)
        # Making new entry
        team_a_mem1 = Entry(bg="#306383")
        team_a_mem1.place(x=220, y=250, width=200, height=30)
        team_a_mem2 = Entry(bg="#306383")
        team_a_mem2.place(x=220, y=280, width=200, height=30)
        team_a_mem3 = Entry(bg="#306383")
        team_a_mem3.place(x=220, y=310, width=200, height=30)
        team_a_mem4 = Entry(bg="#306383")
        team_a_mem4.place(x=220, y=340, width=200, height=30)
        team_a_mem5 = Entry(bg="#306383")
        team_a_mem5.place(x=220, y=370, width=200, height=30)
        team_a_mem6 = Entry(bg="#306383")
        team_a_mem6.place(x=220, y=400, width=200, height=30)
        team_a_mem7 = Entry(bg="#306383")
        team_a_mem7.place(x=220, y=430, width=200, height=30)
        team_a_mem8 = Entry(bg="#306383")
        team_a_mem8.place(x=220, y=460, width=200, height=30)
        team_a_mem9 = Entry(bg="#306383")
        team_a_mem9.place(x=220, y=490, width=200, height=30)
        team_a_mem10 = Entry(bg="#306383")
        team_a_mem10.place(x=220, y=520, width=200, height=30)
        team_a_mem11 = Entry(bg="#306383")
        team_a_mem11.place(x=220, y=550, width=200, height=30)
        team_b_mem1 = Entry(bg="#306383")
        team_b_mem1.place(x=1120, y=250, width=200, height=30)
        team_b_mem2 = Entry(bg="#306383")
        team_b_mem2.place(x=1120, y=280, width=200, height=30)
        team_b_mem3 = Entry(bg="#306383")
        team_b_mem3.place(x=1120, y=310, width=200, height=30)
        team_b_mem4 = Entry(bg="#306383")
        team_b_mem4.place(x=1120, y=340, width=200, height=30)
        team_b_mem5 = Entry(bg="#306383")
        team_b_mem5.place(x=1120, y=370, width=200, height=30)
        team_b_mem6 = Entry(bg="#306383")
        team_b_mem6.place(x=1120, y=400, width=200, height=30)
        team_b_mem7 = Entry(bg="#306383")
        team_b_mem7.place(x=1120, y=430, width=200, height=30)
        team_b_mem8 = Entry(bg="#306383")
        team_b_mem8.place(x=1120, y=460, width=200, height=30)
        team_b_mem9 = Entry(bg="#306383")
        team_b_mem9.place(x=1120, y=490, width=200, height=30)
        team_b_mem10 = Entry(bg="#306383")
        team_b_mem10.place(x=1120, y=520, width=200, height=30)
        team_b_mem11 = Entry(bg="#306383")
        team_b_mem11.place(x=1120, y=550, width=200, height=30)
        team_a_goal = Entry(bg="#306383")
        team_a_goal.place(x=220, y=600, width=200, height=75)
        team_b_goal = Entry(bg="#306383")
        team_b_goal.place(x=1120, y=600, width=200, height=75)
        # Submit button
        Button(enter2, text="Submit", command=team_check, height=3, width=30, bg="#edae49").place(x=650, y=615)


def team_check():
    team_a_player1 = team_a_mem1.get()
    team_b_player1 = team_b_mem1.get()
    # Check if goals are number
    try:
        int(team_a_goal.get())
        a_goal = "True"
    except ValueError:
        a_goal = "False"

    try:
        int(team_b_goal.get())
        b_goal = "True"
    except ValueError:
        b_goal = "False"

    # Check if the entries are correct
    if team_a_player1 == "" or team_b_player1 == "":
        Label(enter2, font='bold', text='Please make sure you have at least entered 1 member on each team', bg="#094074", fg="red").place(x=480, y=550)
    elif a_goal == "False" or b_goal == "False":
        Label(enter2, font='bold', text='Please make sure you have entered the goals each team score in numbers', bg='#094074', fg='red').place(x=450, y=550)
    else:
        # Put player's name in a list
        team_a_player = [team_a_mem1.get(), team_a_mem2.get(), team_a_mem3.get(), team_a_mem4.get(), team_a_mem5.get(),
                         team_a_mem6.get(), team_a_mem7.get(), team_a_mem8.get(), team_a_mem9.get(), team_a_mem10.get(),
                         team_a_mem11.get()]
        team_b_player = [team_b_mem1.get(), team_b_mem2.get(), team_b_mem3.get(), team_b_mem4.get(), team_b_mem5.get(),
                         team_b_mem6.get(), team_b_mem7.get(), team_b_mem8.get(), team_b_mem9.get(), team_b_mem10.get(),
                         team_b_mem11.get()]
        # Create new page
        enter2.destroy()
        enter3 = Tk()
        enter3.geometry("1500x750")
        enter3.config(bg="#094074")
        enter3.resizable(False, False)
        # Labels for new page
        Label(enter3, font='bold', text=team_a_box, bg='#003d5b', fg='white').place(x=300, y=160)
        Label(enter3, font='bold', text=team_b_box, bg='#003d5b', fg='white').place(x=1200, y=160)
        Label(enter3, font='bold', text=date_box, bg='#003d5b', fg='white').place(x=750, y=160)
        Label(enter3, font='bold', text=location_box, bg='#003d5b', fg='white').place(x=750, y=200)
        Label(enter3, font='bold', text="Please enter goal scored by each member on each side", bg='#094074', fg='white').place(x=530, y=240)
        Label(enter3, font='bold', text="(Remove the player's name then add the goal they scored)", bg='#094074',
              fg='white').place(x=515, y=280)
        # Entry boxes for goal scored by each member
        team_a_mem1_goal = Entry(bg="#306383")
        team_a_mem1_goal.place(x=220, y=250, width=200, height=30)
        team_a_mem1_goal.insert(0, team_a_player[0])
        team_a_mem2_goal = Entry(bg="#306383")
        team_a_mem2_goal.place(x=220, y=280, width=200, height=30)
        team_a_mem2_goal.insert(0, team_a_player[1])
        team_a_mem3_goal = Entry(bg="#306383")
        team_a_mem3_goal.place(x=220, y=310, width=200, height=30)
        team_a_mem3_goal.insert(0, team_a_player[2])
        team_a_mem4_goal = Entry(bg="#306383")
        team_a_mem4_goal.place(x=220, y=340, width=200, height=30)
        team_a_mem4_goal.insert(0, team_a_player[3])
        team_a_mem5_goal = Entry(bg="#306383")
        team_a_mem5_goal.place(x=220, y=370, width=200, height=30)
        team_a_mem5_goal.insert(0, team_a_player[4])
        team_a_mem6_goal = Entry(bg="#306383")
        team_a_mem6_goal.place(x=220, y=400, width=200, height=30)
        team_a_mem6_goal.insert(0, team_a_player[5])
        team_a_mem7_goal = Entry(bg="#306383")
        team_a_mem7_goal.place(x=220, y=430, width=200, height=30)
        team_a_mem7_goal.insert(0, team_a_player[6])
        team_a_mem8_goal = Entry(bg="#306383")
        team_a_mem8_goal.place(x=220, y=460, width=200, height=30)
        team_a_mem8_goal.insert(0, team_a_player[7])
        team_a_mem9_goal = Entry(bg="#306383")
        team_a_mem9_goal.place(x=220, y=490, width=200, height=30)
        team_a_mem9_goal.insert(0, team_a_player[8])
        team_a_mem10_goal = Entry(bg="#306383")
        team_a_mem10_goal.place(x=220, y=520, width=200, height=30)
        team_a_mem10_goal.insert(0, team_a_player[9])
        team_a_mem11_goal = Entry(bg="#306383")
        team_a_mem11_goal.place(x=220, y=550, width=200, height=30)
        team_a_mem11_goal.insert(0, team_a_player[10])
        team_b_mem1_goal = Entry(bg="#306383")
        team_b_mem1_goal.place(x=1120, y=250, width=200, height=30)
        team_b_mem1_goal.insert(0, team_b_player[0])
        team_b_mem2_goal = Entry(bg="#306383")
        team_b_mem2_goal.place(x=1120, y=280, width=200, height=30)
        team_b_mem2_goal.insert(0, team_b_player[1])
        team_b_mem3_goal = Entry(bg="#306383")
        team_b_mem3_goal.place(x=1120, y=310, width=200, height=30)
        team_b_mem3_goal.insert(0, team_b_player[2])
        team_b_mem4_goal = Entry(bg="#306383")
        team_b_mem4_goal.place(x=1120, y=340, width=200, height=30)
        team_b_mem4_goal.insert(0, team_b_player[3])
        team_b_mem5_goal = Entry(bg="#306383")
        team_b_mem5_goal.place(x=1120, y=370, width=200, height=30)
        team_b_mem5_goal.insert(0, team_b_player[4])
        team_b_mem6_goal = Entry(bg="#306383")
        team_b_mem6_goal.place(x=1120, y=400, width=200, height=30)
        team_b_mem6_goal.insert(0, team_b_player[5])
        team_b_mem7_goal = Entry(bg="#306383")
        team_b_mem7_goal.place(x=1120, y=430, width=200, height=30)
        team_b_mem7_goal.insert(0, team_b_player[6])
        team_b_mem8_goal = Entry(bg="#306383")
        team_b_mem8_goal.place(x=1120, y=460, width=200, height=30)
        team_b_mem8_goal.insert(0, team_b_player[7])
        team_b_mem9_goal = Entry(bg="#306383")
        team_b_mem9_goal.place(x=1120, y=490, width=200, height=30)
        team_b_mem9_goal.insert(0, team_b_player[8])
        team_b_mem10_goal = Entry(bg="#306383")
        team_b_mem10_goal.place(x=1120, y=520, width=200, height=30)
        team_b_mem10_goal.insert(0, team_b_player[9])
        team_b_mem11_goal = Entry(bg="#306383")
        team_b_mem11_goal.place(x=1120, y=550, width=200, height=30)
        team_b_mem11_goal.insert(0, team_b_player[10])


main()
