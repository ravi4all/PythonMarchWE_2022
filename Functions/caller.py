import calc

print("""
1. Add
2. Sub
3. Div
4. Mul
""")

ch = input("Enter your choice : ")

fnum = int(input("Enter first number : "))
snum = int(input("Enter second number : "))

operations = {
    "1" : calc.add,
    "2" : calc.sub,
    "3" : calc.div,
    "4" : calc.mul
}
result = operations.get(ch, calc.invalidChoice)(fnum, snum)
print("Result is",result)