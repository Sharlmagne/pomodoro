import math
from tkinter import *
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
check_mark = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    global check_mark
    global timer
    reps = 0
    check_mark = ""
    check_label.config(text=check_mark)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="")
    window.after_cancel(timer)


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_mark
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 0 or reps == 2 or reps == 4 or reps == 6:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)
        reps += 1
    elif reps == 1 or reps == 3 or reps == 5:
        check_mark += "✔"
        check_label.config(text=check_mark)
        count_down(short_break_sec)
        reps += 1
        timer_label.config(text="Break", fg=PINK)
    elif reps == 7:
        check_mark += "✔"
        check_label.config(text=check_mark)
        count_down(long_break_sec)
        timer_label.config(text="Break", fg=RED)
        reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    if count_min < 10:
        count_min = f"0{count_min}"
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 30, "bold"), foreground=GREEN, background=YELLOW)
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_btn = Button(text="start", command=start_timer)
start_btn.grid(column=0, row=2)

reset_btn = Button(text="reset", command=reset)
reset_btn.grid(column=2, row=2)


check_label = Label(text=check_mark, background=YELLOW, foreground=GREEN)
check_label.grid(column=1, row=3)


window.mainloop()
