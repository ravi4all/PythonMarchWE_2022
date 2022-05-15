# w mode 
# - create file if file do not exists
# - overwrite the file if file already exists
# file = open('file_3.txt', 'w')
# data = "Hello how are you ?"
# data = "Hope everything is fine..."
# file.write(data)
# file.close()


# x mode
# - always creates a new file
# - if file already exists then raise error
file = open('file_3.txt', 'x')
data = "Hope everything is fine..."
file.write(data)
file.close()





