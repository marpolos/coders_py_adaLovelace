import requests as req
import datetime as dt
import csv
from PIL import Image
from IPython.display import display

url = 'https://api.covid19api.com/dayone/country/brazil'
res = req.get(url)

# print(res.status_code)
raw_data = res.json()

# print(raw_data[0])
final_data = list()
for obs in raw_data:
    final_data.append([
        obs["Confirmed"],
        obs["Deaths"],
        obs["Recovered"],
        obs["Active"],
        obs["Date"]
        ])

# print(final_data)
final_data.insert(0, ["Confirmed", "Deaths", "Recovered", "Active", "Date"])
print(final_data)

CONFIRMED = 0
DEATHS = 1
RECOVERED = 2
ACTIVE = 3
DATA = 4

for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
    # DATA representa a posição em que está esse dado
    # [:10] faz um slice de 0 a 10

# print(final_data)

# datetime tem 3 tipos de criação de data: time, date e datetime
# datetime.time(hora, minuto, segundo, microssegundo)
# datetime.data(ano, mes, dia)
# datetime.datetime(ano, mes, dia, hora, minuto, segundo, microssegundo)

with open("brasil_covid.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerows(final_data)

# transformar data de string para datetime
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

print(final_data)


def get_dataset(y, labels):
    if type(y[0] == list):
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
            })
        return datasets
    else:
        return [{
            'label': labels[0],
            'data': y
        }]


def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }


def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_dataset(y, labels)
    options = set_title(title)

    chart = {
        'type': kind,
        'data': {
            'labels': x,
            'datasets': datasets,
        },
        'options': options
    }

    return chart


def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = req.get(f"{url_base}?c={str(chart)}")
    return resp.content


def save_image(path, content):
    with open(path, 'wb') as image:
        image.write(content)


def display_image(path):
    img_pil = Image(path)
    display(img_pil)

y_data_1 = list()
for obs in final_data[1::10]:

