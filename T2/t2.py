n = int(input())
num = []

for i in range(n):
    x = int(input())
    num.append(x)

num.sort()
print(num[0])
print(num[n - 1])