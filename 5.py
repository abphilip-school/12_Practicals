class employee:
    def getData(self):
        i=input
        self.e_no = i("Employee Number: ")
        self.name = i("Name: ")
        self.des = i("Designation: ")
        self.addr = i("Address: ")
        self.phone = i("Phone: ")
        
    def putData(self):
        print {
            "Employee Number": str(self.e_no),
            "Employee Name": str(self.name),
            "Employee Designation": str(self.des),
            "Employee Address": str(self.addr),
            "Employee Phone": str(self.phone),
        }
