

def add(x,y):
    
    z = x + y

    add(x-1,y-1)

    return z

a = 6
b = 8

s = add(b,a)
print(s)


