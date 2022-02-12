
amortization
============

Python library for calculating amortizations and generating amortization schedules


.. raw:: html

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


Support
-------

If you like ``amortization`` or if it is useful to you, show your support by sponsoring my projects.


.. image:: https://img.shields.io/github/sponsors/roniemartinez?label=github%20sponsors&logo=github%20sponsors&style=for-the-badge
   :target: https://github.com/sponsors/roniemartinez
   :alt: Github Sponsors


Installation
------------

.. code-block:: bash

   pip install amortization

Usage
-----

Python
^^^^^^

Amortization Amount
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from amortization.amount import calculate_amortization_amount

   amount = calculate_amortization_amount(150000, 0.1, 36)

Amortization Period
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from amortization.period import calculate_amortization_period

   period = calculate_amortization_period(150000, 0.1, 4840.08)

Amortization Schedule
^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

   from amortization.schedule import amortization_schedule

   for number, amount, interest, principal, balance in amortization_schedule(150000, 0.1, 36):
       print(number, amount, interest, principal, balance)

Amortization Schedule (using tabulate)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code-block:: python

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

Command line
^^^^^^^^^^^^

.. code-block:: bash

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

.. code-block:: bash

   amortize -P 150000 -n 36 -r 0.1         # period
   amortize -P 150000 -n 36 -r 0.1 -s      # schedule
   amortize -P 150000 -a 4840.08 -r 0.1    # amount

Dependencies
------------

`tabulate <https://bitbucket.org/astanin/python-tabulate>`_

Author
------

`Ronie Martinez <mailto:ronmarti18@gmail.com>`_

References
----------


* `Amortization Calculation Formula <https://www.vertex42.com/ExcelArticles/amortization-calculation.html>`_
* `Amortization Period Formula <https://math.stackexchange.com/a/3185904>`_
