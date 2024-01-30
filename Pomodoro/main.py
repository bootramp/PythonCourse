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
reps = 1
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    status_text.config(text="Timer")
    check_symbol.config(text="")
    reps = 1
# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global reps
    work_min_in_sec = WORK_MIN * 60
    short_break_in_sec = SHORT_BREAK_MIN * 60
    long_break_in_sec = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        status_text.config(text="Break", fg=RED)
        count_down(long_break_in_sec)
    elif reps % 2 == 0:
        status_text.config(text="Break", fg=PINK)
        count_down(short_break_in_sec)
    elif reps % 2 == 1:
        status_text.config(text="Work", fg=GREEN)
        count_down(work_min_in_sec)
    reps += 1
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_min = math.floor(count / 60)
    if count_min < 10:
        # Python is Dynamic Lan
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        # Python is Dynamic Lan
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        check_mark = math.floor(reps/2)
        for _ in range(check_mark):
            mark = "✔"
        check_symbol.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=220, height=260, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(111, 120, image=tomato_img)
timer_text = canvas.create_text(111, 140, text="00:00", fill="white", font=(FONT_NAME, 40, "bold"))
canvas.grid(column=2, row=1)

status_text = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"), highlightthickness=0)
status_text.grid(column=2, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=1, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=3, row=2)

check_symbol = Label(fg=GREEN, bg=YELLOW, font=(26), highlightthickness=0)
check_symbol.grid(column=2, row=3)


window.mainloop()
