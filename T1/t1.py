def grade(score, midterm, final):
    total = score + midterm + final
    if total >= 80:
        return 'A'
    elif total <= 79 and total >= 75:
        return 'B+'
    elif total <= 74 and total >= 70:
        return 'B'
    elif total <= 69 and total >= 65:
        return 'C+'
    elif total <= 64 and total >= 60:
        return 'C'
    elif total <= 59 and total >= 55:
        return 'D+'
    elif total <= 54 and total >= 50:
        return 'D'
    elif total <= 49:
        return 'F'

score = int(input())
midterm = int(input())
final = int(input())
print(grade(score, midterm, final))