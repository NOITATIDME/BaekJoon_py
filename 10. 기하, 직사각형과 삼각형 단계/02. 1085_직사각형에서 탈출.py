x,y,w,h = map(int, input().split())

list = []

list.append(abs(0-x))
list.append(abs(w-x))

list.append(abs(0-y))
list.append(abs(h-y))

print(min(list))