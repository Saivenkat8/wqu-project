import requests

def retrieve_local_ip_address():
    """Return IP address of your Computer"""
    response = requests.get('https://api.ipify.org')
    return response.text

def geo_location(ip_address):
    """Return geolocation based on the IP address"""
    response = requests.get(f'https://ipinfo.io/{ip_address}')
    data = response.json()
    coords = [float(coord) for coord in data['loc'].split(',')]
    return coords

def get_weather_location(coords):
    """Return Weather data for given set of coordinates"""
    url = 'https://www.metaweather.com/api/location/search/'
    params = {'lattlong': f'{coords[0]}, {coords[1]}'}
    response = requests.get(url, params=params)
    woeid = response.json()[0]['woeid']
    return woeid

def get_weather_data(woeid):
    url = 'https://www.metaweather.com/api/location/'
    response = requests.get(url + str(woeid))
    return response.json()

def weather_data(ip_address):
    coords = geo_location(ipaddress)
    woeid = get_weather_location(coords)
    weather_data = get_weather_data(woeid)
    temperature = weather_data['consolidated_weather'][0]['the_temp']
    return f"Hello the temperature is {temperature} deg C"

if __name__ == '__main__':
    print(weather_data())