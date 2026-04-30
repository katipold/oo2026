from abc import ABC, abstractmethod

#liides -> abstraktne klass
class Arvutaja(ABC):
    @abstractmethod
    def lisa_arv(self, n):
        pass

    @abstractmethod
    def kysi_summa(self):
        pass

    @abstractmethod
    def nulli(self):
        pass

#realiseeriv klass
class LihtneArvutaja(Arvutaja):
    def __init__(self):
        self.summa = 0

    def lisa_arv(self, n):
        self.summa += n

    def kysi_summa(self):
        return self.summa

    def nulli(self):
        self.summa = 0

#testimine
def testid():
    print("Testid käivad...")

    a = LihtneArvutaja()

    assert a.kysi_summa() == 0

    a.lisa_arv(5)
    assert a.kysi_summa() == 5

    a.lisa_arv(3)
    assert a.kysi_summa() == 8

    a.nulli()
    assert a.kysi_summa() == 0

    print("Kõik testid korras ✅")


def pea():
    arvutaja = LihtneArvutaja()

    arvutaja.lisa_arv(4)
    arvutaja.lisa_arv(6)

    print("Summa:", arvutaja.kysi_summa())

    arvutaja.nulli()
    print("Pärast nullimist:", arvutaja.kysi_summa())


testid()
pea()