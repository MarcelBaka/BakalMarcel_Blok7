class Skarb:
    def __init__(self, nazwa, wartosc, waga):
        self.nazwa = nazwa
        self.wartosc = wartosc
        self.waga = waga

def opis(skarb):
    return f"Skarb: {skarb.nazwa}, Wartość: {skarb.wartosc}, Waga: {skarb.waga}"

print("---Skarby---")

skarb1 = Skarb("Złoty Miecz", 1000, 5)
skarb2 = Skarb("Diamentowy Pierścień", 500, 1)
skarb3 = Skarb("Starożytny Amulet", 2000, 2)

print(f"Łączna wartość skarbów: {skarb1.wartosc + skarb2.wartosc + skarb3.wartosc}")
print(f"Łączna waga skarbów: {skarb1.waga + skarb2.waga + skarb3.waga}")
print(opis(skarb1))
print(opis(skarb2))
print(opis(skarb3))
print("------------")
print("Skarb o najlepszym wartości do wagi:")
if skarb1.wartosc / skarb1.waga > skarb2.wartosc / skarb2.waga and skarb1.wartosc / skarb1.waga > skarb3.wartosc / skarb3.waga:
    print(opis(skarb1))
elif skarb2.wartosc / skarb2.waga > skarb3.wartosc / skarb3.waga:
    print(opis(skarb2))
else:
    print(opis(skarb3))
