import pandas as pd
import os
import time

thesis_data_file = 'data/example.csv'
thesis_data = None
last_read = 0

def getThesisData():
    global thesis_data
    global last_read
    print("Last Read:\t", last_read)
    print("Last Modified:\t", os.path.getmtime(thesis_data_file))
    if os.path.getmtime(thesis_data_file)<last_read and thesis_data is not None:
        return thesis_data
    print("[*] Reading file:", thesis_data_file)
    thesis_data = pd.read_csv(thesis_data_file)
    last_read = time.time()
    return thesis_data
