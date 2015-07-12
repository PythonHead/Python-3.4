Python 3.4.2 (v3.4.2:ab2c023a9432, Oct  5 2014, 20:42:22) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "copyright", "credits" or "license()" for more information.
>>> WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable.
Visit http://www.python.org/download/mac/tcltk/ for current information.

>>> test_file = open('/Users/roccolouis/test.txt')
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    test_file = open('/Users/roccolouis/test.txt')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/roccolouis/test.txt'
>>> test_file = open('/Users/RoccoLouis/test.txt')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    test_file = open('/Users/RoccoLouis/test.txt')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/RoccoLouis/test.txt'
>>> test_file = open('/Users/RoccoLouis/text.txt')
>>> test_file = open('c:\\myfile.txt','w')
>>> x = read(test.txt)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    x = read(test.txt)
NameError: name 'read' is not defined
>>> x = read(test_file)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    x = read(test_file)
NameError: name 'read' is not defined
>>> test_file.read
<built-in method read of _io.TextIOWrapper object at 0x101b397e0>
>>> print(test_file.read())
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    print(test_file.read())
io.UnsupportedOperation: not readable
>>> test_file.close
<built-in method close of _io.TextIOWrapper object at 0x101b397e0>
>>> test_file.close()
>>> test_file.close()
>>> test_file = open('/Users/RoccoLouis/text.txt')
>>> print(test_file.read())
hello my name is bob!!!
>>> test_file.close()
>>> a = abs(10) + abs(-10)
>>> print(a)
20
>>> b = abs(-10) + -10
>>> print(b)
0
>>> 
