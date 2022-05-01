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