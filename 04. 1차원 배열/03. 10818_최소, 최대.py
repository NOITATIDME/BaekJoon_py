N = int(input())
data = list(map(int, input().split()))
data.sort()
print(data[0],data[N-1],end=' ')