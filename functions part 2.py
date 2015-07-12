Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
'int functions
SyntaxError: EOL while scanning string literal
>>> 'int function'
'int function'
>>> int(156.675)
156
>>> int('123')
123
>>> int('2.0)
    
SyntaxError: EOL while scanning string literal
>>> int('2.0')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int('2.0')
ValueError: invalid literal for int() with base 10: '2.0'
>>> print('len function')
len function
>>> 'len function'
'len function'
>>> len('this is a test')
14
>>> mythical_list = ['unicorn', 'cyclops', 'fairy', 'elf', 'dragon', 'troll']
>>> print(len(mythical_list))
6
>>> class(mythical_list)
SyntaxError: invalid syntax
>>> typeof (mythical_list)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    typeof (mythical_list)
NameError: name 'typeof' is not defined
>>> class (mythical_list)
SyntaxError: invalid syntax
>>> enemies_map = {'Batman' : 'Joker'}
>>> enemies_map = {'Batman' : 'Joker', 'Superman' : 'Lex Luthor', 'Spiderman' : 'Green Goblin'}
>>> print(len(enemies_map))
3
>>> enemies_map(1)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    enemies_map(1)
TypeError: 'dict' object is not callable
>>> enemies_map[1]
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    enemies_map[1]
KeyError: 1
>>> fruit = ['apple', 'banana', 'clementine', 'dragon fruit']
>>> length = len(fruit)
>>> for x in range (0, length):
	print('the fruit at index %s is %s' % (x, fruit[x]))

	
the fruit at index 0 is apple
the fruit at index 1 is banana
the fruit at index 2 is clementine
the fruit at index 3 is dragon fruit
>>> fruit[1]
'banana'
>>> fruit[1:2]
['banana']
>>> fruit[1,2]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    fruit[1,2]
TypeError: list indices must be integers, not tuple
>>> 'max + min functions'
'max + min functions'
>>> 
>>> 
>>> 
>>> height = [100, 132, 149, 87]
>>> print(max(height))
149
>>> print(min(height))
87
>>> letters = [a, b, c]
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    letters = [a, b, c]
NameError: name 'a' is not defined
>>> letters = 'a, b, c'
>>> print(max(letters))
c
>>> print(min(letters))
 
>>> print(min(letters))
 
>>> letters = 'a,b,c'
>>> print(min(letters))
,
>>> letters = 'abc'
>>> print(min(letters))
a
>>> guess_this_number = 61
>>> player_guesses = [3, 7, 13, 2]
>>> if max(player_guesses) > guess_this_number:
	print('boom! You lose')
	else:
		
SyntaxError: invalid syntax
>>> guess_this_number = 61
>>> player_guesses = [3, 7, 13, 2]
>>> if max(player_guesses) > guess_this_number:
	print('boom! You lose')

	
>>> if max(player_guesses) > guess_this_number:
	print('boom! You lose')

	
>>> if max(player_guesses) > guess_this_number:
	print('boom! You lose')
else:
	print('You Win!')

	
You Win!
>>> guess_this_number = 61
>>> player_guesses = [3, 7, 13, 2]
>>> if max(player_guesses) > guess_this_number:
	print('boom! You lose')
	
SyntaxError: multiple statements found while compiling a single statement
>>> guess_this_number = 61
>>> player_guesses = [3, 7, 13, 2]
>>> if max(player_guesses) > guess_this_number:
else:
	
SyntaxError: multiple statements found while compiling a single statement
>>> guess_this_number = 61
>>> player_guesses = [18, 3, 41, 89]
>>> if max(player_guesses) > guess_this_number:
	print('Boom! You lose')
else:
	print('You win')

	
Boom! You lose
>>> 
