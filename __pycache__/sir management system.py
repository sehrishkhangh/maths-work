print('=================================================================================================================================================')
students=[]
while True:
    print('Press 1 to add student')
    print('Press 2 to del student')
    print('Press 3 to find the student actual value')
    print('Press 4 to changing in student profile')
    print('Press 5 to take exit from thee system= ')
    choice=int(input('Write your desired act! '))
    if choice==1:
        student={}
        student['Name']=input('Student Name= ').title()
        student['F/Name']=input('Student F.name= ').title()
        student['Class']=input('Student Class= ').title()
        print(student)
        students.append(student)
        print(students)
    elif choice==2:
        indx=int(input('Index Number= '))
        del students[indx]
        print(students)
    elif choice==3:
        print(len(students))
    elif choice==4:
        indx_change=int(input('The dictionary needs changing= '))
        profile_key=input('The key you needs changing= ').title()
        calling_profile=students[indx_change]
        insert_changing=calling_profile[profile_key]
        print(insert_changing)
        new_value=input('write your changing= ')
        insert_changing=new_value
        print(insert_changing)
        #for i in student:
         #   if profile_key==i:
    elif choice==5:
        break                  




















