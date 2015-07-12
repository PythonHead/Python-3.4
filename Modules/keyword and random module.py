Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
'keyword module'
'keyword module'
>>> 
>>> 
>>> ================================ RESTART ================================
>>> 
Enter your first guess:2
Enter your second guess:1
Enter your third guess:5
Enter your fourth guess:10
You Win! The correct answer was 1
>>> ================================ RESTART ================================
>>> 
Enter your first guess:5
Enter your second guess:7
Enter your third guess:6
Enter your fourth guess:4
Boom! You lose the correct answer was 1
>>> 'keyword module'
'keyword module'
>>> 
>>> 
>>> import keyword
>>> print(keyword.iskeyword('if'))
True
>>> print(keyword.iskeyword('correct'))
False
>>> print(keyword.iskeyword('end'))
False
>>> print(keyword.iskeyword('python'))
False
>>> print(keyword.iskeyword('abs'))
False
>>> 'random module'
'random module'
>>> import random
>>> ================================ RESTART ================================
>>> 
Enter your first guess:19
Enter your second guess:5
Enter your third guess:10
Enter your fourth guess:12
Boom! You lose the correct answer was 20
>>> ================================ RESTART ================================
>>> 
Enter your first guess:20
Enter your second guess:12
Enter your third guess:6
Enter your fourth guess:17
Boom! You lose the correct answer was 7
>>> print(random.randint(1,100))
19
>>> print(random.randint(100,1000))
502
>>> print(random.randint(1000,5000))
4449
>>> import random
>>> ================================ RESTART ================================
>>> 
Guess 4 numbers between 1 and 20
Enter your first guess:7
Enter your second guess:20
Enter your third guess:5
Enter your fourth guess:3
Boom! You lose the correct answer was 4
>>> import random
>>> sweeties = ['sour bottles','candy','lolliepop']
>>> print(random.choice(sweeties))
lolliepop
>>> print(random.choice[31]sweeties))
SyntaxError: invalid syntax
>>> print(random.choice[31].sweeties))
SyntaxError: invalid syntax
>>> 
>>> print(random.choice[31].sweeties)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(random.choice[31].sweeties)
TypeError: 'method' object is not subscriptable
>>> print(random[31].choice.sweeties)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    print(random[31].choice.sweeties)
TypeError: 'module' object is not subscriptable
>>> import random
>>> sweeties = ['sour bottles','candy','lolliepop','marshmallows']
>>> random.shuffle(sweetie)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    random.shuffle(sweetie)
NameError: name 'sweetie' is not defined
>>> random.shuffle(sweeties)
>>> print(sweeties)
['lolliepop', 'marshmallows', 'candy', 'sour bottles']
>>> 
