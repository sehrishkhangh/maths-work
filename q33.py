'''num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)'''
print('============================== REVERSE NAME ===================================')
print('\n')

first_name=input('Enter your first name= ').title()
last_name=input('Enter your last name= ').title()
full_name=str(first_name)+str(' ')+str(last_name)
print(full_name)
print(full_name[::-1])
print('\n')
print('================================= THE END ===================================')
