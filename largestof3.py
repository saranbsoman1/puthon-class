input("largest of 3 nos")
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
if ((a>b)&(a>c)):
    print(a)
elif ((b>c)&(b>a)):
    print(b)
else:
    print(c)