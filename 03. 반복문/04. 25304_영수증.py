##첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
X = int(input())
## 둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N 이 주어진다.
N = int(input())
## 이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.
total = 0
cost = 0
print(N)
for i in range(N+1):
    a, b = map(int, input().split())
    cost = a * b
    total += cost

if(total == X):
    print('YES')

#else if(total != X):
#   print('NO')
#else:

#    print(total)
#    print(i)