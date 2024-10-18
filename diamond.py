n=3
for i in range(n):
    for j in range(i,n):
        print(' ',end='')
    for k in range(i+1):
        print('*',end='')
    for l in range(i):
        print('*',end='')
print()
for m in range(n-1):
    for o in range(m+2):
        print(' ',end='')
    for p in range(n-m-1):
        print('*',end='')
    for q in range(n-m-2):
        print('*',end='')
print()