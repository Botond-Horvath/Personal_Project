import csv

def loadList(fileName):
    with open(fileName, newline='') as csv_file:
        reader = csv.reader(csv_file)
        dataList = list(reader)
    return dataList