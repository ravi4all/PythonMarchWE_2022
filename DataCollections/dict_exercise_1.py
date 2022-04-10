data = {
    "names" : ["John","Max","Sam","Nick","Tom","Jeff","Jenny"],
    "dept" : ["IT","HR","IT","IT","Sales","Sales","HR"],
    "salary" : [45000,55000,65000,25000,60000,35000,50000]
    }

'''
1. Take employee name as input from user and print his/her dept and salary
   without using loop
2. Find average salary of employees who works in IT Department
'''

emp_name = input("Enter the name of employee : ")
index = data["names"].index(emp_name)
dept = data["dept"][index]
sal = data["salary"][index]
print("Name : {}, Salary : {}, Dept : {}".format(emp_name, sal, dept))


count = 0
salary = 0
for i in range(len(data["names"])):
    if data["dept"][i] == "IT":
        count += 1
        salary += data["salary"][i]

print("Average Salary : ", salary // count)










