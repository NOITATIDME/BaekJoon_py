N = int(input())
data = list(map(int,input().split()))

maxnum = max(data)
newlist = []
for score in data:
    newlist.append(score / maxnum * 100)

mean = sum(newlist) / N

print(mean)