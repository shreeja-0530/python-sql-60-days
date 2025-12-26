num=int(input("Enter a number: "))
if num%2==0:
    print("Even")
else:
    print("Odd")

n=int(input("Enter a number: "))
if n<0:
    print("Negative")
elif n==0:
    print("Zero")
else:
    print("Positive")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))

if a>b and a>c:
    print("a is the largest with value ",a)
elif b>a and b>c:
    print("b is the largest with value ",b)
elif c>a and c>b:
    print("c is the largest with value ",c)
else:
    print(f"{a},{b},{c} are equal")