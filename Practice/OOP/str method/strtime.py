

# class Time:
    
#     def __init__(self,hr,min,sec):
#         self.hr=hr
#         self.min=min
#         self.sec=sec
        
#     def __str__(self):
#         return f"{self.hr} : {self.min} : {self.sec}"
    
#     def __add__(self, other): ##override
#         thr=self.hr+other.hr
#         tmin=self.min+other.min
#         tsec=self.sec+other.sec
#         t=Time(thr,tmin,tsec)
#         return t
        
#         # return "I am additon"
# t1=Time(12,4,6)
# t2=Time(1,5,6)
# print(t1+t2)



#opertion overloading
# conversion
class Time:
    
    def __init__(self,hr,min,sec):
        self.hr=hr
        self.min=min
        self.sec=sec
        
    def __str__(self):
        return f"{self.hr} : {self.min} : {self.sec}"
    
    def __add__(self, other): ##override
        tsec=self.sec+other.sec
        addmin=tsec//60
        tsec=tsec%60
        tmin=self.min+other.min+addmin
        adhr=tmin//60
        tmin=tmin%60
        thr=self.hr+other.hr+adhr
        return Time(thr,tmin,tsec)
        
        # thr=self.hr+other.hr
        # tmin=self.min+other.min
        # tsec=self.sec+other.sec
        # t=Time(thr,tmin,tsec)
        # return t
        
        # return "I am additon"
t1=Time(12,14,60)
t2=Time(7,55,45)
print(t1+t2)