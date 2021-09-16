# Calculator

# Written by [Loren Lemarr]

print("calculator program")

x=input("press enter to continue")
print(x)

while x=="":
    a = int(input("enter your first number:"))
    print(a)
    b = int(input("enter your second number:"))
    print(b)
    def doMath(a,b,c):
        if c==1:
            return str(a+b)
        if c==2:
            return str(a-b)
        if c==3:
            return str(a*b)
        if c==4:
            return str(round(a/b))
        if c==5:
            return str(a%b)
        if c==6:
            d=a
            factone=a*d
            while d!=0:
                d = d-1
                if d!=0:
                    factone = factone*d
            return str(factone)
        if c==7:
             d=b
             facttwo=b*d
             while d!=0:
                d = d-1
                if d!=0:
                    facttwo = facttwo*d
             return str(facttwo)
    
    print("Sum:\t\t" + doMath(a,b,1))
    print("Difference:\t" + doMath(a,b,2))
    print("Product:\t" + doMath(a,b,3))
    print("Quotient:\t" + doMath(a,b,4))
    print("Modulo:\t\t" + doMath(a,b,5))
    print("1st Factorial:\t" + doMath(a,b,6))
    print("2nd Factorial:\t" + doMath(a,b,7))
    x=input("press X to end or enter to continue")
    print(x)
