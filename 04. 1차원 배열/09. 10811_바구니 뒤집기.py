N, M = map(int,input().split())
data = [i+1 for i in range(N)]

for n in range(M):
    i, j = map(int, input().split())
    temp = data[i-1:j]
    temp.reverse()
    data[i-1:j] = temp

for i in range(N):
    print(data[i],end=" ")