from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps  # Used to declare that you are working with the global variables
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    # By the 8th rep, countdown to long break
    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text="LONG BREAK SESSION", fg=PINK)
    # For reps divisible by 2, short break
    elif reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text="SHORT BREAK SESSION", fg=RED)
    # for other odd reps, normal timer
    else:
        count_down(work_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
# A function to carry out the timer countdown
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer, text=f"{count_min}:{count_sec}")
    if count > 0:  # This if statement acts like a while loop to trigger the function when count > 0
        window.after(1000, count_down, count - 1)
    else:
        start_timer()
        reps_marker = ""
        work_session = math.floor(reps/2)   # This is used to get the whole number for each rep and break combined
        for rep in range(work_session):
            reps_marker += "✅"
        check_mark.config(text=reps_marker)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")

# We set padding for the window to adjust the distance between the image and window background
window.config(padx=100, pady=100, bg=YELLOW)

# The title_label designed from the label class, fg is used to set text color while bg is for background color
# Note, grid and pack layout managers cannot be combined

title_label = Label(text="Timer", font=(FONT_NAME, 45, "italic"), fg=GREEN, bg=YELLOW)
title_label.grid(row=0, column=1)

# Canvas class which allows us to overlap different images on each other
canvas = Canvas(width=200, height=224, bg=YELLOW)

# PhotoImage class allows us to declare the image file and store in an object for later display
tomato_image = PhotoImage(file="tomato.png")

canvas.create_image(102, 112, image=tomato_image)
timer = canvas.create_text(103, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start Button", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset Button", highlightthickness=0)
reset_button.grid(row=2, column=2)

check_mark = Label(text="", fg=GREEN, bg="white")
check_mark.grid(row=2, column=1)

window.mainloop()

