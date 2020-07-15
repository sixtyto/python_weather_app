from requests import get
from json import loads


def main(city):
    find = False
    url = 'https://danepubliczne.imgw.pl/api/data/synop'
    response = get(url)
    for data in loads(response.text):
        if data['stacja'] == city:
            print(data)
            find = True
    if not find:
        print("city not found")


if __name__ == '__main__':
    print("Weather app")
    city = input('Type city name to check: ')
    main(city.capitalize())
