#Пример входных данных:

students_avg_scores = {'Max': 4.964, 'Eric': 4.962, 'Peter': 4.923, 'Mark': 4.957, 'Julie': 4.95, 'Jimmy': 4.973, 'Felix': 4.937, 'Vasya': 4.911, 'Don': 4.936, 'Zoi': 4.937}

import operator

def make_report_about_top3(students_avg_scores):
    sorted_students = sorted(students_avg_scores.items(), key=operator.itemgetter(1), reverse=True)
    list_top3 = []
    k = 0
    for top3 in sorted_students:
        if k == 3:
            break
        list_top3.append(top3[0])
        k += 1

    return list_top3


def main():
    print(make_report_about_top3(students_avg_scores=students_avg_scores))

if __name__ == '__main__':
    main()