def sum_matrix(matrix, m, n):
    result = []
    for i in range(m):
        for j in range(n):
            result.append(matrix[i][j] + matrix[i + m][j])
    return result

m, n = input().split()
m = int(m)
n = int(n)
mat = []

for i in range(2 * m):
    temp = [int(x) for x in input().split()]
    mat.append(temp)
result = sum_matrix(mat, m, n)

for i in range(len(result)):
    if i % n == 0 and i != 0:
        print(end='\n')
    print(result[i], end=' ')