"""Przykład 24: od rysunku do kodu. Klasa Pocisk i JEDEN obiekt."""

import pygame,Pocisk

SZEROKOSC, WYSOKOSC = 820, 460
FPS = 60

TLO = (28, 28, 40)
BIALY = (235, 235, 230)
SZARY = (150, 150, 170)
RAMKA = (90, 150, 240)
PRZEGRODA = (44, 46, 62)


class Pocisk:
    """Jeden pocisk lecacy w prawo."""

    def __init__(self, x, y, predkosc, promien, kolor):
        self.x = x
        self.y = y
        self.predkosc = predkosc
        self.promien = promien
        self.kolor = kolor

    def wystrzel(self, x, y):
        """Ustawia pocisk na nowej pozycji startowej."""
        self.x = x
        self.y = y

    def lec(self, dt):
        """Przesuwa pocisk w prawo."""
        self.x = self.x + self.predkosc * dt

    def poza_ekranem(self):
        """Zwraca True, gdy pocisk wylecial poza prawa krawedz."""
        return self.x - self.promien > SZEROKOSC

    def rysuj(self, ekran):
        pygame.draw.circle(ekran, self.kolor, (self.x, self.y), self.promien)


# ---------------------------------------------------------------------------
# Ponizsza funkcja rysuje tabliczke obiektu. To tylko ozdoba tej lekcji -
# nie jest czescia nauki o klasach.
# ---------------------------------------------------------------------------

def rysuj_tabliczke(ekran, czcionka, pocisk):
    """Rysuje pudelko z trzema przegrodami dla podanego pocisku."""
    pudelko = pygame.Rect(30, 90, 300, 290)
    pygame.draw.rect(ekran, PRZEGRODA, pudelko, 0, 6)
    pygame.draw.rect(ekran, RAMKA, pudelko, 2, 6)

    naglowek = czcionka.render("pocisk : Pocisk", True, BIALY)
    ekran.blit(naglowek, (pudelko.x + 16, pudelko.y + 12))
    pygame.draw.line(ekran, BIALY, (pudelko.x + 16, pudelko.y + 34),
                     (pudelko.x + 16 + naglowek.get_width(), pudelko.y + 34))

    pygame.draw.line(ekran, RAMKA, (pudelko.left, pudelko.y + 48),
                     (pudelko.right, pudelko.y + 48))

    dane = [
        f"x = {pocisk.x:.1f}",
        f"y = {pocisk.y}",
        f"predkosc = {pocisk.predkosc}",
        f"promien = {pocisk.promien}",
        f"kolor = {pocisk.kolor}",
    ]
    for i, linia in enumerate(dane):
        ekran.blit(czcionka.render(linia, True, BIALY),
                   (pudelko.x + 16, pudelko.y + 60 + i * 24))

    pygame.draw.line(ekran, RAMKA, (pudelko.left, pudelko.y + 190),
                     (pudelko.right, pudelko.y + 190))

    metody = ["wystrzel(x, y)", "lec(dt)", "poza_ekranem()", "rysuj(ekran)"]
    for i, linia in enumerate(metody):
        ekran.blit(czcionka.render(linia, True, SZARY),
                   (pudelko.x + 16, pudelko.y + 202 + i * 22))


pygame.init()
ekran = pygame.display.set_mode((SZEROKOSC, WYSOKOSC))
pygame.display.set_caption("Pocisk - jeden obiekt")
zegar = pygame.time.Clock()
czcionka = pygame.font.Font(None, 24)
duza = pygame.font.Font(None, 30)

# JEDEN obiekt. Tyle wystarczy, zeby zobaczyc wszystko, co robi klasa.
pocisk = Pocisk(400, 250, 420, 10, (255, 210, 90))
wystrzaly = 0

dziala = True
while dziala:
    dt = zegar.tick(FPS) / 1000

    for zdarzenie in pygame.event.get():
        if zdarzenie.type == pygame.QUIT:
            dziala = False
        elif zdarzenie.type == pygame.KEYDOWN:
            if zdarzenie.key == pygame.K_ESCAPE:
                dziala = False
            elif zdarzenie.key == pygame.K_SPACE:
                pocisk.wystrzel(400, 250)
                wystrzaly = wystrzaly + 1

    pocisk.lec(dt)

    ekran.fill(TLO)

    pygame.draw.line(ekran, (50, 52, 70), (360, 250), (SZEROKOSC, 250), 2)
    pocisk.rysuj(ekran)

    rysuj_tabliczke(ekran, czcionka, pocisk)

    ekran.blit(duza.render("Jeden obiekt klasy Pocisk", True, BIALY), (30, 36))
    if pocisk.poza_ekranem():
        ekran.blit(czcionka.render("poza_ekranem() -> True", True, (240, 120, 120)),
                   (360, 300))
    else:
        ekran.blit(czcionka.render("poza_ekranem() -> False", True, (120, 210, 140)),
                   (360, 300))
    ekran.blit(czcionka.render(f"wystrzalow: {wystrzaly}", True, SZARY), (360, 330))
    ekran.blit(czcionka.render("SPACJA - wystrzel     ESC - koniec", True, SZARY),
               (30, WYSOKOSC - 32))

    pygame.display.flip()

pygame.quit()
