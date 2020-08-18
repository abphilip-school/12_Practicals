class ITEMINFO:
    def __init__(self):
        self.ICode = 0
        self.Item = " "
        self.Price = 0
        self.Qty = 0
        self.Discount = 0
        self.Netprice = 0
        
    def FindDisc(self):
        if(self.Qty<=10):
            self.Discount = 0
            return
        if(self.Qty<=20):
            self.Discount = 15
            return
        self.Discount = 20
        
    def Buy(self):
        i = input
        self.ICode = i('Enter ICode')
        self.Item = i('Enter Item')
        self.Price = i('Enter Price')
        self.Qty = i('Enter Qty')
        
    def ShowAll(self):
        print {
            "ICode": self.ICode,
            "Item": self.Item,
            "Price": self.Price,
            "Qty": self.Qty,
            "Discount": self.Discount
        }

