"""
Zadanie 2 - Nawiasy

Opis zadania:
- Zweryfikuj, czy podany ciąg znaków zawiera poprawne nawiasy.
- Każdemu otwartemu nawiasowi '(' powinien odpowiadać nawias zamykający ')'.
- Jeśli nawiasy się zgadzają, funkcja ma zwrócić True, w przeciwnym wypadku False.
- Rozpatrujemy wyłącznie nawiasy okrągłe.

Przykładowe wejścia (True):
    "( if ( zero ? x ) max (/ 1 x ))"
    "I told ( that its not ( yet ) done ). (42)"
Przykładowe wejścia (False):
    ":-)"
    "Czesc (o kurcze, chyba niechcacy zamkne ten nawias dwa razy))"
    "())(("

Wymagania:
- Implementacja funkcji `check_parentheses(s: str) -> bool`.
- Użycie stosu do weryfikacji poprawności nawiasów.
"""

def check_parentheses(s: str) -> bool:
    """
    Sprawdza, czy w ciągu znaków 's' nawiasy okrągłe są poprawnie sparowane.

    Args:
        s (str): Ciąg znaków do analizy.

    Returns:
        bool: True jeśli nawiasy są poprawne, False w przeciwnym wypadku.
    """
    ### TUTAJ PODAJ ROZWIĄZANIE ZADANIA
    licznik = 0
    for znak in s:
        if znak == '(':
            licznik += 1
        elif znak == ')':
            licznik -= 1
            if licznik < 0:
                return False
    ### return False - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)
    return licznik == 0

tekst_input = input("Podaj tekst: ")
czy_poprawne = check_parentheses(tekst_input)

if czy_poprawne:
    print("True")
elif not czy_poprawne:
    print("False")