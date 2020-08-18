class Departmental:
    def __init__(self):
        self.Prod_Name = "NULL"
        self.Dis_Price = 0
        self.Dis_type = "N"
        self.Listprice = 0
        self.Net =  0
    def Accept(self):
        i = input
        self.prod_name = i("Enter product name")
        self.Listprice = i("Enter list price")
        self.Dis_type = i("Enter dicount type")
        self.Cal_Price()
    def ShowBill(self):
        print {
            "Product Name": self.Prod_Name,
            "List Price": self.Listprice,s
            "Discount price": self.Dis_Price,
            "Net Price": self.Net
        }
    def Cal_Price(self):
        if self.Dis_type == "N":
            self.Dis_Price = 0.1*self.Listprice
            return self.Listprice - self.Dis_Price
        elif self.Dis_Type == "F":
            self.Dis_Price = (1-(0.9*0.93))*self.Listprice
            return self.Listprice - self.Dis_Price
