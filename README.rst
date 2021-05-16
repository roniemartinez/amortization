.. role:: raw-html-m2r(raw)
   :format: html


amortization
============

Python library for calculating amortizations and generating amortization schedules


.. raw:: html

   <table>
       <tr>
           <td>License</td>
           <td><img src='https://img.shields.io/pypi/l/amortization.svg' alt="License"></td>
           <td>Version</td>
           <td><img src='https://img.shields.io/pypi/v/amortization.svg' alt="Version"></td>
       </tr>
       <tr>
           <td>Travis CI</td>
           <td><img src='https://www.travis-ci.com/roniemartinez/amortization.svg?branch=master' alt="Travis CI"></td>
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


Support
-------

If you like ``amortization`` or if it is useful to you, show your support by buying me a coffee.

:raw-html-m2r:`<a href="https://www.buymeacoffee.com/roniemartinez" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>`

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

.. code-block:: bash

   amortize -P 150000 -n 36 -r 0.1 -s

Dependencies
------------

`tabulate <https://bitbucket.org/astanin/python-tabulate>`_

Author
------

`Ronie Martinez <mailto:ronmarti18@gmail.com>`_

References
----------


* `Packaging and distributing projects <https://packaging.python.org/guides/distributing-packages-using-setuptools/>`_
* `Using TestPyPI <https://packaging.python.org/guides/using-testpypi/>`_
