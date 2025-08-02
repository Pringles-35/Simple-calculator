print("Welcome to the Simple Calculator!")

#Choose an operation
print("Please choose an operation: +. -, *, /")
operation=input("Enter here:")

#Obtain numbers
print("Now enter your numbers")
one=float(input("Enter your first number:"))
two=float(input("Enter your second number:"))

result=None

#Perform operations
if operation=="+":
    result=one + two
elif operation=="-":
    result=one - two
elif operation=="*":
    result=one*two
elif operation=="/":
    if two != 0:
      result=one/two
    else:
        print("Cannot divide by 0")
        
else:
    print("Invalid operation")


#Show result
if result is not None:
    print("Result:",result)
