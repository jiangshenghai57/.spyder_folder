# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 11:34:06 2018

@author: Shenghai
"""
"""
Prepayment model in this script is based on PSA standard model after 30 periods the pool becomes seasoned
"""
'''
CONSTANTS DO NOT CHANGE
'''
TWO = 2
ONE = 1
ZERO = 0
EIGHT = 8
ZERO_F = 0.00
HUNDRED = 100
THIRTY = 30
TWELVE = 12
'''
CONSTANTS DO NOT CHANGE
'''

import pandas as pd
import numpy as np
from datetime import date

wac = 0.0988
years = 7
payments_year = 12
principal = 850005960.82
closing_date = (date(2018, 2, 2))
start_date = (date(2018, 3, 1))
init_int_prd = 30
yr_convent = 360
mo_convent = 30
PSA = 1.00
CPR = 0.1



# Calculating first interest payment, it will vary depends on the initial interst period
first_int = wac * principal * init_int_prd / yr_convent

rng = pd.date_range(start_date, periods=years * payments_year + ONE, freq='MS')
rng.name = 'payment_date'
df = pd.DataFrame(index=rng, columns = ['Balance', 'interest', 'principal',
                                        'PTR Rate', 'Net-PPIS', 'Fresh Cils',
                                        'Cils Paid', 'Cils Outstanding',
                                        'Fresh Cpls', '%Outstanding'], dtype = 'float')

df.reset_index(inplace=True)
df.index += ZERO
df.index.name = 'prd'
cap_period = df.index[-ONE] + ONE
df['payment_date'] = df['payment_date'].shift(ONE)

# Calculating amortization schedule
for i in np.arange(ZERO, cap_period):
    if i == ZERO:
        df.loc[i, 'payment_date'] = closing_date
        df.loc[i, 'Balance'] = principal
        df.loc[i, 'principal'] = ZERO_F
        df.loc[i, 'interest'] = ZERO_F
    elif i == ONE:
        pmt = -round(np.pmt(wac/payments_year, years*payments_year, principal) ,TWO)
        SMM = ONE - (ONE - CPR * PSA * (i / THIRTY)) ** (ONE/TWELVE)
        df.loc[i, 'interest'] = principal * wac / payments_year
        pre_pmt = (principal - (pmt - df.loc[i, 'interest'])) * SMM
        df.loc[i, 'principal'] = pmt - df.loc[i, 'interest'] + pre_pmt
        df.loc[i, 'Balance'] = principal - df.loc[i, 'principal']
    elif i <= THIRTY:
        pmt = -round(np.pmt(wac/payments_year, years*payments_year - i + ONE, df.loc[i - ONE, 'Balance']) ,TWO)
        SMM = ONE - (ONE - CPR * PSA * (i / THIRTY)) ** (ONE/TWELVE)
        df.loc[i, 'interest'] = df.loc[i - ONE, 'Balance'] * wac / payments_year
        pre_pmt = (df.loc[i - ONE, 'Balance'] - (pmt - df.loc[i, 'interest'])) * SMM
        df.loc[i, 'principal'] = min(df.loc[i - ONE, 'Balance'], pmt - df.loc[i, 'interest'] + pre_pmt)
        df.loc[i, 'Balance'] = df.loc[i - ONE, 'Balance'] - df.loc[i, 'principal']
    else:
        pmt = -round(np.pmt(wac/payments_year, years*payments_year - i + ONE, df.loc[i - ONE, 'Balance']) ,TWO)
        SMM = ONE - (ONE - CPR * PSA) ** (ONE/TWELVE)
        df.loc[i, 'interest'] = df.loc[i - ONE, 'Balance'] * wac / payments_year
        pre_pmt = (df.loc[i - ONE, 'Balance'] - (pmt - df.loc[i, 'interest'])) * SMM
        df.loc[i, 'principal'] = min(df.loc[i - ONE, 'Balance'], pmt - df.loc[i, 'interest'] + pre_pmt)
        df.loc[i, 'Balance'] = df.loc[i - ONE, 'Balance'] - df.loc[i, 'principal']

# If projected month, all these should set to zero
for i in np.arange(ZERO, cap_period):
    df.loc[:, 'Net-PPIS'] = ZERO_F
    df.loc[:, 'Fresh Cils'] = ZERO_F
    df.loc[:, 'Cils Paid'] = ZERO_F
    df.loc[:, 'Cils Outstanding'] = ZERO_F
    df.loc[:, 'Fresh Cpls'] = ZERO_F
    df.loc[i, '%Outstanding'] = "{0:.0f}".format(df.loc[i, 'Balance'] / principal * HUNDRED)

df = df.round(TWO)

df.loc[:, 'PTR Rate'] = (df.loc[:, 'interest'] / df.loc[:, 'Balance'].shift(ONE)) * payments_year * HUNDRED
df.loc[ZERO, 'PTR Rate'] = ZERO_F
df.loc[:, 'Balance'] = df.loc[:, 'Balance'].apply(lambda x: '{:.2f}'.format(x))
df.loc[:, 'PTR Rate'] = df.loc[:, 'PTR Rate'].apply(lambda x: '{:.5f}'.format(x))

for i in np.arange(cap_period):
    if (float(df.loc[i, 'interest']) == ZERO_F) and (float(df.loc[i, 'principal']) == ZERO_F) and i != ZERO:
        df = df.drop(i)

print(df)
`

if float(df['Balance'].iloc[-ONE]) != ZERO_F:
    print("WARNING, the bond does not pay down to zero, the end bal is %d", df['Balance'].iloc[-ONE])
else:
    pass
