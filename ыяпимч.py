import csv

with open('students.csv', encoding = 'utf8') as f:
    reader = csv.reader(f, delimiter = ',')
    answer = list(reader)[1:]

    sum_class = {}
    count_class = {}

    for id,Name,titleProject_id,level,score in answer:
        if 'Хадаров Владимир'in Name:
            print(f'Ты получил: {score}, за проект - {titleProject_id}')

        sum_class[level] = sum_class.get(level, 0) + int(score if score != 'None' else 0)
        count_class[level] = count_class.get(level, 0) + 1

    for el in answer:
        if el[-1] == 'None':
            el[-1] = round(sum_class[el[-2]]/count_class[el[-2]], 3)

with open('student_new1.csv', 'w', encoding = 'utf8', newline = '') as f:
    writer = csv.writer(f, delimiter = ',')
    writer.writerow('id,Name,titleProject_id,class,score')
    writer.writerows(answer)