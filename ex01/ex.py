row,col = map(int,input().split())
matrix = []
for i in range(row):
    matrix.append(list(input()))
for i in range(row):
    for j in range(col):
        if (matrix[i][j] != '*'):
            matrix[i][j] = 0
            for x in range(i-1,i+2):
                for y in range(j-1,j+2):
                    if not (y<0 or x<0 or y >=row or x>=col):
                        if matrix[i][j] != '*' and matrix[x][y] == '*':
                            matrix[i][j] += 1
        else:
            continue
for i in matrix:
    for j in i:
        print(j,end = '')
    print()
