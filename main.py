#!/usr/bin/python
import requests
import uuid
import json
import string
import time

def clean_shitty_string(text):
    result = ''.join([i if ord(i) < 128 else ' ' for i in text])
    return result.strip()

def clean(s):
    return ''.join(i for i in s if i.isdigit())

def get_cars():
    identifier = uuid.uuid4()

    for page in range(1,10):
        params = {
            'CatID': 1,
            'Auto': 0.0,
            'SubModelID': 247.0,
            'SubCatID': 1,
            'ModelID': 28.0,
            'ToPrice': 35000,
            'FromYear': 2009.0,
            'AppType': 'Android',
            'AppVersion': 2.9,
            'DeviceType': 'Nexus 5',
            'udid': identifier,
            'OSVersion': 5.1,
            'Page': page
        }

        headers = {
            'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)'
        }

        r = requests.get('http://m.yad2.co.il/API/MadorResults.php', params=params, headers=headers)

        data = r.json()

        private_cars = data['Private']['Results']
        for item in private_cars:

            car_id = clean_shitty_string(item.get('RecordID', ''))

            if not car_id:
                continue

            price = clean_shitty_string(item['Line3'])
            price = clean(price)
            raw = item['Line2']

            
            raw=raw.encode('ascii', 'ignore')
            raw = clean_shitty_string(raw)
            raw = ''.join(raw.split())
            raw = raw.split(',:')
            hand = clean(raw[0])
            year = clean(raw[1])
            
            car_link = 'http://www.yad2.co.il/Cars/Car_info.php?CarID={car_id}'.format(car_id=car_id)

            yield car_id, price, hand, year, car_link



def main():

    data = dict()

    for car_id, price, hand, year, car_link in get_cars():
        print car_id, price, hand, year, car_link
        time.sleep(0.3)

if __name__ == "__main__":
    main()
