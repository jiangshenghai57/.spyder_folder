# -*- coding: utf-8 -*-
"""
Spyder Editor

Data srubbing for citi deals
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

df = pd.read_csv('e:/cititax/dataout.csv',header = None, index_col = False, parse_dates = False )

# DataFrame indexing [Col][row]
# indexing convention df[0][:] = {1, 2, 3, ..... 30, 31, 32}, periods
# indexing convention df[1][1:] = {income array}
# indexing convention df[1:][0] = {deal name array}

loan_count = 0
dealname_list = []

# Remove 1 stddev outlier and reset y array
def remove_outliers(_list_):
    # Hard coded stddev and ave
    _list_std = np.std(_list_)
    _list_ave = np.average(_list_)
    results = []

    for i in range(0, len(_list_)):
        if (_list_[i] > (_list_ave + _list_std)) or (_list_[i] < (_list_ave - _list_std)):
            results.append(_list_[i])

    for i in range(0, len(results)):
        _list_.remove(results[i])

    return _list_

# Remove 2 stddev outlier and rest y array
def remove_outliers_2(_list_):
    # Hard coded stddev and ave
    _list_std = np.std(_list_)
    _list_ave = np.average(_list_)
    results = []

    for i in range(0, len(_list_)):
        if (_list_[i] > (_list_ave + _list_std * 2)) or (_list_[i] < (_list_ave - _list_std * 2)):
            results.append(_list_[i])

    for i in range(0, len(results)):
        _list_.remove(results[i])

    return _list_

# column zero is just a index ref
for col in range(1,299):
    # Setting up the income array to be graphed
    y = np.array(df[col][1:])
    y = list(y)
    for i in range(0, len(y)):
        y[i] = float(y[i])

    # Take out the Nan in the array, not all deals have 32 periods
    y = [value for value in y if not math.isnan(value)]

    # Reset y
#    if len(y) > 2:
#        remove_outliers_2(y)

    # Creating an array mathces with y's length for x inputs
    x = list(range(1, len(y) + 1))


    p = np.poly1d(np.polyfit(x, y, 1))
    p2 = np.poly1d(np.polyfit(x, y, 2))
    # p3 = np.poly1d(np.polyfit(x, y, 3))

    slope_co_1deg = list(np.polyfit(x, y, 1))
#    slope_co_2deg = list(np.polyfit(x, y, 2))
#    slope_co_3deg = list(np.polyfit(x, y, 3))

    # Projection formula
    next_qrt_proj = slope_co_1deg[0] * (x[-1] + 1) + slope_co_1deg[1]
    qrt_2_proj = slope_co_1deg[0] * (x[-1] + 2) + slope_co_1deg[1]
    qrt_3_proj = slope_co_1deg[0] * (x[-1] + 3) + slope_co_1deg[1]
    qrt_4_proj = slope_co_1deg[0] * (x[-1] + 4) + slope_co_1deg[1]

#    We are only considering the negative slope and negative projection within the next 4 quarters
#    (next_qrt_proj < 0) or (qrt_2_proj < 0) or (qrt_3_proj < 0) or (qrt_4_proj < 0)
#    slope_co_1deg[0] < 0
    if ((next_qrt_proj < 0) or (qrt_2_proj < 0) or (qrt_3_proj < 0) or (qrt_4_proj < 0)):
        print("_______________________________________________________________________________")
        loan_count = loan_count + 1
        print("Deal name: " +df[col][0])
        dealname_list.append(df[col][0])
        print("")

        print("Fitted line formula: " + "y = " + str(slope_co_1deg[0]) + " * x + " + str(slope_co_1deg[1]))
        print("")
        #print("2-degree coefficient: " + "y = " + str(slope_co_2deg[0]) + "*x^2 + " + str(slope_co_2deg[1]) + "*x + " + str(slope_co_2deg[2]))
        #print("3-degree coefficient: " + "y = " + str(slope_co_3deg[0]) + "*x^3 + " + str(slope_co_3deg[1]) + "*x^2 + " + str(slope_co_3deg[2]) + "*x" + str(slope_co_3deg[3]))

        # Projection formula
        print("Next quarter projection is going to be " + str(next_qrt_proj))
        print("2 quarters from now projection is going to be " + str(qrt_2_proj))
        print("3 quarters from now projection is going to be " + str(qrt_3_proj))
        print("4 quarters from now projection is going to be " + str(qrt_4_proj))

        xp = np.linspace(0, len(y) + 4, num = 50, endpoint=True)
        plt.plot(x, y,"*", label = "Income Payment")
        plt.plot(xp, p(xp), "-", label="Linear Progression")
        plt.plot(xp, p2(xp), "--", label = "Qudratic")
        plt.xlabel("Quarters")
        plt.ylabel("Income")
        max_num_y = max(y) + 100000
        min_num_y = min(y) + 100000

        plt.ylim(min_num_y, max_num_y)
        plt.legend(loc = "upper left", bbox_to_anchor=[0, 1], ncol = 2, shadow= True, title = str(df[col][0]))
        plt.show()
#        plt.savefig("plot" + str(col) + ".png", dpi = 100)


        print("")
        print("")

for j in range(0, len(dealname_list)):
    print(dealname_list[j])

print("_______________________________________________________________________________")
print("")
print("There are/is " + str(loan_count) + " loan(s) with negative income projections within the next four quarters.")
