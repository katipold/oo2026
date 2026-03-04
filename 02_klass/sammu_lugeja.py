# Klass sammude ja läbitud vahemaa arvutamiseks
class Sammulugeja:

    def __init__(self, nimi, sammud, samm_pikkus):
        self.nimi = nimi
        self.sammud = sammud
        self.samm_pikkus = samm_pikkus

    def kuva_andmed(self):
        meetrid = self.sammud * self.samm_pikkus
        kilomeetrid = meetrid / 1000

        print("Nimi:", self.nimi)
        print("Sammud:", self.sammud)
        print("Sammu pikkus:", self.samm_pikkus, "m")
        print("Läbitud:", kilomeetrid, "km")

        if self.sammud >= 10000:
            print("10 000 sammu eesmärk täidetud!")
        else:
            print("Eesmärk täitmata")
        print()

isik1 = Sammulugeja("Mari", 9999, 0.70)
isik2 = Sammulugeja("Jaan", 10005, 0.80)

isik1.kuva_andmed()
isik2.kuva_andmed()
