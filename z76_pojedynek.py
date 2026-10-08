class Postacie:
    def __init__(self, imie, zdrowie, atak, obrona):
        self.imie = imie
        self.zdrowie = zdrowie
        self.atak = atak
        self.obrona = obrona

    def atakuj(self, przeciwnik):
        obrazenia = self.atak - przeciwnik.obrona
        if obrazenia > 0:
            przeciwnik.zdrowie -= obrazenia
            print(f"{self.imie} zadaje {obrazenia} obrażeń {przeciwnik.imie}.")
        else:
            print(f"{self.imie} nie zadaje obrażeń {przeciwnik.imie}.")

    def czy_zyje(self):
        return self.zdrowie > 0