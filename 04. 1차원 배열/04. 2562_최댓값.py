data = []
for _ in range(9):
    num = int(input())
    data.append(num)


print(max(data))
print(data.index(max(data))+1)