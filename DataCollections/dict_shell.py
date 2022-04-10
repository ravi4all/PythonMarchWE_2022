Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> data = [3,4,6]
>>> data.extend([1,2,'h'])
>>> data
[3, 4, 6, 1, 2, 'h']
>>> data = [3,5,7,7,3,3,6,12]
>>> for i in range(len(data)):
	print(data[i])

	
3
5
7
7
3
3
6
12
>>> for i in range(len(data)):
	print(i,":",data[i])

	
0 : 3
1 : 5
2 : 7
3 : 7
4 : 3
5 : 3
6 : 6
7 : 12
>>> for item in data:
	print(item)

	
3
5
7
7
3
3
6
12
>>> data = [[12,34,5,7],[2,4,6,7],[16,8,8,3]]
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[i][j], end=',')
	print()

	
12,34,5,7,
2,4,6,7,
16,8,8,3,
>>> for i in range(len(data)):
	for j in range(len(data[i])):
		print(data[j][i], end=',')
	print()

	
12,2,16,Traceback (most recent call last):
  File "<pyshell#19>", line 3, in <module>
    print(data[j][i], end=',')
IndexError: list index out of range
>>> for i in range(len(data)):
	for j in range(len(data)):
		print(data[j][i], end=',')
	print()

	
12,2,16,
34,4,8,
5,6,8,
>>> for i in range(len(data[0])):
	for j in range(len(data)):
		print(data[j][i], end=',')
	print()

	
12,2,16,
34,4,8,
5,6,8,
7,7,3,
>>> even = []
>>> for i in range(1,51):
	if i % 2 == 0:
		even.append(i)

		
>>> even
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

>>> even.extend(4)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    even.extend(4)
TypeError: 'int' object is not iterable
>>> data = [i for i in range(1,11)]
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> data = []
>>> for i in range(1,11):
	data.append(i)

	
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> data = [i for i in range(1,11)]
>>> data
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> data = [i ** 2 for i in range(1,11)]
>>> data
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> data = [i for i in range(1,51) if i % 2 == 0]
>>> data
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]
>>> data = {'name' : 'John', 'salary' : 45000, 'dept' : 'IT', 'address' : 'Delhi'}
>>> data
{'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    data[0]
KeyError: 0
>>> data['name']
'John'
>>> data['salary']
45000
>>> data['']
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    data['']
KeyError: ''
>>> data['phone'] = 89798779009
>>> data
{'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi', 'phone': 89798779009}
>>> data['email']
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    data['email']
KeyError: 'email'
>>> data.keys()
dict_keys(['name', 'salary', 'dept', 'address', 'phone'])
>>> data.values()
dict_values(['John', 45000, 'IT', 'Delhi', 89798779009])
>>> data.items()
dict_items([('name', 'John'), ('salary', 45000), ('dept', 'IT'), ('address', 'Delhi'), ('phone', 89798779009)])
>>> data.get('name')
'John'
>>> data['name']
'John'
>>> data.get('email')
>>> data.get('email', 'Not available')
'Not available'
>>> data.get('phone', 'Not available')
89798779009
>>> data.popitem()
('phone', 89798779009)
>>> data
{'name': 'John', 'salary': 45000, 'dept': 'IT', 'address': 'Delhi'}
>>> data.pop('dept')
'IT'
>>> data
{'name': 'John', 'salary': 45000, 'address': 'Delhi'}
>>> data.update({'phone':678787878, 'email':'john@gmail.com'})
>>> data
{'name': 'John', 'salary': 45000, 'address': 'Delhi', 'phone': 678787878, 'email': 'john@gmail.com'}
>>> data['salary'] = 55000
>>> data
{'name': 'John', 'salary': 55000, 'address': 'Delhi', 'phone': 678787878, 'email': 'john@gmail.com'}
>>> for item in dataL
SyntaxError: invalid syntax
>>> for item in data:
	print(item)

	
name
salary
address
phone
email
>>> for item in data:
	print(item, data[item])

	
name John
salary 55000
address Delhi
phone 678787878
email john@gmail.com
>>> for item in data:
	print(item, ":", data[item])

	
name : John
salary : 55000
address : Delhi
phone : 678787878
email : john@gmail.com
>>> 
=== RESTART: D:/Batches/2022/Feb Python WE/DataCollections/dict_exercise_1.py ==
>>> data
{'names': ['John', 'Max', 'Sam', 'Nick', 'Tom', 'Jeff', 'Jenny'], 'dept': ['IT', 'HR', 'IT', 'IT', 'Sales', 'Sales', 'HR'], 'salary': [45000, 55000, 65000, 25000, 60000, 35000, 50000]}
>>> data["names"]
['John', 'Max', 'Sam', 'Nick', 'Tom', 'Jeff', 'Jenny']
>>> 
>>> data["salary"]
[45000, 55000, 65000, 25000, 60000, 35000, 50000]
>>> 
=== RESTART: D:/Batches/2022/Feb Python WE/DataCollections/dict_exercise_1.py ==
Enter the name of employee : Tom
Name : Tom, Salary : 60000, Dept : Sales
>>> indexes = [i for i in range(len(data ["dept"])) if data ["dept"] == "IT"]
>>> indexes
[]
>>> indexes = [i for i in range(len(data ["dept"])) if data["dept"][i] == "IT"]
>>> indexes
[0, 2, 3]
>>> 
=== RESTART: D:/Batches/2022/Feb Python WE/DataCollections/dict_exercise_1.py ==
Enter the name of employee : John
Name : John, Salary : 45000, Dept : IT
Average Salary :  45000
>>> 