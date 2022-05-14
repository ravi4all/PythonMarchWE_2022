try:
    name = input("Enter your Name : ")
    fnum = int(input("Enter first num : "))
    snum = int(input("Enter second num : "))

    add = fnum + snum
    sub = fnum - snum
    div = fnum / snum
    mul = fnum * snum

    # name[0] = 'X'

except ZeroDivisionError:
    print("Cannot divide by zero...")

except ValueError:
    print("Invalid Input...Please enter a valid number")

except BaseException as ex:
    print("Some Error : ",ex)

else:
    print("Addition is :",add)
    print("Subtraction is :",sub)
    print("Division is :",div)
    print("Multiplication is :",mul)

finally:
    print("I will always execute...")
    print("Thankyou for using this Calc...")
