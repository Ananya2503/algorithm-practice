from math import sqrt

def pythagorus(a, b):
    pow_c = pow(a, 2) + pow(b, 2)
    return sqrt(pow_c)

a, b = input().split()
a = float(a)
b = float(b)
result = pythagorus(a, b)
print('{:.6f}'.format(result))