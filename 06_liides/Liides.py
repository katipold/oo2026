from abc import ABC, abstractmethod

class Seade(ABC):
    @abstractmethod
    def kaivita(self):
        pass

    @abstractmethod
    def peata(self):
        pass


class Arvuti(Seade):
    def kaivita(self):
        print("Arvuti käivitub")

    def peata(self):
        print("Arvuti lülitub välja")


class Telefon(Seade):
    def kaivita(self):
        print("Telefon lülitub sisse")

    def peata(self):
        print("Telefon lülitub välja")


# Näitprogramm
s1 = Arvuti()
s2 = Telefon()

s1.kaivita()
s1.peata()
s2.kaivita()
s2.peata()