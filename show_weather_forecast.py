import requests
from urllib.parse import urljoin


def show_weather_forecast(location):
    payload = {
            'M': '',
            'n': '',
            'T': '',
            'q': '',
            'lang': 'ru'
    }
    url = urljoin('https://wttr.in/', f'{location}')
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)

if __name__ == '__main__':
    locations = ['SVO', 'London', 'Череповец']
    for location in locations:
        show_weather_forecast(location)
