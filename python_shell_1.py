Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_1.py ===========
15
Traceback (most recent call last):
  File "D:/Batches/2022/Feb Python WE/Backup_codes/code_1.py", line 5, in <module>
    print(k)
NameError: name 'k' is not defined
>>> 2 ** 15
32768
>>> x = 12
>>> type(x)
<class 'int'>
>>> x = "hello"
>>> type(x)
<class 'str'>
>>> x = 10.55
>>> type(x)
<class 'float'>
>>> 
=========== RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_1.py ===========
15
Sum is 15
Sum of 12 and 3 is 15
Sum of {} and {} is {}
>>> 
=========== RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_1.py ===========
15
Sum is 15
Sum of 12 and 3 is 15
Sum of 12 and 3 is 15
>>> name = "Ram"
>>> salary = 45000
>>> msg = "Hello "+ name + "Your salary is " + salary
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    msg = "Hello "+ name + "Your salary is " + salary
TypeError: can only concatenate str (not "int") to str
>>> 10 + "10"
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    10 + "10"
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(10) + "10"
'1010'
>>> msg = "Hello {}, Your salary is {}"
>>> msg
'Hello {}, Your salary is {}'
>>> msg = "Hello {}, Your salary is {}".format(name, salary)
>>> msg
'Hello Ram, Your salary is 45000'
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_1.py
15
Sum is 15
Sum of 12 and 3 is 15
Sum of 12 and 3 is 15
Sum of {x} and {y} is {z}
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_1.py
15
Sum is 15
Sum of 12 and 3 is 15
Sum of 12 and 3 is 15
Sum of 12 and 3 is 15
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_2.py
Sum is 11
Sub is -1
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_2.py

Sum is 11
Sub is -1
Div is 0.8333333333333334
Mul is 30

>>> 
= RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_2.py

Sum is 11
Sub is -1
Div is 0.83
Mul is 30

>>> 
= RESTART: D:/Batches/2022/Feb Python WE/Backup_codes/code_2.py

Sum is 11
Sub is -1
Div is 0.83
Mul is 30

>>> lat = 23.55
>>> lon = 27.88
>>> url = "https://www.weather.com/lat="+lat
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    url = "https://www.weather.com/lat="+lat
TypeError: can only concatenate str (not "float") to str
>>> url = "https://www.weather.com/lat="+str(lat)+"&lon="+str(lon)
>>> url
'https://www.weather.com/lat=23.55&lon=27.88'
>>> url = "https://www.weather.com/lat={}&lon={}".format(lat, lon)
>>> url
'https://www.weather.com/lat=23.55&lon=27.88'
>>> url = f"https://www.weather.com/lat={lat}&lon={lon}"
>>> url
'https://www.weather.com/lat=23.55&lon=27.88'
>>> path = "D:\trainings\ncu_dsa"
>>> path
'D:\trainings\ncu_dsa'
>>> print(path)
D:	rainings
cu_dsa
>>> text = "hello world"
>>> print(text)
hello world
>>> text = "hello "
""
>>> text = "hello "world""
SyntaxError: invalid syntax
>>> text = 'hello "world"'
>>> print(text)
hello "world"
>>> text = """hello "world""""
SyntaxError: EOL while scanning string literal
>>> text = 'hello "world"'
>>> print(text)
hello "world"
>>> text = "hello \nworld"
>>> print(text)
hello 
world
>>> text = "hello \\nworld"
>>> print(text)
hello \nworld
>>> text = "hello \"world\""
>>> print(text)
hello "world"
>>> path = "D:\\trainings\\ncu_dsa"
>>> print(path)
D:\trainings\ncu_dsa
>>> path
'D:\\trainings\\ncu_dsa'
>>> path = "D:/Trainings/NCU_DevOps/Maven/maven_docker/src/main/java/com/bmpl/maven_docker"
>>> path
'D:/Trainings/NCU_DevOps/Maven/maven_docker/src/main/java/com/bmpl/maven_docker'
>>> path = r"D:\Trainings\NCU_DevOps\Maven\maven_docker\src\main\java\com\bmpl\maven_docker"
>>> path
'D:\\Trainings\\NCU_DevOps\\Maven\\maven_docker\\src\\main\\java\\com\\bmpl\\maven_docker'
>>> #r - raw string
>>> 