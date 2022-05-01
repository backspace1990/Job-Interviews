#Пример входных данных:

names = ["Vasya","Alice","Petya","Jenny","Fedya","Viola","Mark","Chris","Margo","Amir","Umit","Aleksandr"]
birthday_years = [1962,1995,2000,None,None,None,None,1998,2001,1995,1996, None]
genders = ["Male","Female","Male","Female","Male",None,None,None,None,"Male","Male","Male"]

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