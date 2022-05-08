Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def counter():
    x = 0
    while x < 10:
        x += 1
        return x

    
counter()
1
counter()
1
counter()
1
def counter():
    x = 0
    while x < 10:
        x += 1
        yield x

        
counter()
<generator object counter at 0x000001F4C09A1770>
text = "Brain Mentors"
iter(text)
<str_iterator object at 0x000001F4C09DC610>
iter_obj = iter(text)
next(iter_obj)
'B'
next(iter_obj)
'r'
next(iter_obj)
'a'
next(iter_obj)
'i'
next(iter_obj)
'n'
increment = counter()
next(increment)
1
next(increment)
2
next(increment)
3
next(increment)
4
next(increment)
5
next(increment)
6
next(increment)
7
next(increment)
8
next(increment)
9
next(increment)
10
next(increment)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    next(increment)
StopIteration
def greet():
    yield "Hi"
    yield "How are you ?"
    yield "Bye Take care..."

    
greet()
<generator object greet at 0x000001F4C09A1770>
msg = greet()
next(msg)
'Hi'
next(msg)
'How are you ?'
next(msg)
'Bye Take care...'
def greet():
    return "Hi"
    return "How are you ?"
    return "Bye Take care..."

greet()
'Hi'
greet()
'Hi'
greet()
'Hi'
