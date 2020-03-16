h, w = map(int, input().split())
l = [[0 for x in range(w)] for y in range(h)]
n = int(input())
input_list = [[int(x) for x in input().split()] for y in range(n)]
for k in input_list:
    for j, v1 in enumerate(l):
        for i, v2 in enumerate(v1):
            if j == k[2] - 1 and i == k[3] - 1:
                if k[1] == 0:
                    for m in range(k[0]):
                        l[j][i + m] = 1
                elif k[1] == 1:
                    for m in range(k[0]):
                        l[j + m][i] = 1
for i in l:
    for j in i:
        print(j, end=" ")
    print()

