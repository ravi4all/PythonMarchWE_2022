import random

name = input("Enter your name : ")

startMessages = ["what's in your mind ?", "Ask me anything", "Enter your message ", f"Welcome {name}"]

print(random.choice(startMessages))

chat = True
while chat:
    msg = input(">> ")

    if msg == "hello":
        print(f"Hello {name}...")
    elif msg == "bye":
        print("Bye...Take Care")
        chat = False
    else:
        print("I don't understand")
