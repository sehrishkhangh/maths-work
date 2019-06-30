print('\n')
name=input('Name of Student :')
#print('name :'+'name of student')
name_of_institute=input('Name of Institute:')
#print('name')
standard=input('Level:')
print('\n')
physics=int(input('Marks of PHYSICS='))
math=int(input('Marks of MATHS='))
chem=int(input('Marks of CHEMISTRY='))
english=int(input('Marks of ENGLISH='))
sindhi=int(input('Marks of SINDHI='))
total_marks=500
obtained_marks=physics+ math+chem+english+sindhi
percentage=(obtained_marks*100/total_marks)
print('\n')
print('------------------MARK SHEET-------------------------------')
print('\n')
print('SUBJECTS                    OBTAINED MARKS    MAXIMUM MARKS')
print('Physics            :          '+str(physics)+'                 '+str(100))
print('Maths              :          '+str(math)+'                 '+str(100))
print('Chemistry          :          '+str(chem)+'                 '+str(100))
print('English            :          '+str(english)+'                 '+str(100))
print('Sindhi             :          '+str(sindhi)+'                 '+str(100))
print('------------------------------------------------------------')
print('\n')
print('Total              :          '+str(obtained_marks)+'                '+str(500))
print('Percentage= '+str(percentage)+'%')
if obtained_marks>350:
   print('Grade=A+')
elif 350<obtained_marks>250:
   print('Grade=A')
elif 250<obtained_marks>150:

   print('Grade=B')
else:
   print('FAILS')



