import requests
import uuid


def main():
    identifier = uuid.uuid4()

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
        'OSVersion': 5.1
    }

    headers = {
        'User-Agent': 'Apache-HttpClient/UNAVAILABLE (java 1.4)'
    }

    r = requests.get('http://m.yad2.co.il/API/MadorResults.php', params=params, headers=headers)

    print r.content


if __name__ == "__main__":
    main()
