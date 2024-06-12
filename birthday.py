# Name: Nana Kwasi Owusu
# Program Description: This is a hashable object type that can be used as a key in a hash table

class Birthday:
    def __init__(self,month,day,year):
        self.__birthmonth = month
        self.__birthday = day
        self.__birthyear = year
        
    #this is a getter that returns the birth month 
    def getMonth(self):
        return self.__birthmonth
    
    #this is a getter that returns the birth day
    def getDay(self):
        return self.__birthday
    
    #this is a getter that returns the birth year
    def getYear(self):
        return self.__birthyear
    
    #this is a method that provides a string representation of the birthday object
    def __str__(self):
        return f'{self.__birthmonth}/{self.__birthday}/{self.__birthyear}'
    
    #this is a method that returns an integer as the sum of the day, month, and year, mod 12
    def __hash__(self):
        num = int((self.__birthmonth + self.__birthday + self.__birthyear)%12)
        return num
        
    #this method tests if two birthday objects have the same attributes
    def __eq__(self,other):
        if self.__birthmonth != other.__birthmonth:
            return False
        return (self.__birthday==other.__birthday) and (self.__birthyear==other.__birthyear)
    
    
