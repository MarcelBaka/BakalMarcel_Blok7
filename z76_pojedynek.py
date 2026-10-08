class Postac:
    def __init__(self, imie, zdrowie, atak):
        self.imie = imie
        self.zdrowie = zdrowie
        self.atak = atak

def opis(postac):
    return f"{postac.imie}: {postac.zdrowie} HP, atak {postac.atak}"

def zadaj_cios(atakujacy, cel):
    cel.zdrowie = cel.zdrowie - atakujacy.atak
    if cel.zdrowie < 0:
        cel.zdrowie = 0
    print(f"{atakujacy.imie} uderza: {cel.imie} traci {atakujacy.atak} HP")

bohater = Postac("Varek", 100, 12)
goblin = Postac("Goblin", 40, 7)

print("--- POJEDYNEK ---")
print(opis(bohater))
print(opis(goblin))

runda = 1
while bohater.zdrowie > 0 and goblin.zdrowie > 0:
    if bohater.atak > goblin.atak:
        print(f"runda {runda}")
        zadaj_cios(bohater, goblin)
        if goblin.zdrowie > 0:
            zadaj_cios(goblin, bohater)
        print("  ", opis(bohater))
        print("  ", opis(goblin))
        runda = runda + 1
    else:
        print(f"runda {runda}")
        zadaj_cios(goblin, bohater)
        if bohater.zdrowie > 0:
            zadaj_cios(bohater, goblin)
        print("  ", opis(bohater))
        print("  ", opis(goblin))
        runda = runda + 1

print()
if bohater.zdrowie > 0:
    print(f"Wygrywa {bohater.imie}")
else:
    print(f"Wygrywa {goblin.imie}")