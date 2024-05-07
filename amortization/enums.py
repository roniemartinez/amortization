from enum import Enum


class PaymentFrequency(Enum):
    DAILY = 365
    BIWEEKLY = 104
    WEEKLY = 52
    FORTNIGHTLY = 26
    SEMIMONTHLY = 24
    MONTHLY = 12
    QUARTERLY = 4
    SEMIYEARLY = 2
    YEARLY = 1
