from random import randint
from time import sleep

import requests


class Browser:
    def get(self, url) -> str:
        response = None

        while not response:
            response = requests.get(url)

            if response.status_code != 200:
                response = None

                print(
                    "Error while getting page data",
                    f"status code: {response.status_code}"
                )
                print("Retrying...")
                sleep(randint(1, 3))

        print(f"Got page data from {url}")
        return response.text
