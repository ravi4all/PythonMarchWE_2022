'''
x = 10
while x > 0:
    print(x)
    x -= 1
'''

x = 10
flag = True
while flag:
    print(x)
    if x == 1:
        flag = False
    x -= 1
    print(flag)
