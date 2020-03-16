w, h, b = map(int, input().split())
storage = w * h * b / 1024 / 1024 / 8
print("%.2f" % round(storage, 2), end=" ")
print("MB")
