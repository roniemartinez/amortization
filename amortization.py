#!/usr/bin/env python
# __author__ = "Ronie Martinez"
# __copyright__ = "Copyright 2019, Ronie Martinez"
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


def main():  # pragma: no cover
    import argparse
    from tabulate import tabulate

    parser = argparse.ArgumentParser(
        description='Python library for calculating amortizations and generating amortization schedules')
    # required parameters
    required = parser.add_argument_group('required arguments')
    required.add_argument('-P', '--principal', dest='principal', type=float, required=True, help='Principal amount')
    required.add_argument('-n', '--period', dest='period', type=int, required=True, help='Total number of periods')
    required.add_argument('-r', '--interest-rate', dest='interest_rate', type=float, required=True,
                          help='Interest rate per period')
    # optional parameters
    parser.add_argument('-s', '--schedule', dest='schedule', default=False, action='store_true',
                        help='Generate amortization schedule')
    arguments = parser.parse_args()
    if arguments.schedule:
        table = (x for x in amortization_schedule(arguments.principal, arguments.interest_rate, arguments.period))
        print(
            tabulate(
                table,
                headers=["Number", "Amount", "Interest", "Principal", "Balance"],
                floatfmt=",.2f",
                numalign="right"
            )
        )
    else:
        amount = calculate_amortization_amount(arguments.principal, arguments.interest_rate, arguments.period)
        print("Amortization amount: {:,.2f}".format(amount))


if __name__ == '__main__':   # pragma: no cover
    main()
