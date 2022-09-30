def SquareIt(x):
    return x*x

print (SquareIt(44))


def square(f,x):
    return f(x)

print (square(SquareIt,5))

print (square(lambda x: x*x*x,3))

def prime(x):
    for i in range (2,(int)((x/2+2)/2)):
        if (x%i==0):
            return -1
            break



ts=[23,33,21,321,421,421,123,41,424,23,42,1,424,213,421]
for xa in ts:
    ch=prime(xa)
    if (ch!= -1 and ((xa!=0) and (xa!=1))):
        print (xa)