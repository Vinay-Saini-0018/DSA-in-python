# hasing operations using dictionaries

student = {
    'name' : 'vinay',
    'age' : 34,
    'gender' : 'male'
}

# print(student)

# insertion ---------->
student['nationality'] = 'indian'
#print(student)

# update --------->
student.update({'age' : 24})
# M-2  :  student['age'] = 24
# print(student)

student.setdefault('religion','Na')
#print(student)

print(student['name'])

# deletion ---------->
# del student['religion']
student.pop('name')
# print(student)

print('name' in student)

# iteration ------------>
'''for x in student:
    print(f'{x}') '''

'''for x in student.items():
    print(x)'''

for k,v in student.items():
    print(f"{k}:{v}")
