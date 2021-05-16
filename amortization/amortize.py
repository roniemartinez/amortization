from amortization.amount import calculate_amortization_amount  # pragma: no cover
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
        "-n",
        "--period",
        dest="period",
        type=int,
        required=True,
        help="Total number of periods",
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
    arguments = parser.parse_args()
    if arguments.schedule:
        table = (x for x in amortization_schedule(arguments.principal, arguments.interest_rate, arguments.period))
        print(
            tabulate(
                table,
                headers=["Number", "Amount", "Interest", "Principal", "Balance"],
                floatfmt=",.2f",
                numalign="right",
            )
        )
    else:
        amount = calculate_amortization_amount(arguments.principal, arguments.interest_rate, arguments.period)
        print("Amortization amount: {:,.2f}".format(amount))
