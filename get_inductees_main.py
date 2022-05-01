def get_inductees(names, birthday_years, genders):
    list1 = []
    list2 = []
    k = 0
    for name in names:
        if genders[k] == 'Male':
            if type(birthday_years[k]) == int:
                if (2021 - birthday_years[k] >= 18) and (2021 - birthday_years[k] <= 30):
                    list1.append(name)
            elif type(birthday_years[k]) == type(None):
                list2.append(name)
        elif genders[k] == None:
            if type(birthday_years[k]) == int:
                if (2021 - birthday_years[k] >= 18) and (2021 - birthday_years[k] <= 30):
                    list2.append(name)
            elif type(birthday_years[k]) == type(None):
                list2.append(name)

        k += 1

    return list1, list2


def main():
    print(get_inductees(names=names, birthday_years=birthday_years, genders=genders))

if __name__ == '__main__':
    main()
