n = int(input())
cnt = 0
for i in range (100, 1000):
    if i % 10 + i // 10 % 10 + i // 100 % 10 == n:
        cnt += 1
print(cnt)