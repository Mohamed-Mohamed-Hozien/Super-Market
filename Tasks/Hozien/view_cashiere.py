def view_casheire():
    import csv

    firstRow = True
    lst = []
    with open("Casheire.csv", mode='r') as cl:
        csv_reader = csv.reader(cl)
        for line in csv_reader:
            if firstRow:
                firstRow = False
            else:
                lst.append(line)
    print(lst)
