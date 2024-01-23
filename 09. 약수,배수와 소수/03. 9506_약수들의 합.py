while True:
    n = int(input())
    nList = []
    if n == -1:
        break
    for i in range(1,n):
        if n % i == 0 :
            nList.append(i)

    if sum(nList) == n:
        print(n, " = ", " + ".join(str(j) for j in nList),sep="" )
    else:
        print(n, "is NOT perfect.")