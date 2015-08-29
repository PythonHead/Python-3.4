Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> canvas.create_arc(10,10,20,100, extent=180,style=ARC)
1
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> canvas.create_arc(10,10,200,80, extent=45,style=ARC)
1
>>> canvas.create_arc(10,80,200,160, extent=90,style=ARC)
2
>>> canvas.create_arc(10,160,200,240,extent=135,style=ARC)
3
>>> canvas.create_arc(10,240,200,320,extent=180,style=ARC)
4
>>> canvas.create_arc(10,320,200,400,extent=359,style=ARC)
5
>>> from tkinter import *
>>> tk = Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> canvas.create_polygon(10,10,100,10,100,110,fill="",
		      outline="pink")
1
>>> canvas.create_polygon(200,10,240,30,120,100,140,120,fill="",
		      outline="Green")
2
>>> 
