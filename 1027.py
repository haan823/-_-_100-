date = list(map(int, input().split(".")))
print("%02d" % date[2], end="-")
print("%02d" % date[1], end="-")
print("%04d" % date[0])
