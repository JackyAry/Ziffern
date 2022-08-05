
import tkinter as tk
from PIL import ImageGrab


lastx, lasty = 0, 0


def xy(event):
    "Takes the coordinates of the mouse when you click the mouse"
    global lastx, lasty
    lastx, lasty = event.x, event.y


def addLine(event):
    """Creates a line when you drag the mouse
  from the point where you clicked the mouse to where the mouse is now"""
    global lastx, lasty
    drawingWindow.create_line((lastx, lasty, event.x, event.y),width =3 )
    # this makes the new starting point of the drawing
    lastx, lasty = event.x, event.y


def save():
    x = drawingWindow.winfo_rootx() + drawingWindow.winfo_x()
    y = drawingWindow.winfo_rooty() + drawingWindow.winfo_y()
    x1 = x + drawingWindow.winfo_width()
    y1 = y + drawingWindow.winfo_height()
    im = ImageGrab.grab((x, y, x1, y1))
    im.resize((28,28))
    im.save("captured.png")


def clearCanvas():
    drawingWindow.delete('all')
    label.configure(text ='')


root = tk.Tk()
root.geometry("300x600")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

drawingWindow = tk.Canvas(root, width = 280, height = 280, bg = "white")
drawingWindow.grid(column=0, row=0, sticky ="")
drawingWindow.bind("<Button-1>", xy)
drawingWindow.bind("<B1-Motion>", addLine)
root.bind("<Control-s>", save)



frame = tk.Frame(root, bg = "yellow", width = 200, height = 50).grid(row = 1, column = 0)
button1 = tk.Button(frame, text = "Erkennen", command = save).grid(row = 1, column = 0, sticky = "W", padx = 60)
button2 = tk.Button(frame, text = "Löschen", command = clearCanvas).grid(row = 1, column = 0, sticky = "E", padx = 60)



canvas = tk.Canvas(root, width = 280, bg = "white")
canvas.grid(column=0, row=2)
label = tk.Label(root,text = "1", font=('Times 100'), bg = "white")
label.grid(row = 2, column = 0)

root.mainloop()