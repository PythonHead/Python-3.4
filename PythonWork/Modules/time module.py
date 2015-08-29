Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> 'time module'
'time module'
>>> import time
>>> print(time.time())
1436408800.193509
>>> def lot_of_numbers(max):
	for bubble in range (0,max):
		print(bubble)

		
>>> def lot_of_numbers(max):
	for x in range (0,max):
		print(x)

		
>>> lots_of_numbers(1000)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    lots_of_numbers(1000)
NameError: name 'lots_of_numbers' is not defined
>>> import time
>>> def lot_of_numbers(max):
	for x in range (0,max):
		print(x)

		
>>> lots_of_numbers(1000)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lots_of_numbers(1000)
NameError: name 'lots_of_numbers' is not defined
>>> def lot_of_numbers(max):
	for x in range (0,max):
		print(x)

		
>>> lots_of_numbers(1000)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    lots_of_numbers(1000)
NameError: name 'lots_of_numbers' is not defined
>>> print("pickle Module")
pickle Module
>>> game_data = {
	'player-positions' : 'N23 E45',
	'pockets' : ['keys', 'pocket knife', 'polished stone'],
	'backpack' : ['rope', 'hammer', 'apple'],
	'money' : 158.50
	}
>>> save_file = open('save.dat','wb')
>>> pickle.dump(game_data,save_file)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pickle.dump(game_data,save_file)
NameError: name 'pickle' is not defined
>>> import pickle
>>> game_data = {
	'player-positions' : 'N23 E45',
	'pockets' : ['keys', 'pocket knife', 'polished stone'],
	'backpack' : ['rope', 'hammer', 'apple'],
	'money' : 158.50
	}
>>> save_file = open('save.dat','wb')
>>> pickle.dump(game_data,save_file)
>>> save_file.close()
>>> load_file = open('save.dat','rb')
>>> loaded_game_data = pickle.load(load_file)
>>> load_file.close()
>>> print(loaded_game_data)
{'backpack': ['rope', 'hammer', 'apple'], 'player-positions': 'N23 E45', 'pockets': ['keys', 'pocket knife', 'polished stone'], 'money': 158.5}
>>> 
