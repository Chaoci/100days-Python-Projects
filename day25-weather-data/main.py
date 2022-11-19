import pandas as pd
import csv

# with open("./day25-weather-data/weather_data.csv", "r") as file:
#     res = file.readlines()
#     print(res)

# with open("./day25-weather-data/weather_data.csv") as data:
#     data_file = csv.reader(data)
#     header = next(data_file)
#     temperture = []
#     # print(header)
#     for row in data_file:
#         temperture.append(row[1])
#     # temperture.remove("temp")
#     print(temperture)

data = pd.read_csv("./day25-weather-data/weather_data.csv")
data_list = data.temp.to_list()
average = data.temp.mean()

maximum = data.temp.max()

data_condition = data.condition
data_monday = data[data.day == 'Monday']

max_tempday = data[data.temp == maximum]

c = int(data_monday.temp)
res = c * 9/5 +32
data_monday.temp = res
print(data_monday)