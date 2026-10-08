"""Przykład 24: gra bez klas. Dwie postacie - szesc zmiennych."""

# --- dane pierwszej postaci ---
bohater_imie = "Varek"
bohater_hp = 100
bohater_sila = 12

# --- dane drugiej postaci ---
goblin_imie = "Goblin"
goblin_hp = 40
goblin_sila = 7


def opis(imie, hp, sila):
    """Zwraca opis postaci. Trzeba podac komplet danych."""
    return f"{imie}: {hp} HP, sila {sila}"


def zadaj_cios(imie_atakujacego, sila_atakujacego, imie_celu, hp_celu):
    """Odejmuje zycie celowi i zwraca jego nowe hp."""
    hp_celu = hp_celu - sila_atakujacego
    if hp_celu < 0:
        hp_celu = 0
    print(f"{imie_atakujacego} uderza: {imie_celu} traci {sila_atakujacego} HP")
    return hp_celu


print("--- POJEDYNEK ---")
print(opis(bohater_imie, bohater_hp, bohater_sila))
print(opis(goblin_imie, goblin_hp, goblin_sila))
print()

runda = 1
while bohater_hp > 0 and goblin_hp > 0:
    print(f"runda {runda}")
    goblin_hp = zadaj_cios(bohater_imie, bohater_sila, goblin_imie, goblin_hp)
    if goblin_hp > 0:
        bohater_hp = zadaj_cios(goblin_imie, goblin_sila, bohater_imie, bohater_hp)
    print("  ", opis(bohater_imie, bohater_hp, bohater_sila))
    print("  ", opis(goblin_imie, goblin_hp, goblin_sila))
    runda = runda + 1

print()
if bohater_hp > 0:
    print(f"Wygrywa {bohater_imie}")
else:
    print(f"Wygrywa {goblin_imie}")

print()
print("--- A TERAZ POMYLKA, KTOREJ PYTHON NIE ZAUWAZY ---")
# Mieszamy dane dwoch postaci. Program wypisze bzdure i nie zglosi bledu.
print(opis(bohater_imie, goblin_hp, bohater_sila))