import random
from datetime import datetime as dt
import webbrowser

name = input("Enter your name : ")
name = name.title()
startMessages = ["what's in your mind ?", "Ask me anything", "Enter your message ", f"Welcome {name}"]

print(random.choice(startMessages))

greetIntent = ["hi", "hello", "hey", "hey there", "hi there", "hello there"]
timeIntent = ["time", "time please", "what's the time", "tell me time", "please tell me time"]
dateIntent = ["date", "date please", "what's the date", "tell me date", "please tell me date"]

chat = True
while chat:
    msg = input(">> ")
    msg = msg.lower()
    if msg in greetIntent:
        reply = random.choice(greetIntent)
        reply = reply.title()
        print(f"{reply} {name}")
    elif msg in dateIntent:
        currentDate = dt.now().date()
        print(currentDate.strftime("%d %B, %y, %a"))
    elif msg in timeIntent:
        currentTime = dt.now().time()
        print(currentTime.strftime("%I:%M:%S, %p"))
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web+".com")
    elif msg == "bye":
        print("Bye...Take Care")
        chat = False
    else:
        print("I don't understand")
