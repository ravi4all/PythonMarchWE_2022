# / represents that arguments before / will be positional only
# def greet(fname, lname, /, address, pin=202020):
#     print("Welcome",fname, lname)
#     print("Address is",address)

# greet("Ram", "Sharma", "Delhi") # positional
# greet(name="Raman", lname="Tyagi", address="Noida") # keyword

# keyword or positional arguments
# greet("Shyam", "Kumar", address="Pune")

def greet(fname, lname, *, address, pin=202020):
    print("Welcome",fname, lname)
    print("Address is",address)

greet("Ram", "Sharma", address="Delhi")
