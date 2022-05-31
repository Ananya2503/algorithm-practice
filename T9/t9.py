def print_number(num, cha):
    for i in cha:
        if i == 'A':
            print(num[0], end=' ')
        elif i == 'B':
            print(num[1], end=' ')
        elif i == 'C':
            print(num[2], end=' ')

num = [int(x) for x in input().split()]
cha = input()
num.sort()
print_number(num, cha)