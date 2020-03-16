num = input()
for i, v in enumerate(num):
    j = len(num) - i - 1
    for k in range(j):
        v += "0"
    print("[" + v + "]")
