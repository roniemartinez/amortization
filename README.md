# amortization

Python library for calculating amortizations and generating amortization schedules
<table>
    <tr>
        <td>License</td>
        <td><img src='https://img.shields.io/pypi/l/amortization.svg' alt="License"></td>
        <td>Version</td>
        <td><img src='https://img.shields.io/pypi/v/amortization.svg' alt="Version"></td>
    </tr>
    <tr>
        <td>Github Actions</td>
        <td><img src='https://github.com/roniemartinez/amortization/actions/workflows/python.yml/badge.svg' alt="Github Actions"></td>
        <td>Coverage</td>
        <td><img src='https://codecov.io/gh/roniemartinez/amortization/branch/master/graph/badge.svg'></td>
    </tr>
    <tr>
        <td>Supported versions</td>
        <td><img src='https://img.shields.io/pypi/pyversions/amortization.svg' alt="Python Versions"></td>
        <td>Wheel</td>
        <td><img src='https://img.shields.io/pypi/wheel/amortization.svg' alt="Wheel"></td>
    </tr>
    <tr>
        <td>Status</td>
        <td><img src='https://img.shields.io/pypi/status/amortization.svg' alt="Status"></td>
        <td>Downloads</td>
        <td><img src='https://img.shields.io/pypi/dm/amortization.svg' alt="Downloads"></td>
    </tr>
</table>

## Support
If you like `amortization` or if it is useful to you, show your support by buying me a coffee.

<a href="https://www.buymeacoffee.com/roniemartinez" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>

## Installation

```bash
pip install amortization
```

## Usage

### Python

#### Amortization Amount

```python
from amortization.amount import calculate_amortization_amount

amount = calculate_amortization_amount(150000, 0.1, 36)
```

### Amortization Schedule

```python
from amortization.schedule import amortization_schedule

for number, amount, interest, principal, balance in amortization_schedule(150000, 0.1, 36):
    print(number, amount, interest, principal, balance)
```

### Amortization Schedule (using tabulate)

```python
from amortization.schedule import amortization_schedule
from tabulate import tabulate

table = (x for x in amortization_schedule(150000, 0.1, 36))
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
amortize -h
usage: amortize [-h] -P PRINCIPAL -n PERIOD -r INTEREST_RATE [-s]

Python library for calculating amortizations and generating amortization
schedules

optional arguments:
  -h, --help            show this help message and exit
  -s, --schedule        Generate amortization schedule

required arguments:
  -P PRINCIPAL, --principal PRINCIPAL
                        Principal amount
  -n PERIOD, --period PERIOD
                        Total number of periods
  -r INTEREST_RATE, --interest-rate INTEREST_RATE
                        Interest rate per period
```

```bash
amortize -P 150000 -n 36 -r 0.1 -s
```

## Dependencies

[tabulate](https://bitbucket.org/astanin/python-tabulate)

## Author

[Ronie Martinez](mailto:ronmarti18@gmail.com)

## References

- [Packaging and distributing projects](https://packaging.python.org/guides/distributing-packages-using-setuptools/)
- [Using TestPyPI](https://packaging.python.org/guides/using-testpypi/)
