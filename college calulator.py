a = int(input("enter first number : "))
b = int(input("enter second number : "))
c = str(input("choose the operator (+,-,*,/) : "))
if c == '+':
    print("addition =",a+b)
elif c == '-':
    print("subtraction =",a-b)
elif c == '*':
    print("multiplication =",a*b)
elif c == '/':
    print("division =",a/b)
else:
    print("invalid choice")
