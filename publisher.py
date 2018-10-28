from google.cloud import pubsub_v1
import os, json
import base64
import time
import random
from datetime import datetime


def random_number(base):
    return (base + round(random.random(),2))

def create_pd():
    iot_pd = {
        "pressure": random_number(24),
        "temperature": random_number(64),
        "dewpoint": random_number(39),
        "timecollected": datetime.utcnow().strftime("%Y %m %d %H:%M:%S"),
        "latitude": random_number(37),
        "sensorID": "lucky-sensor-1",
        "zipcode": "94043",
        "longitude": -122.0856,
        "humidity": random_number(20) 
    }
    return iot_pd

def test():

    print create_pd()

def main():

    # Instantiates a client
    publisher = pubsub_v1.PublisherClient()

    topic_path = publisher.topic_path("first-try-209611", "iot-ingest")

    for x in range(1, 3):
        pd = json.dumps(create_pd())
        publisher.publish(topic_path, data=pd)
        print("message published")
        print(pd)
        print("sleeping 2 second")
        time.sleep(2)

if __name__ == "__main__":
        main()
