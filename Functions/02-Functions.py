# Positional Arguments
# def greet(fname, lname):
#     print("Hello", fname, lname)

# greet("Ram", "Sharma")

# Default Arguments
def greet(fname, lname="", address="Delhi"):
    print("Hello", fname, lname)
    print("Location is",address)

greet("Ram", "Sharma")
greet("Ram")
greet("Ram", "Sharma", "Noida")

# Keyword arguments
greet(fname="Ram")
greet(fname="Ram", address="Noida")
greet(address="Pune", fname="Ram", lname="Sharma")