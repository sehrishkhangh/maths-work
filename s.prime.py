num1=int(input('give a number to ask'))
if num1==0 or num1==1:
    print(str(num1)+' is not prime' )
elif num1==2:
    print(str(num1)+' is  prime')
else:
    for i in range(2,num1):
        if num1%i==0:
            print(str(num1)+'is not  prime.')
            #break
        else:
            print(str(num1)+' is  prime.')



