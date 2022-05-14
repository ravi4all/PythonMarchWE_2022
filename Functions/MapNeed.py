def convert_temp(c):
    return 9/5 * c + 32

def km_to_m(km):
    return km * 1000

# c = 40.6
# f = convert_temp(c)
# print(f)
temps = [30.5,32.4,33.6,37.6,34.5,39.6,30.6]
# f = []
# for i in range(len(temps)):
#     f.append(convert_temp(temps[i]))

# print(f)

kms = [4545,45,77,122,7.8,5.4,312]
# ms = []
# for i in range(len(kms)):
#     ms.append(km_to_m(kms[i]))

# print(ms)

def converter(func, iter):
    data = []
    for i in range(len(iter)):
        data.append(func(iter[i]))
    return data

f = converter(convert_temp, temps)
print(f)

ms = converter(km_to_m, kms)
print(ms)

