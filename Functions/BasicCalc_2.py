def calc(x, y, opr):
    expression = x + opr + y
    result = eval(expression)
    print("Result is",result)

def invalidChoice(*args, **kwargs):
    print("Invalid Choice...")

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

fnum = input("Enter first number : ")
snum = input("Enter second number : ")

operators = {
    "1" : "+",
    "2" : "-",
    "3" : "/",
    "4" : "*"
}
opr = operators.get(ch)
calc(fnum, snum, opr)