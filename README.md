# show_weather_forecast

Данная программа делает запрос на сайт [wttr.in] и возвращает прогноз погоды в нужном формате и по заданным городам.

[wttr.un]: http://wttr.in

![get_weather_forecast](https://github.com/user-attachments/assets/7d179b1e-a207-42cb-95e1-13630fa22ac1)

Для запуска скрипта полностью скопируйте код:
```python
import requests
from urllib.parse import urljoin


def show_weather_forecast(location):
    payload = {
            'M': '',
            'n': '',
            'T': '',
            'q': '':
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
```
Вставьте код в своей среде разработки (дополнительно понадобится библиотека [requests](https://requests.readthedocs.io/en/latest/user/install/#install)).
Далее запускаете скрипт по кнопке `Run` и вся информация появляется у вас на экране.

![работа функции](https://github.com/user-attachments/assets/0db5ff53-84ab-4405-a101-3cb06425d5ba)

Можно добавить интересующие вас города в список `locations` и посмотреть на результат.

