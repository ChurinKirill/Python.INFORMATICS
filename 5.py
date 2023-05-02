a, b = map(int, input().split())
a += a % 2
s = 0
for i in range(a, b + 1, 2):
    s += i
print(s)