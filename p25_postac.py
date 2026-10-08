"""Przykład 25: ta sama gra, ale z klasa. Jeden przepis, dwie postacie."""


class Postac:
    """Postac w grze: ma imie, zycie i sile."""

    def __init__(self, imie, hp, sila):
        self.imie = imie
        self.hp = hp
        self.sila = sila


def opis(postac):
    """Teraz wystarczy JEDEN argument - cala postac."""
    return f"{postac.imie}: {postac.hp} HP, sila {postac.sila}"


def zadaj_cios(atakujacy, cel):
    """Obie postacie podane w calosci - nie da sie pomylic danych."""
    cel.hp = cel.hp - atakujacy.sila
    if cel.hp < 0:
        cel.hp = 0
    print(f"{atakujacy.imie} uderza: {cel.imie} traci {atakujacy.sila} HP")


# Dwie postacie z jednego przepisu.
bohater = Postac("Varek", 100, 12)
goblin = Postac("Goblin", 40, 7)

print("--- POJEDYNEK ---")
print(opis(bohater))
print(opis(goblin))
print()

runda = 1
while bohater.hp > 0 and goblin.hp > 0:
    print(f"runda {runda}")
    zadaj_cios(bohater, goblin)
    if goblin.hp > 0:
        zadaj_cios(goblin, bohater)
    print("  ", opis(bohater))
    print("  ", opis(goblin))
    runda = runda + 1

print()
if bohater.hp > 0:
    print(f"Wygrywa {bohater.imie}")
else:
    print(f"Wygrywa {goblin.imie}")