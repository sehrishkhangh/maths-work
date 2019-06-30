
print('\n')
print('\n')
op=input('operation')
nmbr1=int(input('#1'))
nmbr2=int(input('#2'))
print('\n')
print('\n')
   
print(str(nmbr1)+op+str(nmbr2))

ans1=int(nmbr1+nmbr2)
ans2=int(nmbr1-nmbr2)
ans3=int(nmbr1*nmbr2)
ans4=int(nmbr1/nmbr2)
if op == '+':
    print('                  '+str(ans1))
elif op == '-':
    print('                  '+str(ans2))
elif op=='*':
    print('                  '+str(ans3))
else:

    print('                  '+str(ans4))


print('\n')
print('7           8        9     DEL')
print('4           5        6       /')
print('1           2        3       *')
print('.           0        =       +')



