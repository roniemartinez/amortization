#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from amortization.amount import calculate_amortization_amount


def amortization_schedule(principal, interest_rate, period):
    """
    Generates amortization schedule

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of periods
    :return: Rows containing period, interest, principal, balance, etc
    """
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)
    number = 1
    balance = principal
    while number <= period:
        interest = balance * interest_rate
        principal = amortization_amount - interest
        balance -= principal
        yield number, amortization_amount, interest, principal, balance if balance > 0 else 0
        number += 1
