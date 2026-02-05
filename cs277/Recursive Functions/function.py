# function 

def f(a,b):
    if b == 0:
        return 1
    if a < b:
        return 0
    return f(a-1, b) + f(a-1,b-1)

# tests

print(f(0,0)) # should print 1
print(f(0,1)) # should print 0
print(f(5,3)) 
print(f(4,6)) 