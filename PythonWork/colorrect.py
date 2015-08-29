from tkinter import *
import random
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()

def random_rectangle(width,height,fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1,y1,x2,y2,fill=fill_colour)

colorchooser.askcolor()
canvas.create_arc(10,10,200,100 extent=180,style=ARC)



   
                    
    
