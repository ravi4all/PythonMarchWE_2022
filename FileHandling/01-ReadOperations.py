try:
    file = open('file_2.txt')
    data = file.read("hello")
    # print(data)

    # file.seek(50)
    # data = file.read(100)
    # print(data)

    # line = file.readline()
    lines = file.readlines()
    print(lines)
except FileNotFoundError:
    print("File Not Found...")
    file = open('file_2.txt', 'x')
except TypeError:
    print("Some error...")
finally:
    file.close()
# finally:
#     try:
#         file.close()
#     except NameError:
#         print("File Not Exists...")