import random
lst=[]
for i in range(100):
    lst.append(random.randint(1,50))
print('\n')     
print('\n')
print('\n')
print('\n')

print('LIST= '+str(lst))
min_val=lst[0]
min_idx=0
for i in range(100):
    if min_val>lst[i]:
        min_val=lst[i]
        min_idx=i


print('MINIMUM VALUE: '+ str(min_val))
print('MINIMUM INDEX: '+str(min_idx))
max_val=lst[0]
max_idx=0
for i in range(100):
        if max_val<lst[i]:
           max_val=lst[i]
           max_idx=i
print('MAXIMUM VALUE: '+str(max_val))
print('MAXIMUM INDEX: '+str(max_idx))
