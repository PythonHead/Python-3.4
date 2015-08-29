Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> if age == 10 or age == 11 or age == 12 or age == 13:
	print('What is 13 + 49 + 84 + 155 + 97 A headache!')
else:
	print('Huh?')

	
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    if age == 10 or age == 11 or age == 12 or age == 13:
NameError: name 'age' is not defined
>>> myval = None
>>> print(myval)
None
>>> myval = None
>>> if myval == None:
	print("The variable myval doesn't have a value")

	
The variable myval doesn't have a value
>>> if age == 10:
	print("what's the best way to speak to a monster?")
	print("from as far away as possible!")

	
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    if age == 10:
NameError: name 'age' is not defined
>>> 
