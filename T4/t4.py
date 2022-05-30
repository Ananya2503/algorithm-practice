cha = input()
isUpper = cha.isupper()
isLower = cha.islower()

if isUpper:
    print('All Capital Letter')
elif isLower:
    print('All Small Letter')
else:
    print('Mix')