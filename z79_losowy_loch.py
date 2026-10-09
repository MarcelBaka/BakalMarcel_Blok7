import random

lista_postaci = (
    "Goblin",
    "Szczur",
    "Szkielet",
    "Wilk",
    "Ork"
)

def losuj_postc():
    imie = random.choice(lista_postaci)
    hp = random.randint(20, 100)
    sila = random.randint(2, 15)
    return imie, hp, sila

print(f"Postac 1: {losuj_postc()}")
