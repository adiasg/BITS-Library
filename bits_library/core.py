import pandas as pd
import os
import time

data_file = 'data/example.csv'
data = None
last_read = 0

def getEntries():
    global data
    global last_read
    print("Last Read:\t", last_read)
    print("Last Modified:\t", os.path.getmtime(data_file))
    if os.path.getmtime(data_file)<last_read and data is not None:
        return data
    print("[*] Reading file:", data_file)
    data = pd.read_csv(data_file)
    last_read = time.time()
    return data
