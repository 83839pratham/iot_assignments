

def maximum(a, b, c):

    if (a>b) and (a>c):
        largest =  a
    elif (b>a) and (b>c):
        largest  = b
    else:
        largest  = c
    
    return largest
a = 33
b = 11
c = 22
print(maximum(a,b,c))

