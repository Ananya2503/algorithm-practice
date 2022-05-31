def find_number(mean, num1):
    return 2 * mean - num1

x1, s = input().split()
s = int(s)
x1 = int(x1)
print(find_number(s, x1))