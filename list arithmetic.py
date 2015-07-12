Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
print(list arithmetic)
SyntaxError: invalid syntax
>>> 
>>> print(list_arithmetic)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(list_arithmetic)
NameError: name 'list_arithmetic' is not defined
>>> print("list_arithmetic")
list_arithmetic
>>> list1 = [1,2,3,4]
>>> list2 = ['i', 'tripped', 'over', 'and', 'hit', 'the', 'floor',]
>>> print list1 + list2
SyntaxError: Missing parentheses in call to 'print'
>>> print (list1 + list2)
[1, 2, 3, 4, 'i', 'tripped', 'over', 'and', 'hit', 'the', 'floor']
>>> list1 = [1,2,3,4]
>>> list2 = ['i', 'ate', 'chocolate', 'and', 'i', 'want', 'more']
>>> print(list1 + list2)
[1, 2, 3, 4, 'i', 'ate', 'chocolate', 'and', 'i', 'want', 'more']
>>> list1 = [1,2]
>>> print(list1 * 5)
[1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
>>> 
