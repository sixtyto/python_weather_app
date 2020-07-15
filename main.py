from requests import get
from json import loads
from terminaltables import AsciiTable


def main(city):
    find = False
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    rows = [
        ['City', 'Time', 'Temperature']
    ]
    for data in loads(response.text):
        if data['stacja'] == city:
            rows.append([
                data['stacja'],
                data['godzina_pomiaru'],
                data['temperatura']
            ])
            find = True
    if find:
        table = AsciiTable(rows)
        print(table.table)
    else:
        print("city not found")


if __name__ == '__main__':
    print("Weather app")
    city = input('Type city name to check: ')
    main(city.capitalize())
