names = {
    'students': [
        {'firstName': 'Nikki', 'lastName': 'Roysden'},
        {'firstName': 'Mervin', 'lastName': 'Friedland'},
        {'firstName': 'Aron', 'lastName': 'Wilkins'}
    ],
    'teachers': [
        {'firstName': 'Amberly', 'lastName': 'Calico'},
        {'firstName': 'Regine', 'lastName': 'Agtarap'}
    ]
}

print("List of students:")
for student in names['students']:
    full_name = student['firstName'] + ' ' + student['lastName']
    print("- " + full_name)

print("\nList of teachers:")
for teacher in names['teachers']:
    full_name = teacher['firstName'] + ' ' + teacher['lastName']
    print("- " + full_name)
