from typing import Any, List  # pragma: no cover

from amortization.amount import calculate_amortization_amount  # pragma: no cover
from amortization.period import calculate_amortization_period
from amortization.schedule import amortization_schedule  # pragma: no cover


def main() -> None:  # pragma: no cover
    import argparse

    from tabulate import tabulate

    parser = argparse.ArgumentParser(
        description="Python library for calculating amortizations and generating amortization schedules"
    )
    # required parameters
    required = parser.add_argument_group("required arguments")
    required.add_argument(
        "-P",
        "--principal",
        dest="principal",
        type=float,
        required=True,
        help="Principal amount",
    )
    required.add_argument(
        "-r",
        "--interest-rate",
        dest="interest_rate",
        type=float,
        required=True,
        help="Interest rate per period",
    )
    # optional parameters
    parser.add_argument(
        "-s",
        "--schedule",
        dest="schedule",
        default=False,
        action="store_true",
        help="Generate amortization schedule",
    )
    mutually_exclusive = parser.add_mutually_exclusive_group(required=True)
    mutually_exclusive.add_argument(
        "-n",
        "--period",
        dest="period",
        type=int,
        help="Total number of periods",
    )
    mutually_exclusive.add_argument(
        "-a",
        "--amount",
        dest="amount",
        type=float,
        help="Amortization amount per period",
    )
    arguments = parser.parse_args()
    if arguments.schedule:
        if arguments.period is None:
            parser.error("-s/--schedule requires -n/--period")
        total_paid = total_interest = total_principal = 0.0
        table: List[Any] = []
        for row in amortization_schedule(arguments.principal, arguments.interest_rate, arguments.period):
            table.append(row)
            total_paid += row[1]
            total_interest += row[2]
            total_principal += row[3]
        table.append(("Totals", total_paid, total_interest, total_principal))
        print(
            tabulate(
                table,
                headers=["Number", "Amount", "Interest", "Principal", "Balance"],
                floatfmt=",.2f",
                numalign="right",
            )
        )
    elif arguments.amount:
        period = calculate_amortization_period(arguments.principal, arguments.interest_rate, arguments.amount)
        print("Amortization period: {}".format(period))
    else:
        amount = calculate_amortization_amount(arguments.principal, arguments.interest_rate, arguments.period)
        print("Amortization amount: {:,.2f}".format(amount))
