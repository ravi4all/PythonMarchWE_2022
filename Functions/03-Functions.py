# *args - variable length arguments
def add(*x):
    # internally x will be of tuple type
    sum = 0
    for i in x:
        if not isinstance(i, int):
            continue
        sum += i
    print("Sum is",sum)


# add(4,5)
# add(4,5,6,"Hello")
# add(4,3,4,6,8,8,4)
# add()
# add(4)


# **kwargs - Keyword argument
def person(**details):
    # internally details will become dictionary object
    print(details)

person(name="Ram")
person(name="Ram", salary=45000, dept="IT")
person(id=101, name="Shyam", dept="HR")