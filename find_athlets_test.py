#Пример входных данных:

know_english = ["Vasya","Jimmy","Max","Peter","Eric","Zoi","Felix"]
sportsmen = ["Don","Peter","Eric","Jimmy","Mark"]
more_than_20_years = ["Peter","Julie","Jimmy","Mark","Max"]

def find_athlets(know_english, sportsmen, more_than_20_years):
    spisok = []
    for ingman in know_english:
        if (ingman in sportsmen) and (ingman in more_than_20_years):
            spisok.append(ingman)
    
    return spisok


def main():
    print(find_athlets(know_english=know_english, sportsmen=sportsmen, more_than_20_years=more_than_20_years))

if __name__ == '__main__':
    main()