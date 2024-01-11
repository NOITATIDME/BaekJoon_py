table = [[0 for _ in range(101)] for _ in range(101)]

A = int(input())

for _ in range(A):
    x, y = map(int, input().split())
    for row in range(x, x+10):
        for col in range(y, y+10):
            table[row][col] = 1

result = 0

for i in table:
    result += i.count(1)

print(result)