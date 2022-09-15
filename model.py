from time import time as now


class time(float) :


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

    @property
    def milisecounds(self):
        return ((self%1)//0.01)

    def __sub__ (self,friend):
        return (type(self))(float.__sub__(float(self),friend)) 
    
    def __add__ (self,friend):
        return type(self)(float.__add__(float(self),friend))
    
    def __mul__ (self,other):
        return type(self)(float.__mul__(float(self), other))
    
    def __pow__(self,other):
        return type(self)(float.__pow__(float(self),other))
    
    def __mod__(self,other):
        return type(self)(float.__mod__(float(self),other))

    @classmethod
    def from_minutes(cls,num):
        return cls.from_secounds(num*60)

    @classmethod
    def from_secounds(cls,num):
        return cls(num)

    @classmethod
    def from_hours(cls,num):
        return cls.from_minutes(num*60)

    @classmethod
    def from_milisecounds(cls,num):
        return cls.from_secounds(num/100)

    @classmethod
    def now (cls):
        return cls(now())

    @property
    def type (self):
        return type(self)

    @property
    def delta_now (self):
        return self.type.now() - self

    @property
    def float(self):
        return float(self)

    def iso(self,format='{m}:{s}:{ms}'):
        def iso (num):
            num = int(num//1)
            if len(str(num)) == 2:
                return str(num)
            return '0'+str(num)
        h = iso(self.hours)
        m = iso(self.minutes)
        s = iso(self.secounds)
        ms = iso(self.milisecounds)
        return format.format(**{'h':h,'m':m,'s':s,'ms':ms})
