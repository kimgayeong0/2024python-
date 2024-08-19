import requests
servicekey='0x8x2O1IksymMFdz/hXLsva1bp814aDOnLNiTY3IMC1M4ukRMXNdx4RbRVyOjd6wkOqmNkbIZg92QPqhCq+wdA=='
url = 'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty'
params ={'serviceKey' : servicekey, 'returnType' : 'json', 'numOfRows' : '100', 'pageNo' : '1', 'sidoName' : '울산', 'ver' : '1.0' }

response = requests.get(url, params=params)
data=response.json()
print(type(data))
print(data['response']['body']['items'][1]['pm10Value'])