class Donor(object):
    donors = []
    def __init__(self):
        self.__name = self.__dob = self.__address = self.__phno = self.__bldgrp = ""
    def Input(self):
        self.__name = raw_input("Enter name: ")
        self.__dob = raw_input("Enter DOB: ")
        self.__address = raw_input("Enter address: ")
        self.__phno = raw_input("Enter phone number: ")
        self.__bldgrp = raw_input("Enter blood group: ")
    def Append(self):
        Donor.donors.append({'name': self.__name, 'dob': self.__dob, 'address': self.__address, 'phno': self.__phno, 'bldgrp': self.__bldgrp})
    def Show(self, name):
        for donor in Donor.donors:
            if donor['name'] == name:
                return donor
    def Search(self, bldgrp):
        t = []
        for donor in Donor.donors:
            if donor['bldgrp'] == bldgrp:
                t.append(donor)
        return t

m = Donor()
i = int(raw_input("Enter the no. of times to repeat: "))
for a in range(0,i):
    m.Input()
    m.Append()
print m.Show(raw_input('Enter name to show: '))
print m.Search(raw_input('Enter blood group to search: '))
