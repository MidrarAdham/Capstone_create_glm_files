import csv
import pandas as pd
from itertools import cycle

#minutes hours days months weekdays value

# Read HOUSE.csv file:

df = pd.read_csv("HOUSE1.csv",header=None)

# Create a list of power values in HOUSE1.csv

#   First step, specify the column

col = df.iloc[:,1]

#   Store values in a list:

def scale_lists(m,h,d,p):
    # scale all other lists by the longest list ( power)
    m *= len(p)
    h *= len(p)

    return (m,h,sorted(d),p)


pow_lis = col.values.tolist()
mins = ['0-14','15-29','30-44','45-59']

l = [(m,h,d) for d in range(6,13) for h in range(0,24) for m in mins]

def create_sched(l):
    print('schedule demand{\n')
    l = list(zip(cycle(l),pow_lis))
    for (m,h,d),p in l:#zip(cycle(minutes_list),cycle(lis_hours),cycle(lis_days),pow_lis):
        print(f"\t{m} {h} {d} * * {p};")
    print('}')



x = create_sched(l)
