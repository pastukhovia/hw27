# Здесь происходит чтение данных из CSV файлов и их сохранение в JSON

import csv
import json


def read_from_csv(filename):
    # Чтение из CSV

    with open(f'./datasets/{filename}', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile)

        data = []
        for row in reader:
            data.append(row)

        return data


def write_ads_to_json(data):
    # Запись в JSON файла ads.csv

    with open(f'./datasets/ads.json', mode='w', encoding='utf-8') as jsonfile:
        data.pop(0)
        jsondata = []
        for row in data:
            if row[6] == 'TRUE':
                row[6] = True
            elif row[6] == 'FALSE':
                row[6] = False

            ad = {
                "model": "ads.ad",
                "pk": row[0],
                "fields": {
                    "name": row[1],
                    "author": row[2],
                    "price": row[3],
                    "desc": row[4],
                    "address": row[5],
                    "is_published": row[6]
                }
            }
            jsondata.append(ad)

        json.dump(jsondata, jsonfile, ensure_ascii=False, indent=4)


def write_categories_to_json(data):
    # Запись в JSON файла categories.csv

    with open(f'./datasets/categories.json', mode='w', encoding='utf-8') as jsonfile:
        data.pop(0)
        jsondata = []
        for row in data:
            category = {
                "model": "ads.category",
                "pk": row[0],
                "fields": {
                    "name": row[1]
                }
            }
            jsondata.append(category)

        json.dump(jsondata, jsonfile, ensure_ascii=False, indent=4)


write_ads_to_json(read_from_csv('ads.csv'))
write_categories_to_json(read_from_csv('categories.csv'))
