import requests
import json


def main():
    resp = requests.get(
        'http://api.tianapi.com/guonei/?key=78686d0772723d6f6a2c030bf1528273&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


if __name__ == "__main__":
    main()
