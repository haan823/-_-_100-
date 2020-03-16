import io, sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf8")
word = input()
for i in word:
    print("'" + i + "'")
