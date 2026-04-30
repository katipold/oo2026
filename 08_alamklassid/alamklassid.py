from abc import ABC, abstractmethod

#ülemklass (abstraktne)
class Soiduk(ABC):
    def __init__(self, nimi):
        self.nimi = nimi

    @abstractmethod
    def liigu(self):
        pass


#alamklass 1
class Auto(Soiduk):
    def liigu(self):
        print(self.nimi, "sõidab maanteel")


#alamklass 2
class Jalgratas(Soiduk):
    def liigu(self):
        print(self.nimi, "sõidab kergliiklusteel")


#alamklass 3
class Buss(Soiduk):
    def liigu(self):
        print(self.nimi, "veab reisijaid")


#näitprogramm
def main():
    soidukid = [
        Auto("Toyota"),
        Jalgratas("BMX"),
        Buss("Linnabuss")
    ]

    for s in soidukid:
        s.liigu()


main()