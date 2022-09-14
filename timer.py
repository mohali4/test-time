from threading import Thread
from time import sleep, time as now


class time(float) :

    @property
    def now (self):
        return type(self)(now())

    @property
    def Asecounds (self):
        return int(self)
    
    @property
    def secounds (self):
        return int(self % 60)

    @property
    def Aminutes (self):
        return int(self.Asecounds // 60)
    
    @property
    def minutes (self):
        return int(self.Aminutes % 60)

    @property
    def Ahours (self):
        return int(self.Aminutes // 60)
    
    @property
    def hours (self):
        return self.Ahours


    def __sub__ (self,friend):
        return (type(self))(float.__sub__(friend,float(self))) 
    
    def __add__ (self,friend):
        return type(self)(float.__add__(float(self),friend))
    
    def __mul__ (self,other):
        return type(self)(float.__mul__(float(self), other))
    
    def __pow__(self,other):
        return type(self)(float.__pow__(float(self),other))
    
    def __mod__(self,other):
        return type(self)(float.__mod__(float(self),other))
