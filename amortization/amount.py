#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019-2020, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"


def calculate_amortization_amount(principal, interest_rate, period):
    """
    Calculates Amortization Amount per period

    :param principal: Principal amount
    :param interest_rate: Interest rate per period
    :param period: Total number of periods
    :return: Amortization amount per period
    """
    x = (1 + interest_rate) ** period
    return principal * (interest_rate * x) / (x - 1)
