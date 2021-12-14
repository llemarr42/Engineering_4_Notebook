from math import sqrt

def doMath(a,b,c):
    d = (b**2)-(4*a*c)
    if d > 0:
        root1 = round((-b + sqrt(b**2 - 4*a*c))/(2*a))
        root2 = round((-b - sqrt(b**2 - 4*a*c))/(2*a))
        Roots = [root1, root2]
    elif d == 0:
        root1 = round((-b + sqrt(b**2 - 4*a*c))/(2*a))
        Roots = root1
    elif d < 0:
        Roots = ""
    return Roots

x=input("press enter to continue")
print(x)


while x=="":
    print("Quadratratic Solver")
    print("Enter the coefficients for ax^2+bx+c=0")
    a=int(input("Enter coefficient a:"))
    print(a)
    b=int(input("Enter coefficient b:"))
    print(b)
    c=int(input("Enter coefficient c:"))
    print(c)
    print("%sx^2+%sx+%s=0" % (a,b,c))
   
    Roots = doMath(a,b,c)
   
    if len(Roots) == 2:
        print("1st root:\t" + str(Roots[0]))
        print("1st root:\t" + str(Roots[1]))
        print("Vertex form:\t {0}(x+{1})^2)+{2}" .format(a,one,two))
    elif len(Roots) == 1:
        print("1st root:\t" + str(Roots[0]))
        print("Vertex form:\t {0}(x+{1})^2)+{2}" .format(a,one,two))

    else:
        print("There Are No Real Roots")
    one = -1*(b/(2*a))
    two = c-(b**2)/(4*a)
   
    x=input("press enter to continue or 'x' to close")
    print(x)

        
