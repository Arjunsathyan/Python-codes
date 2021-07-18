#data encapsulation
class mypc:

    def __init__(self):
       self. sellingprice=2000

    def mysell(self):
        print('the selling price is',self.sellingprice)

    def setmaxprice(self,price):
        self.sellingprice=price


mp=mypc()
mp.mysell()
mp.sellingprice=7000
mp.mysell()
mp.setmaxprice(4000)
mp.mysell()
