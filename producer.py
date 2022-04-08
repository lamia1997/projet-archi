from time import sleep
import json
from json import dumps
from kafka import KafkaProducer
import requests
import random

with open('DBPedia.json') as json_data:
    data = json.load(json_data) 
random.shuffle(data)
producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

for db in data:
        producer.send('Cards', json.dumps(db).encode('utf-8'))
        print('envoyé')
        print(db)
        producer.flush()
        sleep(2)
