data = [i for i in range(1, 31)]

for _ in range(28):
    num = int(input())
    data.remove(num)

print(min(data))
print(max(data))