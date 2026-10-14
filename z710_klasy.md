Klasa to ogólny szablon, a obiekt to konkretny egzemplarz zrobiony na jego podstawie. Przykład: klasa to projekt samochodu, a obiekt to gotowe auto stojące na parkingu.

self oznacza konkretny obiekt, dla którego w tym momencie ustawiamy dane.

Po lewej stronie tworzymy zmienną przypisaną do obiektu (self.hp), a po prawej używamy wartości przekazanej do funkcji (hp).

Nie trzeba jej wywoływać ręcznie, bo Python sam uruchamia ją w tle podczas tworzenia nowego obiektu.

Sprawdzam, czy nie zrobiłem literówki w nazwie sila i czy w metodzie __init__ na pewno dopisałem self.sila.

Przy obiektach zmieniamy ich właściwości bezpośrednio w pamięci, więc zmiana od razu działa w całym programie. Zwykłe liczby czy napisy tak nie działają, więc nową wartość HP trzeba zwrócić z funkcji przez return.