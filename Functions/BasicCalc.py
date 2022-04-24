def add(x, y):
    z = x + y
    print("Sum is",z)

def sub(x, y):
    z = x - y
    print("Sub is",z)

def div(x, y):
    z = x / y
    print("Div is",z)

def mul(x, y):
    z = x * y
    print("Mul is",z)

def invalidChoice(*args, **kwargs):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

# operations = [add, sub, div, mul]
# operations[int(ch) - 1](fnum, snum)

operations = {
    "1" : add,
    "2" : sub,
    "3" : div,
    "4" : mul
}
operations.get(ch, invalidChoice)(fnum, snum)