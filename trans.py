# Python Program to Find the transpose of a given matrix
# Written by Siddarda Gowtham
def transpose(mat, r, c):
    res = [[0] * c] * r
    n = r
    m = c
    for i in range(n):
        for j in range(m):
            res[i][j] = mat[j][i]
            print(res[i][j], end=' ')
        print()
    return
r = int(input("Enter No.of rows:"))
c = int(input("Enter No.of Columns:"))
mat = []
res = [[0] * c] * r
print("Enter Array Elements")
for i in range(c):
    a = []
    for j in range(r):
        a.append(int(input()))
    mat.append(a)
for i in range(c):
    for j in range(r):
        print(mat[i][j], end=' ')
    print()
print("Transpose of a given matrix:")
transpose(mat, r, c)
#Copyrights Belong To Siddarda Gowtham
