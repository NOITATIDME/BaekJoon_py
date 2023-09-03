data = []

for _ in range(10):
    num = int(input())
    n = num % 42
    data.append(n)

print(len(set(data)))
