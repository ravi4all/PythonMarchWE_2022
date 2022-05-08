def outer(func):
    def inner():
        print("This is my inner function...")
        func()
        print("This is something else...")
    return inner

@outer
def caller():
    print("You are calling me...")

@outer
def sendMessage():
    print("Message Sent...")

caller()