l = [[int(x) for x in input().split()] for y in range(19)]
num = int(input())
input_list = [[int(x) for x in input().split()] for y in range(num)]
for i in input_list:
    for j, v1 in enumerate(l):
        for k, v2 in enumerate(v1):
            if k == i[1] - 1:
                l[j][k] = (v2 + 1) % 2
            if j == i[0] - 1:
                for x in v1:
                    l[j][k] = (l[j][k] + 1) % 2
for i in l:
    for j in i:
        print(j, end=" ")
    print()
