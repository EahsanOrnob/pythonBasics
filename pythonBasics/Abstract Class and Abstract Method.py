from abc import ABC,abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
    
class Laptop(Computer):

    def process(self):
        print("its running")   
    
#s1=Computer()

s2=Laptop()
s2.process()