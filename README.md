# get_weather_forecast

Данная программа делает запрос на сайт `wttr.un` и возвращает прогноз погоды в нужном формате и по заданным городам.

![get_weather_forecast](https://github.com/user-attachments/assets/7d179b1e-a207-42cb-95e1-13630fa22ac1)

Для запуска скрипта полностью скопируйте код:
```python
import requests
from urllib.parse import urljoin


def get_weather_forecast(location):
    payload = {
            'M': '',
           'nTq': '',
           'lang': 'ru'
    }
    url = urljoin('https://wttr.in/', f'{location}')
    response = requests.get(url, params=payload)
    response.raise_for_status()
    print(response.text)

if __name__ == '__main__':
    locations = ['SVO', 'London', 'Череповец']
    for location in locations:
        get_weather_forecast(location)
```
Вставьте код в своей среде разработки (дополнительно понадобится библиотека requests).
Далее запускаете скрипт и вся информация появляется у вас на экране.
Можно добавить интересующие вас города в список `locations` и посмотреть на результат.
