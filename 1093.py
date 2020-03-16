l = []
for i in range(23):
    l.append(0)
num = int(input())
input_list = list(map(int, input().split()))
for j in input_list:
    l[j - 1] += 1
for k in l:
    print(k, end=" ")
