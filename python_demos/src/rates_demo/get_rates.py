""" get rates module """

from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta
import threading

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

def get_rate_task(business_day: date, responses: list[str]) -> None:
    """ get rate task """

    rate_url = "".join([
        "http://127.0.0.1:5000/api/",
        str(business_day),
        "?base=USD&symbols=EUR"
    ])

    response = requests.get(rate_url)
    responses.append(response.text)


def get_rates_threaded() -> None:
    """ get rates """
    print("get rates")

    start_date = date(2021, 1, 1)
    end_date = start_date + timedelta(days=20)

    rate_responses: list[str] = []
    threads: list[threading.Thread] = []

    for business_day in business_days_gen(start_date, end_date):
        a_thread = threading.Thread(
            target=get_rate_task, args=(business_day, rate_responses))
        a_thread.start()
        threads.append(a_thread)

    for a_thread in threads:
        a_thread.join()

    print("\n".join(rate_responses))


# def get_rate_task(business_day: date) -> str:
#     """ get rate task """

#     rate_url = "".join([
#         "http://127.0.0.1:5000/api/",
#         str(business_day),
#         "?base=USD&symbols=EUR"
#     ])

#     response = requests.get(rate_url)
#     return response.text

# def get_rates_threadpool() -> None:
#     """ get rates """
#     print("get rates")

#     start_date = date(2021, 1, 1)
#     end_date = start_date + timedelta(days=20)

#     rate_responses: list[str] = []

#     with ThreadPoolExecutor() as executor:

#         print("starting executor map")

#         rate_responses = list(executor.map(
#             get_rate_task,
#             [
#                 business_day
#                 for business_day in business_days_gen(start_date, end_date)
#             ]))

#         print("made it here...")
#         print(rate_responses)


#     print("\n".join(rate_responses))
