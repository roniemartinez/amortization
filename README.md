<table>
    <tr>
        <td>License</td>
        <td><img src='https://img.shields.io/pypi/l/amortization.svg?style=for-the-badge' alt="License"></td>
        <td>Version</td>
        <td><img src='https://img.shields.io/pypi/v/amortization.svg?logo=pypi&style=for-the-badge' alt="Version"></td>
    </tr>
    <tr>
        <td>Github Actions</td>
        <td><img src='https://img.shields.io/github/workflow/status/roniemartinez/amortization/Python?label=actions&logo=github%20actions&style=for-the-badge' alt="Github Actions"></td>
        <td>Coverage</td>
        <td><img src='https://img.shields.io/codecov/c/github/roniemartinez/amortization/branch?label=codecov&logo=codecov&style=for-the-badge' alt="CodeCov"></td>
    </tr>
    <tr>
        <td>Supported versions</td>
        <td><img src='https://img.shields.io/pypi/pyversions/amortization.svg?logo=python&style=for-the-badge' alt="Python Versions"></td>
        <td>Wheel</td>
        <td><img src='https://img.shields.io/pypi/wheel/amortization.svg?style=for-the-badge' alt="Wheel"></td>
    </tr>
    <tr>
        <td>Status</td>
        <td><img src='https://img.shields.io/pypi/status/amortization.svg?style=for-the-badge' alt="Status"></td>
        <td>Downloads</td>
        <td><img src='https://img.shields.io/pypi/dm/amortization.svg?style=for-the-badge' alt="Downloads"></td>
    </tr>
</table>

# amortization

Python library for calculating amortizations and generating amortization schedules

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

#### Amortization Period

```python
from amortization.period import calculate_amortization_period

period = calculate_amortization_period(150000, 0.1, 4840.08)
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
usage: amortize [-h] -P PRINCIPAL -r INTEREST_RATE [-s] (-n PERIOD | -a AMOUNT)

Python library for calculating amortizations and generating amortization schedules

options:
  -h, --help            show this help message and exit
  -s, --schedule        Generate amortization schedule
  -n PERIOD, --period PERIOD
                        Total number of periods
  -a AMOUNT, --amount AMOUNT
                        Amortization amount per period

required arguments:
  -P PRINCIPAL, --principal PRINCIPAL
                        Principal amount
  -r INTEREST_RATE, --interest-rate INTEREST_RATE
                        Interest rate per period
```

```bash
amortize -P 150000 -n 36 -r 0.1         # period
amortize -P 150000 -n 36 -r 0.1 -s      # schedule
amortize -P 150000 -a 4840.08 -r 0.1    # amount
```

```bash
% amortize -P 150000 -n 36 -r 0.1 -s           
Number        Amount    Interest    Principal     Balance
--------  ----------  ----------  -----------  ----------
1           4,840.08    1,250.00     3,590.08  146,409.92
2           4,840.08    1,220.08     3,620.00  142,789.92
3           4,840.08    1,189.92     3,650.16  139,139.76
4           4,840.08    1,159.50     3,680.58  135,459.18
5           4,840.08    1,128.83     3,711.25  131,747.93
6           4,840.08    1,097.90     3,742.18  128,005.75
7           4,840.08    1,066.71     3,773.37  124,232.38
8           4,840.08    1,035.27     3,804.81  120,427.57
9           4,840.08    1,003.56     3,836.52  116,591.05
10          4,840.08      971.59     3,868.49  112,722.56
11          4,840.08      939.35     3,900.73  108,821.83
12          4,840.08      906.85     3,933.23  104,888.60
13          4,840.08      874.07     3,966.01  100,922.59
14          4,840.08      841.02     3,999.06   96,923.53
15          4,840.08      807.70     4,032.38   92,891.15
16          4,840.08      774.09     4,065.99   88,825.16
17          4,840.08      740.21     4,099.87   84,725.29
18          4,840.08      706.04     4,134.04   80,591.25
19          4,840.08      671.59     4,168.49   76,422.76
20          4,840.08      636.86     4,203.22   72,219.54
21          4,840.08      601.83     4,238.25   67,981.29
22          4,840.08      566.51     4,273.57   63,707.72
23          4,840.08      530.90     4,309.18   59,398.54
24          4,840.08      494.99     4,345.09   55,053.45
25          4,840.08      458.78     4,381.30   50,672.15
26          4,840.08      422.27     4,417.81   46,254.34
27          4,840.08      385.45     4,454.63   41,799.71
28          4,840.08      348.33     4,491.75   37,307.96
29          4,840.08      310.90     4,529.18   32,778.78
30          4,840.08      273.16     4,566.92   28,211.86
31          4,840.08      235.10     4,604.98   23,606.88
32          4,840.08      196.72     4,643.36   18,963.52
33          4,840.08      158.03     4,682.05   14,281.47
34          4,840.08      119.01     4,721.07    9,560.40
35          4,840.08       79.67     4,760.41    4,799.99
36          4,839.99       40.00     4,799.99        0.00
Totals    174,242.79   24,242.79   150,000.00
```

## Dependencies

[tabulate](https://bitbucket.org/astanin/python-tabulate)

## Author

[Ronie Martinez](mailto:ronmarti18@gmail.com)

## References

- [Amortization Calculation Formula](https://www.vertex42.com/ExcelArticles/amortization-calculation.html)
- [Amortization Period Formula](https://math.stackexchange.com/a/3185904)
