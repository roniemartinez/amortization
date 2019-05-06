#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
# __credits__ = ["Ronie Martinez"]
# __maintainer__ = "Ronie Martinez"
# __email__ = "ronmarti18@gmail.com"
from amortization import calculate_amortization_amount
from amortization.schedule import amortization_schedule


def test_amortization_amount():
    principal = 150000
    period = 36
    interest_rate = 0.1
    amortization = principal * (interest_rate * (1 + interest_rate) ** period)/((1 + interest_rate) ** period - 1)
    assert calculate_amortization_amount(principal, interest_rate, period) == amortization


def test_amortization_schedule():
    principal = 150000
    period = 36
    interest_rate = 0.1

    amortization_amount = calculate_amortization_amount(principal, interest_rate, period)

    number = 1
    balance = principal

    for n, a, i, p, b in amortization_schedule(principal, interest_rate, period):
        interest = balance * interest_rate
        principal = amortization_amount - interest
        balance -= principal

        assert number == n
        assert amortization_amount == a
        assert interest == i
        assert principal == p
        assert balance == b

        number += 1
