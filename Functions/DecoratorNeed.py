def outer(func):
    def inner():
        print("This is my inner function...")
        func()
        print("This is something else...")
    return inner

def caller():
    print("You are calling me...")

output = outer(caller)
output()