'''
    *
   ***
  *****
 *******
*********
'''
n = 10
'''
for i in range(n):
    for j in range(n-i):
        print(' ', end='')
    for k in range(2 * i + 1):
        print('*', end='')
    print()
'''

# Reverse Pyramid
for i in range(n):
    for z in range(i):
        print(' ',end='')
    for y in range(n*2-(2*i+1)):
        print ('*',end ='')
    print ()


# Floyd Triangle
'''
    1
   2 3
  4 5 6
 7 8 9 10
'''
'''
x = 0
for i in range(4):
    for j in range(4 - i):
        print(' ', end='')
    for k in range(i+1):
        x += 1
        print(x, end=' ')
    print()
'''

#Reverse Floyd
x = 11
for i in range(4):
    for z in range(i):
        print(' ',end='')
    for y in range(4-i):
        x -= 1
        print (x,end =' ')
    print ()







