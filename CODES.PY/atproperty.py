class converter:
    def __init__(self,temperature=0):
        print('assiging temperature value')
        self._temperature=temperature


    def convert_to_fahrenheit(self):
        return (self._temperature * 1.8) + 32

    def get_temperature(self):
        print('getting temperature value')
        return self._temperature
    
    def set_temperature(self,value):
        if value<-273:
            raise ValueError('Not possible')
        print('setting temp')
        self._temperature=value

    temperature=property()
    temperature=temperature.getter(get_temperature)
    temperature=temperature.setter(set_temperature



c=converter(5)
print(c.temperature)
c.temperature=100
print(c.temperature)
