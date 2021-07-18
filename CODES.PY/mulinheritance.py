class base1:
    def sasuke(self):
        print('sasuke using sharingan')

class base2:
    def naruto(self):
        print('naruto using rasengan from base2')

class base3:
    def kakashi(self):
        print('kakashi using chidori from base3')


class team7(base1,base2,base3):
    def leaf(self):
        print('sakura from leaf')

ob=team7()
ob.sasuke()
ob.naruto()
ob.kakashi()
ob.leaf()
