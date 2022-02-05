department = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
exam_notes = {'Biotech': (2, 3), 'Chemistry': (3, 3), 'Engineering': (4, 5), 'Mathematics': (4, 4), 'Physics': (2, 4)}

N = int(input())
with open('applicant_list.txt') as file:
    students = [line.split() for line in file.readlines()]

for item in range(7, 10):

    for key in department.keys():
        for applicant in sorted(students, key=lambda x: (
                -max(int(x[exam_notes[key][0]]) + int(x[exam_notes[key][1]]), int(x[6]) * 2), x[0], x[1])):

            if applicant[item] == key and len(department[key]) < N:
                max_score = max(((int(applicant[exam_notes[key][0]]) + int(applicant[exam_notes[key][1]])) / 2),
                                float(applicant[6]))
                department[key].append([applicant[0], applicant[1], max_score])
                students.remove(applicant)

for key in department.keys():

    with open(f'{key.lower()}.txt', 'w', encoding='utf-8') as file:
        for student in sorted(department[key], key=lambda x: (-x[2], x[0], x[1])):
            print(*student, file=file)
