import pandas as pd

def problem22():
    names = pd.read_csv('/home/lin/Downloads/pandas-cookbook/names.txt',header=None, keep_default_na=False)
    namesorted=names.iloc[0].order()

    namesscore=0
    for i in range(len(namesorted)):
        namescore=sum(ord(x)-64 for x in namesorted.iloc[i])
        namesscore += namescore*(i+1)

    print (namesscore)

problem22()