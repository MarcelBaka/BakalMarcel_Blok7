import random

imiona = ["Goblin", "Szczur", "Szkielet", "Wilk", "Ork"]
potwory = []

for _ in range(10):
    potwor = {
        "imie": random.choice(imiona),
        "zycie": random.randint(10, 60),
        "sila": random.randint(2, 15),
    }
    potwory.append(potwor)

print("--- Lista wygenerowanych potworów ---")
for i, p in enumerate(potwory, start=1):
    print(f"{i}. {p['imie']} — HP: {p['zycie']}, Siła: {p['sila']}")

# Statystyki
potwory_hp_powyzej_40 = sum(1 for p in potwory if p["zycie"] > 40)
najsilniejszy = max(potwory, key=lambda p: p["sila"])
laczne_zycie = sum(p["zycie"] for p in potwory)

print(f"1. Liczba potworów o życiu powyżej 40: {potwory_hp_powyzej_40}")
print(
    f"2. Największą siłę ma: {najsilniejszy['imie']} (Siła: {najsilniejszy['sila']})"
)
print(f"3. Łączne życie wszystkich potworów: {laczne_zycie}")