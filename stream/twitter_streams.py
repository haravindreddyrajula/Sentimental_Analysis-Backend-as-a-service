import json

import requests

from KafkaService.kafka_client import publish_message
from main import bearer_oauth


def get_stream(kafka_producer):
    response = requests.get(
        "https://api.twitter.com/2/tweets/search/stream", auth=bearer_oauth, stream=True,
    )
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(
            "Cannot get stream (HTTP {}): {}".format(
                response.status_code, response.text
            )
        )
    for response_line in response.iter_lines():
        if response_line:
            json_response = json.loads(response_line)
            publish_message(kafka_producer, 'twitter', 'raw', json_response)
            print(json.dumps(json_response, indent=4, sort_keys=True))

# if __name__ == "__main__":
#     kafka_producer = connect_kafka_producer()
#     get_stream(kafka_producer)
