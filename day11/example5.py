import json


def main():
    mydict = {
        "name": "chen",
        "age": 18,
        "qq": 123,
        "friends": [
            "liu",
            "qiu"
        ],
        "cars": [
            {
                "brand": "BYD",
                "max_speed": 180
            },
            {
                "brand": "Auto",
                "max_speed": 190
            },
            {
                "brand": "Audi",
                "max_speed": 170
            }
        ]
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成！')


if __name__ == "__main__":
    main()
