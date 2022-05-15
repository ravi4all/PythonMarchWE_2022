file = open('sachin-tendulkar-52.jpg', 'rb')
data = file.read()
# print(data)
file.close()

file = open('sachin-tendulkar-52-copy.jpg', 'wb')
file.write(data)
file.close()