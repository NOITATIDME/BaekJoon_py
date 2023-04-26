# 윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.

A = int(input())

A1 = A % 4
A2 = A % 100
A3 = A % 400

if A1 == 0 and A2 != 0:
    print(1)
elif A3 == 0:
    print(1)
else :
    print(0)