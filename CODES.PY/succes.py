class today:
    def __init__(self, real=0 ,imag=0):
        self.imagp=imag
        self.realp=real
        print("constructor from the class")
        
    def display(self):
        print(" {0}i + {1}j".format(self.realp,self.imagp))
        
ob=today(40,50)
ob2=today(50,60)
ob.display()
ob2.display()
