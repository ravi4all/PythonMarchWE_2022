# closures : retaining state with nested functions
# closure factory function
def calc():
    x = 12
    y = 22
    def add():
        z = x + y
        return z
    
    def sub():
        z = x - y
        return z
    
    def mul():
        z = x * y
        return z

    # print(add())
    # print(sub())
    # print(mul())
    return add, sub, mul

# operations = calc()
# print(operations[0]())
# print(operations[1]())
# print(operations[2]())

add, sub, mul = calc()
print("Sum is",add())
print("Sub is",sub())

