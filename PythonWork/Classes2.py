Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 
>>> class Rocco:
	pass

>>> class inanimate(Rocco):
	pass

>>> class animate(Rocco):
	pass

>>> class Sidewalks(inanimate):
	pass

>>> class Animal(inanimate):
	pass

>>> class Mammals(inanimate):
	pass

>>> class Giraffes(inanimate):
	pass

>>> reginald = Giraffes()
>>> def this_is_a_normal_function():_
print('I am a normal function')
SyntaxError: invalid syntax
>>> class Animate(Animate):
        def breathe(self):
                pass
        def move(self):
                pass
        def eat_food(self):
                pass

        
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    class Animate(Animate):
NameError: name 'Animate' is not defined
>>> class Mammals(Animate):
	def feed_young_with_milk(self):
		pass

	
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    class Mammals(Animate):
NameError: name 'Animate' is not defined
>>> class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		pass

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    class Giraffes(Mammals):
NameError: name 'Mammals' is not defined
>>> reginald = Giraffes()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    reginald = Giraffes()
NameError: name 'Giraffes' is not defined
>>> reginald = Giraffes()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    reginald = Giraffes()
NameError: name 'Giraffes' is not defined
>>> reginald.move()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    reginald.move()
NameError: name 'reginald' is not defined
>>> reginald.eat_leaves_from_trees()
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    reginald.eat_leaves_from_trees()
NameError: name 'reginald' is not defined
>>> harold = Giraffes()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    harold = Giraffes()
NameError: name 'Giraffes' is not defined
>>> harold.move()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    harold.move()
NameError: name 'harold' is not defined
>>> class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move 9self0:
		
SyntaxError: invalid syntax
>>> class Animals(Animate):
	def breathe(self):
		print('breathing')
	def move (self):
		print('moving')
	def eat_food(self):
		print('eating_food')

		
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    class Animals(Animate):
NameError: name 'Animate' is not defined
>>> class Mammals(Animals):
	def feed_young_with_milk(self):
		print('feeding young')

		
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    class Mammals(Animals):
NameError: name 'Animals' is not defined
>>> class Giraffes(Mammals):
	def eat_leaves_from_trees(self):
		print ('eating leaves')

		
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    class Giraffes(Mammals):
NameError: name 'Mammals' is not defined
>>> reginald = Giraffes()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    reginald = Giraffes()
NameError: name 'Giraffes' is not defined
>>> harold = giraffes()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    harold = giraffes()
NameError: name 'giraffes' is not defined
>>> reginald.move()
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    reginald.move()
NameError: name 'reginald' is not defined
>>> 
