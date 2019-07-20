#q..1
'''year=int(input('Your year'))
if year%4==0 or year%400==0:
    print('it is a leap year')'''
#q..2
'''cow=4 
pig=4
chicken=2
your_chicken=int(input('Your given chicken'))
your_pig=int(input('Your given pig'))
your_cow=int(input('Your given cow'))
l=[your_chicken*chicken,your_pig*pig,your_cow*cow]
print(l)'''
#q..3
'''fiction={
    'A':'comedy',
    'B':'comic or graphic novel',
    'C':'science fiction',
    'D':'fantasy',
    'E':'historical fiction'
}
non_fiction={
    'F':'history and geography',
    'G':'arts',
    'H':'science and technology',
    'I':'other',
}
choice=int(input('Your choice?'))
if choice==1:
    choice_books=input('Your books interest')
    
    for k,v in fiction.items():
        if choice_books.lower()==v.lower():
            print(k)
            

        #print(fiction[k])'''

#q..4
'''score=[]
count=int(input('Paarticipents'))
for x in range(0,count):
    scores=int(input('Scores'))
    score.append(scores)
    print(score)
maximum=max(score)
print(maximum)
x=score.sort(reverse=True)
if len(score)>1:
    print(score[1])'''
#q..6
print('============================================== QUESTION #6 =====================================================')
password=input('Input your password:')
length=len(password)
flag=True
while flag==True:
    if length>=6 and length<=24:
        print('move to next step.')
    else:
        print('We cant move further.')
        break
    flag=False 
    abcd=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R''S','T','U','V','W','X','Y','Z']
    for i in abcd:
        if i in password:
            print('We have an uppercase letter.')
            break
    else:
        print('We cant move further.')
    flag=False
    other_abcd=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for J in other_abcd:
        if J in password:
            print('We have a lowercase letter.')
            break
    else:
        print('We cant move further.')
    flag=False
    a=str(1)
    b=str(2)
    c=str(3)
    d=str(4)
    e=str(5)
    f=str(6)
    g=str(7)
    h=str(8)
    i=str(9)
    j=str(0)
    counting=[a,b,c,d,e,f,g,h,i,j]
    for z in counting:
        if z in password:
            print('We have a counting element.')
            break
    else:
        print('We cant move further.')
    flag=False
    counter=0
    character1=input('Give your alphabet= ')
    character2=int(input('Give your number= '))
    if password.count(character1)<=2:
        print('We have a character repeating 2 times.')
    elif password.count(character2)<=2:
         print('We have a character repeating maximumly 2 times.')
    else:
        print('Sorry! We dont have repeating character maximumly two times.')
    flag=False

            
    