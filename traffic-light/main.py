import tkinter as tk
from time import sleep
from enum import Enum


class Color(Enum):
    RED = 'red'
    YELLOW = 'yellow'
    GREEN = 'green'
    WHITE = 'white'
    BLACK = 'black'


LIGHT_RED = Color.RED.value
LIGHT_YELLOW = Color.YELLOW.value
LIGHT_GREEN = Color.GREEN.value
BG_WHITE = Color.WHITE.value
BG_BLACK = Color.BLACK.value


class PassState(Enum):
    CAN_PASS = 'Can PASS.'
    SHOULD_NOT_PASS = 'Should not PASS.'


CAN_PASS = PassState.CAN_PASS.value
SHOULD_NOT_PASS = PassState.SHOULD_NOT_PASS.value

# create GUI window
window = tk.Tk()
window.title('TrafficSignal')
window.geometry('300x350')

# Traffic light UI
r = tk.Label(window, bg=BG_WHITE, font=('Arial, 12'),
             borderwidth=2, relief="solid", width=5, height=3)
r.place(x=70, y=40)
y = tk.Label(window, bg=BG_WHITE, font=('Arial, 12'),
             borderwidth=2, relief="solid", width=5, height=3)
y.place(x=130, y=40)
g = tk.Label(window, bg=LIGHT_GREEN, font=('Arial, 12'),
             borderwidth=2, relief="solid", width=5, height=3)
g.place(x=190, y=40)


signal = True
result = tk.StringVar()

result.set(CAN_PASS)


def count_time(i, j):
    while i >= 0 or j >= 0:
        time.set(i)
        window.update()
        sleep(1)
        i = i - 1
        if i == -1:
            change_light(1)
            # sleep(1)
            i = j
            j = -1


def change_light(FLAG):
    global signal
    global x

    # 紅燈時
    if signal is False:
        signal = True
        result.set(CAN_PASS)
        g.config(bg=LIGHT_GREEN)
        r.config(bg=BG_WHITE)
    # 綠燈時
    else:
        signal = False
        g.config(bg=BG_WHITE)

        # 是否轉黃燈
        if FLAG:
            y.config(bg=LIGHT_YELLOW)
            window.update()
            sleep(2)
            y.config(bg=BG_WHITE)

        r.config(bg=LIGHT_RED)
        result.set(SHOULD_NOT_PASS)


time = tk.StringVar()
time.set("0")


def test():
    print("Hello")


# Buttons UI
# 倒數計時
t = tk.Label(window, bg=BG_BLACK, textvariable=time, fg=BG_WHITE,
             font=('Arial, 10'), width=5, height=3)
t.place(x=245, y=45)


s = tk.Button(window, text="Start", width=15, height=2,
              command=lambda: count_time(i=3, j=4))
s.place(x=100, y=120)

# p = tk.Button(window, text="Pause", width=15, height=2,
#               command=lambda: count_time(i=-1, j=-1))
p = tk.Button(window, text="Pause", width=15, height=2,
              command=test)

p.place(x=100, y=170)

c = tk.Button(window, text="Quick Change", cursor="target",
              width=15, height=2,
              command=lambda: change_light(FLAG=0))
c.place(x=100, y=220)

# 顯示狀態
show = tk.Label(window, textvariable=result,
                font=('Arial, 12'), anchor='w', width=18, height=2)
show.place(x=110, y=280)

window.mainloop()
