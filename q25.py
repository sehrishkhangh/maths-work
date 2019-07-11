
your_number=int((input('Enter your number= ')))
result=0
'''while your_number>0:
    digit=your_number%10
    result=result+digit
    your_number=your_number//10
print('The sum is! ',result)'''
print(len(str(your_number)))
for i in range(len(str(your_number))):
    digit=your_number%10
    result=result+digit
    your_number=your_number//10
print('The sum is! ',result)




