import requests
import json
import csv

ip_list = ['122.35.203.161', '174.217.10.111', '187.121.176.91', '176.114.85.116', '174.59.204.133', '54.209.112.174', '109.185.143.49', '176.114.253.216', '210.171.87.76', '24.169.250.142']
ip_list1 = ['122.35.203.161']
ip_list3 = ['122.35.203.161', '174.217.10.111', '187.121.176.91']
ip_list4 = ['212.59.0.1']

url_ip_simple = "https://api.ipbase.com/v2/info"
url_meteo = "https://api.openweathermap.org/data/2.5/weather"

API_key_country = "sfDusrfwZrHZkV2BIp9txss3651ZzS6EOHkcScKc"
API_key_meteo = "0b6a0903412eca97e08b1a13004acd6d"

HEADER = ['IP', 'Country', 'City', 'Temp', 'Weather']


def yeld_country(ip_query):
    global a_ip
    global b
    global c
    global lat
    global lon

    payload = {'apikey': API_key_country, 'ip': ip_query}
    r = requests.get(url_ip_simple, params=payload)
    api_request_json = json.loads(r.text)
    print(api_request_json)

    newlist = []
    for x in api_request_json.values():
        for y in x.values():
            # print(y)
            newlist.append(y)
    a_ip = newlist[0]                          #IP
    city_info = newlist[5]                  #Country/city info
    print (city_info)
    b = city_info['country']['name']        #Country
    c = city_info['city']['name']           #City
    lat = city_info['latitude']             #Latitude
    lon = city_info['longitude']            #Longitude

    print(a_ip)
    print(b)
    print(c)
    print(lat)
    print(lon)


def yeld_meteo(lat_query, lon_query):
    global d
    global e

    payload = {'lat': lat, 'lon': lon, 'exclude': 'minutely,hourly,daily', 'appid': API_key_meteo, 'units': 'metric'}
# 'q' : c info by City name
    r = requests.get(url_meteo, params=payload)

    dic = json.loads(r.text)
    # print(dic)
    newlist = []
    for x in dic.values():
        # print(x)
        newlist.append(x)
    temp_info = newlist[3]              #Temp
    weather_info = newlist[1][0]        #Weather
    d = temp_info['temp']
    e = weather_info['main']
    print(d)
    print(e)

def main():
    with open('ip_data.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f, delimiter=',')
        writer.writerow(HEADER)


    for ip in ip_list4:
        yeld_country(ip)
        yeld_meteo(lat, lon)
        data = [a_ip, b, c, d, e]
        with open('ip_data.csv', 'a',  encoding='UTF8') as f:
            writer = csv.writer(f, delimiter=',')
            writer.writerow(data)


main()