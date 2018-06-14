import requests


class Whether(object):
    def __init__(self):
        self.api = "c795fb88219ffa6cbb0b345d4bd4461f"
        self.url = "http://api.openweathermap.org/data/2.5/weather"

        # weather - weather for one day by city_id
        # forecast - weather for 5 days
        # find?q=City - weather for one day by city_name

        self.city = 'Kharkiv'
        self.city_id = '706483'

    def get_response(self):
        return requests.get(self.url,
                            params={'id': self.city_id, 'units': 'metric', 'lang': 'ru', 'APPID': self.api})

    def get_data(self):
        data = self.get_response().json()
        self.temp = data['main']['temp']
        self.temp_min = data['main']['temp_min']
        self.temp_max = data['main']['temp_max']
        self.description = data['weather'][0]['main']
        self.wind = data['wind']['speed']
        self.clouds = data['clouds']['all']

    def get_string(self):
        return str('Current temperature is {}, clouds {} %, wind {} meters per second, sky is {}'
                   .format(self.temp, self.clouds, self.wind, self.description))


if __name__ == '__main__':
    w = Whether()
    w.get_data()
    print(w.get_string())