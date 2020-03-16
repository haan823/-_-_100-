i = "0x" + input()
for j in range(1, int("F", 16) + 1):
    print(
        format(int(i, 16), "X")
        + "*"
        + format(j, "X")
        + "="
        + format(int(i, 16) * j, "X")
    )
