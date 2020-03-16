l = [[int(x) for x in input().split()] for y in range(10)]
i = 1
j = 1
if l[i][j] == 2:
    l[i][j] = 9
else:
    l[i][j] = 9
    while True:
        if l[i][j + 1] == 0:
            l[i][j + 1] = 9
            j = j + 1
        elif l[i][j + 1] == 2:
            l[i][j + 1] = 9
            break
        elif l[i + 1][j] == 0:
            l[i + 1][j] = 9
            i = i + 1
        elif l[i + 1][j] == 2:
            l[i + 1][j] = 9
            break
        else:
            break

for i in l:
    for j in i:
        print(j, end=" ")
    print()
