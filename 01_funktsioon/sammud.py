# Funktsioon arvutab sammude põhjal läbitud vahemaa.

def sammud_kilomeetriteks(sammud):
    samm_pikkus = 0.75  # meetrites
    
    meetrid = sammud * samm_pikkus
    kilomeetrid = meetrid / 1000
    
    print("Sammud:", sammud)
    print("Läbitud:", meetrid, "m ehk", kilomeetrid, "km")
    
    if sammud >= 10000:
        print("Päevane 10 000 sammu eesmärk on täidetud!")
    else:
        puudu = 10000 - sammud
        print("Eesmärgist puudu:", puudu, "sammu")
    print()


# näidisandmed
sammud_kilomeetriteks(3000)
sammud_kilomeetriteks(8500)
sammud_kilomeetriteks(12000)
