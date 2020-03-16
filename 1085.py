h, b, c, s = map(int, input().split())
storage = h * b * c * s / 1024 / 1024 / 8
print(round(storage, 1), end=" ")
print("MB")
