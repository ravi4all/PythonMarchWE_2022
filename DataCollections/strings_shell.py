Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello World, this is Python programming"
>>> len(text)
39
>>> text[0]
'H'
>>> text[10]
'd'
>>> text[28]
'p'
>>> text[38]
'g'
>>> text[39]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text[39]
IndexError: string index out of range
>>> text[:]
'Hello World, this is Python programming'
>>> text[0:]
'Hello World, this is Python programming'
>>> text[10:]
'd, this is Python programming'
>>> text[:100]
'Hello World, this is Python programming'
>>> text[0:10]
'Hello Worl'
>>> text[10:0]
''
>>> text[0:20:2]
'HloWrd hsi'
>>> text[0:10:1]
'Hello Worl'
>>> text[10:1:-1]
'dlroW oll'
>>> for i in range(0,10,1):
	print(i, end='')

	
0123456789
>>> for i in range(10,0,-1):
	print(i, end=',')

	
10,9,8,7,6,5,4,3,2,1,
>>> text[10:0:-1]
'dlroW olle'
>>> text[10::-1]
'dlroW olleH'
>>> text[::-1]
'gnimmargorp nohtyP si siht ,dlroW olleH'
>>> 
>>> text
'Hello World, this is Python programming'
>>> text[-1]
'g'
>>> text[-2]
'n'
>>> text[-3]
'i'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-1:-12:-1]
'gnimmargorp'
>>> text[-12:-1]
' programmin'
>>> text[-11:]
'programming'
>>> dir(text)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world, this is python programming'
>>> text.capitalize()
'Hello world, this is python programming'
>>> text.upper()
'HELLO WORLD, THIS IS PYTHON PROGRAMMING'
>>> text.title()
'Hello World, This Is Python Programming'
>>> text.swapcase()
'hELLO wORLD, THIS IS pYTHON PROGRAMMING'
>>> text.index('y')
22
>>> text.index('i')
15
>>> text.index('h')
14
>>> text
'Hello World, this is Python programming'
>>> text.count('o')
4
>>> text.index('o')
4
>>> text.index('o',0)
4
>>> text.index('o',1)
4
>>> text.index('o',5)
7
>>> text.index('o',8)
25
>>> text.index('o',26)
30
>>> text.find('o')
4
>>> text.find('o',5)
7
>>> text.find('o',8)
25
>>> text.index('z')
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    text.index('z')
ValueError: substring not found
>>> text.find('z')
-1
>>> text.rindex('p')
28
>>> text.rfind('o')
30
>>> text.isdigit()
False
>>> text.islower()
False
>>> text.isupper()
False
>>> text = '124 hello'
>>> text.isalnum()
False
>>> text = '124hello'
>>> text.isalnum()
True
>>> text.isdigit()
False
>>> text = "Hello World, this is Python programming"
>>> text.split()
['Hello', 'World,', 'this', 'is', 'Python', 'programming']
>>> text.split(',')
['Hello World', ' this is Python programming']
>>> textList = text.split()
>>> textList
['Hello', 'World,', 'this', 'is', 'Python', 'programming']
>>> " ".join(textList)
'Hello World, this is Python programming'
>>> "-".join(textList)
'Hello-World,-this-is-Python-programming'
>>> textList[0]
'Hello'
>>> textList[1]
'World,'
>>> textList[2]
'this'
>>> name = "    Ram Sharma    "
>>> #trim / strip
>>> name.strip()
'Ram Sharma'
>>> name = "####Ram Sharma-----"
>>> name.strip()
'####Ram Sharma-----'
>>> name.strip('#')
'Ram Sharma-----'
>>> name.strip('-')
'####Ram Sharma'
>>> name.lstrip('#')
'Ram Sharma-----'
>>> name = name.lstrip('#')
>>> name
'Ram Sharma-----'
>>> name = name.rstrip('-')
>>> name
'Ram Sharma'
>>> text
'Hello World, this is Python programming'
>>> text.startswith('H')
True
>>> text.startswith('h')
False
>>> text.startswith('W')
False
>>> text.startswith('W',5)
False
>>> text.startswith('W',6)
True
>>> text.endswith('?')
False
>>> text.endswith('.')
False
>>> text.endswith('!')
False
>>> text.endswith('g')
True
>>> text.replace('o','p')
'Hellp Wprld, this is Pythpn prpgramming'
>>> 