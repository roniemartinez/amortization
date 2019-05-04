# amortization

Python library for calculating amortizations and generating amortization schedules

## Demo

[Amortization Calculator](https://apps.easyaspy.org/amortization-calculator)

## Install

```bash
pip install amortization
```

## Usage

### Python

#### Amortization Amount

```python
from amortization import calculate_amortization_amount

amount = calculate_amortization_amount(150_000, 0.1, 36)
```

### Amortization Schedule

```python
from amortization import amortization_schedule

for number, amount, interest, principal, balance in amortization_schedule(150_000, 0.1, 36):
    print(number, amount, interest, principal, balance)
```

### Amortization Schedule (using tabulate)

```python
from amortization import amortization_schedule
from tabulate import tabulate

table = (x for x in amortization_schedule(150_000, 0.1, 36))
print(
    tabulate(
        table,
        headers=["Number", "Amount", "Interest", "Principal", "Balance"],
        floatfmt=",.2f",
        numalign="right"
    )
)
```

### Command line

```bash
amortization -h
usage: amortization [-h] -P PRINCIPAL -n PERIOD -r INTEREST_RATE [-s]

Python library for calculating amortizations and generating amortization
schedules

optional arguments:
  -h, --help            show this help message and exit
  -P PRINCIPAL, --principal PRINCIPAL
                        Principal amount
  -n PERIOD, --period PERIOD
                        Total number of periods
  -r INTEREST_RATE, --interest-rate INTEREST_RATE
                        Interest rate per period
  -s, --schedule        Generate amortization schedule
```

```bash
amortization -P 150000 -n 36 -r 0.1 -s
```

## Dependencies

- [tabulate](https://bitbucket.org/astanin/python-tabulate)

## Author

[Ronie Martinez](ronmarti18@gmail.com)

## References

- [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
- [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)