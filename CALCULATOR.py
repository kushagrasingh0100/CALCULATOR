number1= input("ENTER ANY NUMBER")
num1= int(number1)
sign= input("ENTER ANY SIGN")
number2= input("ENTER ANY NUMBER")
num2= int(number2)
if sign== "+":
    print("your result is", (num1 + num2))
elif sign == "-":
    print("your result is", (num1 - num2))
elif sign=="*":
    print("your result is", (num1*num2))
elif sign=="/":
    print("your result is", (num1/num2))
else:
    print("ENTER ANY SIGN +,-,*,/")
