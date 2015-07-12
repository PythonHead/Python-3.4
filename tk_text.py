Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> from tkinter import *
>>> tk =Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> canvas.create_text(150,100,text='There was once a kid who lived in a daisy,')
1
>>> canvas.create_text(150,100,text='who flew through the sky on a sparrow.',
		   fill='blue')
2
>>> from tkinter import *
>>> tk =Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> canvas.create_text(150,100,text='There was once a kid who lived in a daisy,')
1
>>> ================================ RESTART ================================
>>> from tkinter import *
>>> tk =Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> canvas.create_text(150,100,text='There was once a kid who lived in a daisy,')
1
>>> canvas.create_text(130,120,text='who flew through the sky on a sparrow.',
		   fill='blue')
2
>>> from tkinter import *
>>> tk =Tk()
>>> canvas = Canvas(tk,width=400,height=400)
>>> canvas.pack()
>>> ================================ RESTART ================================
>>> canvas.pack()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    canvas.pack()
NameError: name 'canvas' is not defined
>>> canvas = Canvas(tk,width=400,height=400)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    canvas = Canvas(tk,width=400,height=400)
NameError: name 'Canvas' is not defined
>>> 
