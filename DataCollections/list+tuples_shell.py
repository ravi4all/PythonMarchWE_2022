Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = []
>>> data = lost()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    data = lost()
NameError: name 'lost' is not defined
>>> data = list()
>>> data = [3,4,2,3,6,'python',10.5, True]
>>> data = []
>>> data.append(10)
>>> data
[10]
>>> data.append(20)
>>> data
[10, 20]
>>> data.append(25)
>>> data.append(15)
>>> data.append(11)
>>> data
[10, 20, 25, 15, 11]
>>> data.pop()
11
>>> data
[10, 20, 25, 15]
>>> data.pop()
15
>>> data
[10, 20, 25]
>>> data.append(12,3,5,67,3,2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data.append(12,3,5,67,3,2)
TypeError: list.append() takes exactly one argument (6 given)
>>> data.append([12,3,5,67,3,2])
>>> data
[10, 20, 25, [12, 3, 5, 67, 3, 2]]
>>> data.pop()
[12, 3, 5, 67, 3, 2]
>>> data
[10, 20, 25]
>>> data.extend([12,3,5,67,3,2])
>>> data
[10, 20, 25, 12, 3, 5, 67, 3, 2]
>>> data.pop()
2
>>> data.pop(3)
12
>>> data.insert(3,13)
>>> data
[10, 20, 25, 13, 3, 5, 67, 3]
>>> data.remove(1)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    data.remove(1)
ValueError: list.remove(x): x not in list
>>> data.remove(3)
>>> data
[10, 20, 25, 13, 5, 67, 3]
>>> data.count(10)
1
>>> data.index(25)
2
>>> data.sort()
>>> data
[3, 5, 10, 13, 20, 25, 67]
>>> data.sort(reverse=True)
>>> data
[67, 25, 20, 13, 10, 5, 3]
>>> data.reverse()
>>> data
[3, 5, 10, 13, 20, 25, 67]
>>> data.clear()
>>> data
[]
>>> data = (1,3)
>>> data = 3,4,6,7,3,3,6,12,23,6
>>> data
(3, 4, 6, 7, 3, 3, 6, 12, 23, 6)
>>> data[0] = 12
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    data[0] = 12
TypeError: 'tuple' object does not support item assignment
>>> del data[0]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = [["Ram", "Shyam", "Ankit"], ["IT","IT","HR"], [45000,55000,35000], ["Delhi", "Pune", "Noida"]]
>>> data[0]
['Ram', 'Shyam', 'Ankit']
>>> data[0][0]
'Ram'
>>> 