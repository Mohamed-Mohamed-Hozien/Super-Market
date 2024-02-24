import csv


class Manage:
    def __init__(self):
        self.products = self.viewAllProducts()
        self.cashiers = self.viewCashiers()
        return

    def viewCashiers(self):
        import csv

        firstRow = True
        cashiers = []
        with open("./databases/Cashiers.csv", mode='r') as cl:
            csv_reader = csv.reader(cl, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in csv_reader:
                if firstRow:
                    firstRow = False
                else:
                    cashiers.append(dict(name=row[0], salary=row[1], phone=row[2], NID=row[3]))
        return cashiers

    def addProduct(self, name, quantity, price, path):
        import csv
        products = []
        with open('./databases/productsList.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row == []:
                    pass
                products.append(row)
            csvfile.close()
        isExisted = False
        for p in products:
            if name != p[0]:
                pass
            else:
                isExisted = True
                break
        if not isExisted:
            products.append([name, quantity, price, path])
            with open('./databases/productsList.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                for product in products:
                    writer.writerow(product)

            return 1
        else:
            return 0


    def delProduct(self, name):
        for i in self.products:
            if name == i.name:
                del i
                break
        with open("./databases/productsList.csv", mode="r") as productList:
            csvReader = csv.reader(productList, delimiter=',')
            line = 0
            editedRows = []
            for row in csvReader:
                if line == 0:
                    editedRows.append(row)
                else:
                    if row[0] != name:
                        editedRows.append(row)
        with open("./databases/productsList.csv", mode="w",newline="") as productList:
            csvWriter = csv.writer(productList, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            csvWriter.writerows(editedRows)

    def viewAllProducts(self):
        import csv
        data = []
        firstRow = True
        with open(file="./databases/productsList.csv", mode="r") as fileH:
            reader = csv.reader(fileH, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                if firstRow:
                    firstRow = False
                else:
                    data.append(dict(name=row[0], quantity=row[1], price=row[2], pic_path=row[3]))
        return data
