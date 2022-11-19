import requests as rq

parameters = {
    "amount":10,
    "type": "boolean",
}

response = rq.get(url="https://opentdb.com/api.php?amount=10",params=parameters)
response.raise_for_status()
data = response.json()
question_data = []
for i in data['results']:
    question_data.append(i) 