class myBird:

    def __init__(self):
        print('constructor starting from myBird')

    def whatType(self):
        print("I'm a Bird")

    def canSwim(self):
        print('I think i can swim')

class myPenguin(myBird): # myPenguin extends myBird

    def __init__(self):
       # super().__init__()
        print('myPenguin class costructor')

    def whoisThis(self):
        print("I'm a penguin")

    def canRun(self):
        print(' i can run faster')

mp=myPenguin()
mp.whatType()   #function from myBird
mp.whoisThis()  #function from myPenguin
mp.canSwim()    #function from myBird
mp.canRun()     #function from myPenguin

