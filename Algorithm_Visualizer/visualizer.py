# MINI PROJECT 2 - Algorithm Visualizer

import tkinter as tk
import random
import time

WIDTH = 700
HEIGHT = 400
BAR_WIDTH = 20

data = [random.randint(20, 300) for _ in range(25)]


def draw_bars(canvas, arr, color="skyblue"):
    canvas.delete("all")

    x = 10
    for value in arr:
        canvas.create_rectangle(
            x,
            HEIGHT - value,
            x + BAR_WIDTH,
            HEIGHT,
            fill=color
        )
        x += BAR_WIDTH + 5

    root.update_idletasks()


def bubble_sort():
    n = len(data)

    for i in range(n):
        for j in range(0, n - i - 1):

            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

                draw_bars(canvas, data, "orange")
                time.sleep(0.1)

    draw_bars(canvas, data, "green")


def generate():
    global data
    data = [random.randint(20, 300) for _ in range(25)]
    draw_bars(canvas, data)


# UI
root = tk.Tk()
root.title("Algorithm Visualizer")
root.geometry("750x500")

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text="Generate", command=generate).grid(row=0, column=0, padx=10)
tk.Button(frame, text="Bubble Sort", command=bubble_sort).grid(row=0, column=1, padx=10)

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack(pady=20)

draw_bars(canvas, data)

root.mainloop()