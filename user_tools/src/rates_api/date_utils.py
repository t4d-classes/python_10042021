""" date utils module """

from datetime import date, timedelta


def get_list_of_days(start_date: date, end_date: date) -> list[date]:
    """ get list of days """

    days: list[date] = []

    the_date = start_date

    while the_date <= end_date:
        days.append(the_date)
        the_date = the_date + timedelta(days=1)

    return days
    