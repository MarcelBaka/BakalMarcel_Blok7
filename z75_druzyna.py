# bohater_imie = "Varek"
# bohater_hp = 100
# bohater_sila = 12

# bohater_imie = "Marek"
# bohater_hp = 78
# bohater_sila = 11

# bohater_imie = "Mirek"
# bohater_hp = 120
# bohater_sila = 15

# bohater_imie = "Bartosz"
# bohater_hp = 10
# bohater_sila = 6

# bohater_imie = "Igor"
# bohater_hp = 100
# bohater_sila = 12

lista_p = [
    ("Varek", 100, 12),
    ("Marek", 78, 11),
    ("Mirek", 120, 15),
    ("Bartosz", 10, 6),
    ("Igor", 100, 12),
]

class Postac:
    def __init__(self, imie, hp, sila):
        self.imie = imie
        self.hp = hp
        self.sila = sila

druzyna = [Postac(*p) for p in lista_p]

najsilniejsza = druzyna[1]
for postac in druzyna:
    if postac.sila > najsilniejsza.sila:
        najsilniejsza = postac
print("najsilniejsza postac:", najsilniejsza.imie)

najmniejhp = druzyna[2]
for postac in druzyna:
    if postac.hp < najmniejhp.hp:
        najmniejhp = postac
print("najmniej hp:", najmniejhp.imie)


sredniahp = druzyna[1]
sredniahp = 0

for postac in druzyna:
    sredniahp = sredniahp + postac.hp
sredniahp = sredniahp / len(druzyna)
print("srednie hp:", sredniahp)