list = []

for _ in range(3):
    list.append(int(input()))

if list.count(60) == 3:
    print('Equilateral')
elif sum(list) == 180 and len(dict.fromkeys(list)) == 2:
    print('Isosceles')
elif sum(list) == 180 and len(dict.fromkeys(list)) == 3:
    print('Scalene')
else:
    print('Error')