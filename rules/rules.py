import requests
import json

import self as self

from main import bearer_oauth


class Rules:
    def __init__(self):
        self.authorization = ''

    def get_rules(self):
        response = requests.get(
            "https://api.twitter.com/2/tweets/search/stream/rules", auth=bearer_oauth
        )
        if response.status_code != 200:
            raise Exception(
                "Cannot get rules (HTTP {}): {}".format(response.status_code, response.text)
            )
        print(json.dumps(response.json()))
        return response.json()

    def set_rules(self):

        sample_rules = [
            {"value": "#kohli"},
            {"value": "#COYS"},
            # {"value": "cat has:images -grumpy", "tag": "cat pictures"},
        ]
        payload = {"add": sample_rules}
        response = requests.post(
            "https://api.twitter.com/2/tweets/search/stream/rules",
            auth=bearer_oauth,
            json=payload,
        )
        if response.status_code != 201:
            raise Exception(
                "Cannot add rules (HTTP {}): {}".format(response.status_code, response.text)
            )
        print(json.dumps(response.json()))

    # def delete_all_rules(self):
    #     if rules is None or "data" not in rules:
    #         return None
    #
    #     ids = list(map(lambda rule: rule["id"], rules["data"]))
    #     payload = {"delete": {"ids": ids}}
    #     response = requests.post(
    #         "https://api.twitter.com/2/tweets/search/stream/rules",
    #         auth=bearer_oauth,
    #         json=payload
    #     )
    #     if response.status_code != 200:
    #         raise Exception(
    #             "Cannot delete rules (HTTP {}): {}".format(
    #                 response.status_code, response.text
    #             )
    #         )
    #     print(json.dumps(response.json()))


if __name__ == "__main__":
    Rules.get_rules(self)
    Rules.set_rules(self)
    Rules.get_rules(self)
