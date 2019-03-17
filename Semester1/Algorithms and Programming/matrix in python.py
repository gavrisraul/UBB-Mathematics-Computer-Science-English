r=int(input())
c=int(input())
mat=[]
for i in range(r):
    mat.append([])
    for j in range(c):
        x=int(input())
        mat[i].append(x)

for i in range(r):
    print(mat[i])
    for j in range(c):
        continue
