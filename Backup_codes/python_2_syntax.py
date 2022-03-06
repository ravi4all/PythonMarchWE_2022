Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print "Hello"
Hello
>>> print "Hello", "World"
Hello World
>>> print("Hello", "World")
('Hello', 'World')
>>> input("Enter a number : ")
Enter a number : 45
45
>>> input("Enter your name : ")
Enter your name : Ravi

Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    input("Enter your name : ")
  File "<string>", line 1, in <module>
NameError: name 'Ravi' is not defined
>>> input("Enter your name : ")
Enter your name : 'Ravi'
'Ravi'
>>> raw_input("Enter your name : ")
Enter your name : Ravi
'Ravi'
>>> True = "Hello"
>>> flag = True
>>> flag
'Hello'
>>> 
