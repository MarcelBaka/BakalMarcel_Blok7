import pygame
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