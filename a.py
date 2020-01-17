__all__ = ["_toatal"]

class CountryOlympic():
    def __init__(self,country=None,gold = 0,silver = 0,bronze = 0):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    #def __str__(self):
        #a = vars(self)
        #print(self.__class__.__name__, a, id(self))
        #return ""
        

    def __repr__(self):
        return "{}{}".format(self.__class__.__name__, repr((self.country,self.gold,self.silver,self.bronze)))

    def _total(self):
        return self.gold + self.silver + self.bronze

class UniverseOlympic(CountryOlympic):
    def __init__(self,num_country=None,country=None,gold=0,silver=0,bronze=0):
        super().__init__(country,gold,silver,bronze)
        self.num_country = num_country
        

    def __str__(self):
        a = vars(self)
        print(self.__class__.__name__, a, id(self))
        return ""

    #def __repr__(self):
     #   return "{}{}{}".format(self.__class__.__name__, repr((self.num_country, self.country,self.gold)))

if __name__ == "__main__":
    #s1 = UniverseOlympic("LA",12,3,4)
    #print(s1)
    
    s2 = UniverseOlympic("LA","USA",12,2,3)
    print(s2)

    s3 = UniverseOlympic()
    print(s3)


