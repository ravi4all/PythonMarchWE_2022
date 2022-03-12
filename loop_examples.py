#Sum of n natural numbers
'''
n = 10
sum = 0
for i in range(1,n+1):
    sum += i

print("Sum is",sum)
'''

#Multiplication Table of a Number
'''
I/p : 6
O/p : 6 x 1 = 6
      6 x 2 = 12
'''
'''
num = int(input("Enter a number : "))
for i in range(1,11):
    print(f"{num} x {i} = {num * i}")
'''

'''
Print a Pattern
*
**
***
****
*****
'''
for i in range(1,6):
    print('*' * i)

'''
Print a Pattern
    *
   ***
  *****
 *******
*********
'''
n = 10
for i in range(n):
    print(' ' * (n - i) + '*' * (2*i+1))









