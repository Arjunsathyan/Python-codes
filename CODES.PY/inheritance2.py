class Uzumaki:
    
    def jutsu1(self):
        print('can activate sage mode and rasengan')

    def otherchakra(self):
        print('Has ripper death seal')

class Uchihas:

    def jutsu1(self):
        print('has chidori and susano if mangekyo sharingan is awakened')

    def otherchakra(self):
        print('has sharingan and that is enough')


def shinobi(skill):
    skill.jutsu1()
    skill.otherchakra()

naruto=Uzumaki()
sasuke=Uchihas()
shinobi(naruto)
print()
shinobi(sasuke)

