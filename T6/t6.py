from math import pi

def euclidean(radius):
    return pi * pow(radius, 2)

def taxicab(radius):
    return 2 * pow(radius, 2)

radius = float(input())
print('{:.6f}'.format(euclidean(radius)))
print('{:.6f}'.format(taxicab(radius)))