from typing import Iterator, Tuple

from amortization.amount import calculate_amortization_amount
from amortization.enums import PaymentFrequency


def amortization_schedule(
    principal: float, interest_rate: float, period: int, extra_payment: float = 0.0, payment_frequency: PaymentFrequency = PaymentFrequency.MONTHLY
) -> Iterator[Tuple[int, float, float, float, float]]:
    """
    Generates amortization schedule

    :param principal: Principal amount
    :param interest_rate: Interest rate per year
    :param period: Total number of periods
    :param extra_payment: Extra principal paid each period
    :param payment_frequency: Payment frequency per year
    :return: Rows containing period, amount, interest, principal, balance, etc
    """
    amortization_amount = calculate_amortization_amount(principal, interest_rate, period, extra_payment, payment_frequency)
    adjusted_interest = interest_rate / payment_frequency.value
    balance = principal
    number = 0
    while balance:
        number += 1

        interest = round(balance * adjusted_interest, 2)
        payment = amortization_amount

        if payment < balance:
            principal = payment - interest
            balance -= principal
        else:
            principal, payment, balance = balance, balance + interest, 0

        yield number, payment, interest, principal, balance
