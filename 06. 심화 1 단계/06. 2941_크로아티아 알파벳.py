cAlpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']
croatiaWord = input()
for c in cAlpha:
    croatiaWord = croatiaWord.replace(c,'*')

print(len(croatiaWord))