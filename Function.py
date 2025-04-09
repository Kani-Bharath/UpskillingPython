#Functions
def myFunc(n,m) :
    return n*m

print(myFunc(4,5))

#Nested functions have access to outer variables

def outer(a,b):
    c="c"
    
    def inner():
        return a+b+c
    return(inner)

print(outer("a","b"))

