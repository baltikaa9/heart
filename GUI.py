from tkinter import *

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt

from anim import Animation
from color import Color

fig = plt.figure(figsize=(5, 5), facecolor=Color.dark.value)

root = Tk()
root.wm_title("Сердечко")
root.iconbitmap('F:\\Projects\\PycharmProjects\\heart\\heart.ico')
root.geometry('1080x900+400+70')
root.config(background=Color.dark.value)

# Окно графика
frame1 = Frame(root, bg=Color.dark.value)
frame1.place(x=0, y=0, relwidth=0.83, relheight=1)

canvas = FigureCanvasTkAgg(fig, master=frame1)
canvas.get_tk_widget().place(relx=0, y=0, relwidth=1, relheight=1)

# Окно интерфейса
frame2 = Frame(root, bg=Color.dark.value)
frame2.place(relx=0.83, y=0, relwidth=0.17, relheight=1)

# Навигация
# toolbar = NavigationToolbar2Tk(canvas, root)
# toolbar.config(background=Color.dark.value)
# toolbar._message_label.config(background=Color.dark.value, foreground=Color.white.value)
# toolbar.update()

play = True

# def create_labels():
"""Надписи"""
Label(frame2, text='Speed', bg=Color.dark.value, foreground=Color.white.value).place(x=10, y=10)
Label(frame2, text='Max n', bg=Color.dark.value, foreground=Color.white.value).place(x=10, y=60)

# def create_entries():
"""Поля ввода"""
speed_enter = Entry(frame2, bg=Color.dark.value, foreground=Color.white.value, width=17)
n_enter = Entry(frame2, bg=Color.dark.value, foreground=Color.white.value, width=17)

speed_enter.place(x=10, y=35)
n_enter.place(x=10, y=85)

speed_enter.insert(0, '0.1')
n_enter.insert(0, '100')


def create_buttons():
    """Кнопки"""
    btn_pause = Button(frame2, text='Остановить', bg=Color.dark.value, foreground=Color.white.value,
                       activebackground=Color.dark.value, activeforeground=Color.white.value, command=pause, width=14,
                       height=1)
    btn_restart = Button(frame2, text='Начать заного', bg=Color.dark.value, foreground=Color.white.value,
                         activebackground=Color.dark.value, activeforeground=Color.white.value, command=restart,
                         width=14, height=1)
    btn_quit = Button(frame2, text='Выход', bg=Color.dark.value, foreground=Color.white.value,
                      activebackground=Color.dark.value, activeforeground=Color.white.value, command=_quit, width=14,
                      height=1)

    btn_pause.place(x=10, y=140)
    btn_restart.place(x=10, y=180)
    btn_quit.place(x=10, y=220)
    return btn_restart, btn_pause, btn_quit


def restart(event=None):
    try:
        speed = float(speed_enter.get())
        n = int(n_enter.get())
        if speed > n:
            raise ValueError
    except ValueError:
        return
    else:
        graph.restart(n, speed)

        global play
        play = True
        btn_pause.config(text='Остановить')

        canvas.draw()


def pause():
    global play
    if play:
        graph.pause()
        play = False
        btn_pause.config(text='Продолжить')
    else:
        graph.resume()
        play = True
        btn_pause.config(text='Остановить')


def _quit(event=None):
    root.destroy()
    plt.close()


speed_enter.bind('<Return>', restart)
n_enter.bind('<Return>', restart)
root.bind('<Escape>', _quit)
root.protocol('WM_DELETE_WINDOW', _quit)


def init_gui():
    global btn_run, btn_pause, btn_quit
    btn_run, btn_pause, btn_quit = create_buttons()
    global graph
    graph = Animation(fig)
