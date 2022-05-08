def calc(x,y):
    z1 = x + y
    z2 = x - y
    z3 = x / y
    z4 = x * y
    # Packing
    return z1, z2, z3, z4

# z = calc(4,7)
# print(z)

# Unpacking
a,b,c,d = calc(4,5)
print("Sum is",a)
print("Sub is",b)