print('================================DIFFERENCE BETWEEN DAATES=======================================')
print('\n')

date1=int(input('Kindly give your first date you have! '))
date2=int(input('Kindly give your other date you have! '))
differeence=int(date1-date2)
if date1<date2:
    print('The difference between the dates is = ', str(-differeence))
else:
    print('The difference between the dates is = ', str(differeence))


    