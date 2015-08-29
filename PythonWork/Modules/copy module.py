Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> class Animal
SyntaxError: invalid syntax
>>> 
>>> 
>>> 
>>> class Animal:
	def __init__(self,species,number_of_legs,color)
	
SyntaxError: invalid syntax
>>> ================================ RESTART ================================
>>> 
Enter your first guess:1
Enter your second guess:4
Enter your third guess:19
Enter your fourth guess:18
[1.0, 4.0, 19.0, 18.0]
You Win!
>>> ================================ RESTART ================================
>>> 
Enter your first guess:1
Enter your second guess:2
Enter your third guess:3
Enter your fourth guess:4
You Win! The correct answer was 1
>>> ================================ RESTART ================================
>>> 
Enter your first guess:2
Enter your second guess:3
Enter your third guess:4
Enter your fourth guess:5
Boom! You lose the correct answer was 1
>>> class Animal:
	def __init__(self,species,number_of_legs,color):
		self.species = species
		self.number_of_legs = number_of_legs
		self.color = color

		
>>> harry = Animal('hippogriff',6,'pink')
>>> import copy
>>> harry = Animal('hippogriff',6,'pink')
>>> harriet = copy.copy(harry)
>>> print harry.species
SyntaxError: Missing parentheses in call to 'print'
>>> print (harry.species)
hippogriff
>>> print (harriet.species)
hippogriff
>>> harry = Animal('hippogriff',6,'pink')
>>> carrie = Animal('chimera',4,'green polka dots')
>>> billy = Animal('bogill',0,'paisely')
>>> my_animals = [harry,carrie,billy]
>>> more_animals = copy.copy(my_animals)
>>> print(more_animals[0].species)
hippogriff
>>> print(more_animals[1].species)
chimera
>>> my_animals[0].species = 'ghoul'
>>> print(my_animals[0].species)
ghoul
>>> print(more_animals[0].species)
ghoul
>>> ben = Animal('sphinx',4,'sand')
>>> my_animals.append(ben)
>>> print(len(my_animals))
4
>>> print(len(more_animals))
3
>>> more_animals = copy.deepcopy(my_animals)
>>> my_animals[0].species = 'wyrm'
>>> print(my_animals[0].species)
wyrm
>>> print(more_animals[0].species)
ghoul
>>> 
