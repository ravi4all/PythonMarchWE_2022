#Nested Loop
'''
for i in range(5):
    for j in range(5):
        print(i,j)
'''

'''
*****
*****
*****
*****
*****
'''
'''
for i in range(5):
    for j in range(5):
        print('*', end='')
    print()
'''

'''
*
**
***
****
*****
'''
'''
for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()
'''


'''
*****
****
***
**
*
'''
for i in range(5):
    for j in range(5-i):
        print('*', end='')
    print()


'''
1
23
456
78910
'''
k = 0
for i in range(4):
    for j in range(i+1):
        k += 1
        print(k, end='')
    print()

