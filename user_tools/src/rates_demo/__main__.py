""" main module """

from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

import requests

from rates_demo.business_days import business_days_gen

def get_rates() -> None:
    """ get rates """
    print("get rates")

    start_date = date(2021, 1, 1)
    end_date = start_date + timedelta(days=20)

    rate_responses: list[str] = []

    for business_day in business_days_gen(start_date, end_date):

        rate_url = "".join([
            "http://127.0.0.1:5000/api/",
            str(business_day),
            "?base=USD&symbols=EUR"
        ])

        response = requests.get(rate_url)
        rate_responses.append(response.text)

    print("\n".join(rate_responses))

def get_rate_task(business_day: date) -> str:
    """ get rate task """

    rate_url = "".join([
        "http://127.0.0.1:5000/api/",
        str(business_day),
        "?base=USD&symbols=EUR"
    ])

    response = requests.get(rate_url)
    return response.text


def get_rates_threaded() -> None:
    """ get rates """
    print("get rates")

    start_date = date(2021, 1, 1)
    end_date = start_date + timedelta(days=20)

    rate_responses: list[str] = []

    with ThreadPoolExecutor() as executor:

        rate_responses = list(executor.map(
            get_rate_task,
            [
                business_day
                for business_day in business_days_gen(start_date, end_date)
            ]))


    print("\n".join(rate_responses))


if __name__ == "__main__":
    # get_rates()

    get_rates_threaded()
