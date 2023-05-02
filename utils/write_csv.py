import csv
def write_csv(filename, data):
    with open(filename, 'w', newline='') as f:
        w = csv.DictWriter(f,['Time','Funding Rate'])
        w.writeheader()
        for fund in data:
            w.writerow(fund)

