num = int(input())
l = []
for i in range(19):
    l.append([])
    for j in range(19):
        l[i].append(0)
input_list = []
for i in range(num):
    input_list = list(map(int, input().split()))
    l[input_list[0] - 1][input_list[1] - 1] = 1
for i in l:
    for j in i:
        print(j, end=" ")
    print()

