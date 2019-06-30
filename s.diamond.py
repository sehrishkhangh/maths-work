print('\n')
print('\n')

print('===============================================DIAMOND SHAPE===================================================')
print('\n')


l=5
k=5
for i in range(1,6):
    for j in range(1,k):
        print(end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
    k=k-1
for i in range(1,5):
    for j in range(i):
        print(end=' ')
    for j in range(1,l):
        print('*',end=' ')
    print()
    l=l-1

'''n=5
for i in range(1,n+1):
    for j in range(n-i+1):
        print(end=' ')
    for j in range(i):
        print('*',end=' ')
    print()
for i in range(n-1,0,-1):
    for j in range(n-i+1):
        print(end=' ')
    for j in range(i):
        print('*',end=' ')
    print()'''