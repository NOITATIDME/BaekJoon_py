A, B = map(str, input().split())

#A = int(A[2] + A[1] + A[0])
#B = int(B[2] + B[1] + B[0])
A = int(A[::-1])
B = int(B[::-1])
if A > B:
    print(A)
else:
    print(B)