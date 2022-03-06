Python 3.9.7 (tags/v3.9.7:1016ef3, Aug 30 2021, 20:19:38) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: D:/Batches/2022/Feb Python WE/data_types.py =============
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/data_types.py
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
(2+3j) is type of <class 'complex'>
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/data_types.py
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/data_types.py
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
b'Hello how are you ?'
>>> type(eng_msg)
<class 'str'>
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/data_types.py
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
b'Hello how are you ?'
>>> type(eng_msg)
<class 'bytes'>
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/data_types.py
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
b'Hello how are you ?'
Encoded : b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 \xe0\xa4\xae\xe0\xa5\x88\xe0\xa4\x82 \xe0\xa4\xa0\xe0\xa5\x80\xe0\xa4\x95 \xe0\xa4\xb9\xe0\xa5\x82\xe0\xa4\x81 \xe0\xa4\xa7\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa6'
>>> hindi_msg.decode()
'नमस्ते आप कैसे हैं मैं ठीक हूँ धन्यवाद'
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/data_types.py
12 is type of <class 'int'>
10.5 is type of <class 'float'>
(2+3j) is type of <class 'complex'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
hello is type of <class 'str'>
b'Hello how are you ?'
Encoded : b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 \xe0\xa4\xae\xe0\xa5\x88\xe0\xa4\x82 \xe0\xa4\xa0\xe0\xa5\x80\xe0\xa4\x95 \xe0\xa4\xb9\xe0\xa5\x82\xe0\xa4\x81 \xe0\xa4\xa7\xe0\xa4\xa8\xe0\xa5\x8d\xe0\xa4\xaf\xe0\xa4\xb5\xe0\xa4\xbe\xe0\xa4\xa6'
True is type of <class 'bool'>
>>> x = 10
>>> import sys
>>> sys.getsizeof(x)
28
>>> x = 100000
>>> sys.getsizeof(x)
28
>>> x = 100000000
>>> sys.getsizeof(x)
28
>>> x = 121021020102102102
>>> sys.getsizeof(x)
32
>>> 2 ** 32
4294967296
>>> 2 ** 64
18446744073709551616
>>> x = 4294967296
>>> sys.getsizeof(x)
32
>>> x = 4294967295
>>> sys.getsizeof(x)
32
>>> x = 429496729
>>> sys.getsizeof(x)
28
>>> 2 ** 31
2147483648
>>> 2 ** 63
9223372036854775808
>>> 2 ** 15
32768
>>> import time
>>> time.ctime()
'Sun Mar  6 11:00:57 2022'
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2022, 3, 6, 11, 1, 14, 572531)
>>> type(datetime.now())
<class 'datetime.datetime'>
>>> 
= RESTART: D:/Batches/2022/Feb Python WE/loop_introduction.py
0
1
2
3
4
Loop Exit
>>> 