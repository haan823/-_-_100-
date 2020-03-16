num = int(input())
input_list = list(map(int, input().split()))
min = 24
for i in input_list:
    if i < min:
        min = i
print(min)
