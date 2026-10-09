bohater_imie = "Varek"
bohater_zdrowie = 100
bohater_atak = 12

bohater2_imie = "Bartosz"
bohater2_zdrowie = 100
bohater2_atak = 13

bohater3_imie = "Mirek"
bohater3_zdrowie = 120
bohater3_atak = 15

bohater4_imie = "Krzysiek"
bohater4_zdrowie = 80
bohater4_atak = 10

bohater5_imie = "Tomek"
bohater5_zdrowie = 90
bohater5_atak = 11

bohater6_imie = "Jacek"
bohater6_zdrowie = 110
bohater6_atak = 14

def opis(imie, zdrowie, atak):
    return f"{imie}: {zdrowie} HP, atak {atak}"

def zadaj_cios(imie_atakujacego, atakujacy_atak, imie_celu, cel_zdrowie):
    cel_zdrowie = cel_zdrowie - atakujacy_atak
    if cel_zdrowie < 0:
        cel_zdrowie = 0
    print(f"{imie_atakujacego} uderza: {imie_celu} traci {atakujacy_atak} HP")
    return cel_zdrowie

print("--- TURNIEJ ---")
print(opis(bohater_imie, bohater_zdrowie, bohater_atak))
print(opis(bohater2_imie, bohater2_zdrowie, bohater2_atak))
print(opis(bohater3_imie, bohater3_zdrowie, bohater3_atak))
print(opis(bohater4_imie, bohater4_zdrowie, bohater4_atak))
print(opis(bohater5_imie, bohater5_zdrowie, bohater5_atak))
print(opis(bohater6_imie, bohater6_zdrowie, bohater6_atak))

runda = 1
while (bohater_zdrowie > 0 and bohater2_zdrowie > 0) or (bohater3_zdrowie > 0 and bohater4_zdrowie > 0) or (bohater5_zdrowie > 0 and bohater6_zdrowie > 0):
    print(f"runda {runda}")
    if bohater_zdrowie > 0 and bohater2_zdrowie > 0:
        bohater2_zdrowie = zadaj_cios(bohater_imie, bohater_atak, bohater2_imie, bohater2_zdrowie)
        if bohater2_zdrowie > 0:
            bohater_zdrowie = zadaj_cios(bohater2_imie, bohater2_atak, bohater_imie, bohater_zdrowie)
        print("  ", opis(bohater_imie, bohater_zdrowie, bohater_atak))
        print("  ", opis(bohater2_imie, bohater2_zdrowie, bohater2_atak))
    if bohater3_zdrowie > 0 and bohater4_zdrowie > 0:
        bohater4_zdrowie = zadaj_cios(bohater3_imie, bohater3_atak, bohater4_imie, bohater4_zdrowie)
        if bohater4_zdrowie > 0:
            bohater3_zdrowie = zadaj_cios(bohater4_imie, bohater4_atak, bohater3_imie, bohater3_zdrowie)
        print("  ", opis(bohater3_imie, bohater3_zdrowie, bohater3_atak))
        print("  ", opis(bohater4_imie, bohater4_zdrowie, bohater4_atak))
    if bohater5_zdrowie > 0 and bohater6_zdrowie > 0:
        bohater6_zdrowie = zadaj_cios(bohater5_imie, bohater5_atak, bohater6_imie, bohater6_zdrowie)
        if bohater6_zdrowie > 0:
            bohater5_zdrowie = zadaj_cios(bohater6_imie, bohater6_atak, bohater5_imie, bohater5_zdrowie)
        print("  ", opis(bohater5_imie, bohater5_zdrowie, bohater5_atak))
        print("  ", opis(bohater6_imie, bohater6_zdrowie, bohater6_atak))
    runda = runda + 1
if runda > 6:
    print("Koniec turnieju!")