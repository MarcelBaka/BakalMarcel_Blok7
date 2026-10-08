
"""Przykład 26: test dwoch obiektow i trzecia postac za darmo."""


class Postac:
    """Postac w grze: ma imie, zycie i sile."""

    def __init__(self, imie, hp, sila):
        self.imie = imie
        self.hp = hp
        self.sila = sila


# --- TEST DWOCH OBIEKTOW ---------------------------------------------------
# Sprawdzamy, czy obiekty naprawde maja wlasne dane.

bohater = Postac("Varek", 100, 12)
goblin = Postac("Goblin", 40, 7)

print("przed zmiana:")
print("  bohater.hp =", bohater.hp, "  goblin.hp =", goblin.hp)

bohater.hp = bohater.hp - 30          # zmieniamy TYLKO bohatera

print("po odjeciu 30 bohaterowi:")
print("  bohater.hp =", bohater.hp, "  goblin.hp =", goblin.hp)
print("  goblin nie zmienil sie ani o punkt - ma wlasne dane")
print()

# --- TRZECIA POSTAC NIC NIE KOSZTUJE ---------------------------------------
szczur = Postac("Szczur", 15, 3)

druzyna = [bohater, goblin, szczur]
print("wszystkie postacie w grze:")
for postac in druzyna:
    print(f"  {postac.imie}: {postac.hp} HP, sila {postac.sila}")
print()

# --- NAJSILNIEJSZA ---------------------------------------------------------
najsilniejsza = druzyna[0]
for postac in druzyna:
    if postac.sila > najsilniejsza.sila:
        najsilniejsza = postac
print("najsilniejsza postac:", najsilniejsza.imie)

# --- LACZNE ZYCIE ----------------------------------------------------------
suma = 0
for postac in druzyna:
    suma = suma + postac.hp
print("laczne zycie wszystkich postaci:", suma)