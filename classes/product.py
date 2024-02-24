import csv


class Product:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        return

    def editProduct(self,name, quantity, price, path):
        import csv

        dataFile = "./databases/productList.csv"
        allData = []
        with open(file=dataFile, mode="r") as fileH:
            reader = csv.reader(fileH)
            for row in reader:
                if row != []:
                    temp = [row[0], row[1], row[2], row[3]]
                    allData.append(temp)
        for row in allData:
            if row != allData[0] and row != []:
                if row[0] == name:
                    if quantity != "":
                        row[1] = quantity
                    if price != "":
                        row[2] = price
                    if path != "":
                        row[3] = path

        with open(file=dataFile, mode="w", newline="") as fileH:
            writer = csv.writer(fileH, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(allData)
        fileH = open(dataFile, mode="r")
        tempData = fileH.readlines()
        for line in tempData:
            if line == []:
                del line
        fileH = open(dataFile, mode="w")
        fileH.writelines(tempData)
