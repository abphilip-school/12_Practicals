class Movie(object):
    
    def __Assign(self, c):
        if c > 5500000:
            self.__Rating = '****'
        elif c > 1000000:
            self.__Rating = '***'
        else:
            self.__Rating = '**'
    
    def Read(self):
        self.__Mcode = raw_input('Enter Mcode: ')
        self.__Type = raw_input('Enter Type: ')
        self.__Collections = int(raw_input('Enter Collections: '))
        self.__Assign(self.__Collections)
    
    def Display(self):
        print 'Mcode:', self.__Mcode
        print 'Type:', self.__Type
        print 'Collections:', self.__Collections
        print 'Rating:', self.__Rating
    
    def Ret_Rating(self):
        print "Rating: ",self.__Rating

BB = movie()
BB.Read()
BB.Display()
BB.Ret_Rating()
BB_file = open('movie1.txt','w')
pickle dump(BB,BB_file)
