students = [{'firstName': 'Nikki', 'lastName': 'Roysden'},
            {'firstName': 'Mervin', 'lastName': 'Friedland'},
            {'firstName': 'Aron', 'lastName': 'Wilkins'}]

print("List of students:")
for student in students:
    full_name = student['firstName'] + ' ' + student['lastName']
    print("- " + full_name)
