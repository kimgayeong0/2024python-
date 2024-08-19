import requests
city_name='울산'
API_key='16b95a2dc4be2fbc091173adae42bbb6'
limit=5
url=f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit={limit}&appid={API_key}'
res=requests.get(url)
data=res.json()
# data=res.content.decode('utf-8')
print(len(data))
lat=data[0]['lat']
lon=data[0]['lon']
print(lat,lon)
url=f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}'
res=requests.get(url)
weather=res.json()
print(weather['weather'][0]['description'])
print("20602김가영")
