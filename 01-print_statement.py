a = 12
b = 33
c = a + b
d = a / b
print(c)
print("Sum is",c)
print("Sum of", a, "and", b, "is", c)

print("Sum is %d"%c)
print("Sum of %d and %d is %d"%(a,b,c))

print("Div is %f"%d)

print("Sum is {}".format(c))
print("Sum of {} and {} is {}".format(a,b,c))
print("Div of {} and {} is {}".format(a,b,d))
print("Div of {} and {} is {:.2f}".format(a,b,d))

print("Sum of {1} and {2} is {0}".format(c,a,b))

#f-strings = format-strings
print(f"Sum of {a} and {b} is {c}")

print(f"Div of {a} and {b} is {d:.2f}")







