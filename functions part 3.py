Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.
'range function'
'range function'
>>> 
>>> 
>>> for x in range(0, 5)
SyntaxError: invalid syntax
>>> for x in range(0, 5):
	print(x)

	
0
1
2
3
4
>>> for x in range(1, 5):
	print(x)

	
1
2
3
4
>>> for x in range(0, 30):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
>>> for x in range(0, 30):
	print(x)

	
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
>>> print(list(range(0, 31)))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
>>> count_by_fives = list(range(0, 100, 5))
>>> 
>>> print(count_by_fives)
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
>>> count_down_by_threes = list(range(40, 10, -3))
>>> print(count_down_by_threes)
[40, 37, 34, 31, 28, 25, 22, 19, 16, 13]
>>> "sum function"
'sum function'
>>> my_list_of_numbers = list(range(0, 500, 50))
>>> print(my_list_of_numbers)
[0, 50, 100, 150, 200, 250, 300, 350, 400, 450]
>>> print(sum(my_list_of_numbers))
2250
>>> 'working with files'
'working with files'
>>> 
>>> 
>>> 
>>> 
