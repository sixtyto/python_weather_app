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
    city_list = []
    for data in loads(response.text):
        city_list.append(data['stacja'])
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
        print(f'city not found, please try: {", ".join(city_list)}.')


if __name__ == '__main__':
    print("Weather app")
    city = input('Type city name to check: ')
    main(city.capitalize())
