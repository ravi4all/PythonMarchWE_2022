# def checkEligibility(age):
#     return age > 18

# print(checkEligibility(45))
ageData = [12,40,42,16,71,23,15,28]
# results = list(filter(checkEligibility, ageData))
# print(results)

results = list(filter(lambda num : num % 2 == 0, ageData))
print(results)