import pandas as pd

def getEntries():
    data = pd.read_csv('data/example.csv')
    return data
