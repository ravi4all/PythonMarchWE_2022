temps = [30.5,32.4,33.6,37.6,34.5,39.6,30.6]
kms = [4545,45,77,122,7.8,5.4,312]

f = list(map(lambda c : 9/5 * c + 32, temps))
print(f)

ms = list(map(lambda km : km * 100, kms))
print(ms)
