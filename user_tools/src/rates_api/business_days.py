""" business days module """

from datetime import date
import holidays

from rates_api.date_utils import get_list_of_days


def business_days(start_date: date, end_date: date) -> list[date]:
    """ business days """

    us_holidays = holidays.UnitedStates()

    days: list[date] = []

    for the_date in get_list_of_days(start_date, end_date):
        if (the_date.weekday() < 5) and (the_date not in us_holidays):
            days.append(the_date)

    return days


if __name__ == "__main__":

    the_start_date = date(2020, 12, 15)
    the_end_date = date(2021, 1, 14)

    for business_day in business_days(the_start_date, the_end_date):
        print(business_day)
