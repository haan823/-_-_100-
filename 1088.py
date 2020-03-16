num = int(input())
i = 1
while True:
    if i <= num:
        if i % 3 == 0:
            i += 1
            continue
        else:
            print(i, end=" ")
            i += 1
    else:
        break
