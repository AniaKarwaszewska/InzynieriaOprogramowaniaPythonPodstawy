"""
Zadanie 3 - Indeksowanie dokumentów

Opis zadania:
- Wejście:
    * Pierwsza linia: liczba dokumentów do przetworzenia (n).
    * Kolejne n linii: dokumenty (każdy dokument to wielowyrazowy ciąg znaków).
    * Następna linia: liczba zapytań (m).
    * Kolejne m linii: zapytania (każdy zapytanie to pojedynczy wyraz).
- Wyjście:
    * m linii, z których każda zawiera listę numerów dokumentów, w których wystąpił wyraz z zapytania.
    * Każda lista jest posortowana według częstości wystąpienia zapytania w danym dokumencie (od największej do najmniejszej).
    * W przypadku równych częstości, lista może być posortowana malejąco wg numeru dokumentu (opcjonalnie).
    * Jeśli słowo nie wystąpiło w żadnym dokumencie, zwróć pustą listę.

Przykładowe wejście:
    3
    Your care set up, do not pluck my care down.
    My care is loss of care with old care done.
    Your care is gain of care when new care is won.
    2
    care
    is

Przykładowe wyjście:
    [1, 2, 0]
    [2, 1]

Wymagania:
- Implementacja funkcji `index_documents(documents: list[str], queries: list[str]) -> list[list[int]]`.
- Przetwarzanie tekstu – można użyć podziału na wyrazy, ignorując interpunkcję i wielkość liter.
- Obliczenie liczby wystąpień danego wyrazu w każdym dokumencie.
- Dla każdego zapytania, zwrócenie posortowanej listy indeksów dokumentów.
"""


def index_documents(documents: list[str], queries: list[str]) -> list[list[int]]:
    """
    Przetwarza dokumenty i zapytania, zwracając listy indeksów dokumentów,
    w których występuje zapytanie, posortowane według częstości wystąpienia
    danego wyrazu (malejąco), a w przypadku równych częstości - malejąco wg numeru dokumentu.

    Args:
        documents (list[str]): Lista dokumentów (każdy dokument to ciąg znaków).
        queries (list[str]): Lista zapytań (każdy zapytanie to pojedynczy wyraz).

    Returns:
        list[list[int]]: Lista wyników dla kolejnych zapytań.
    """
    ### TUTAJ PODAJ ROZWIĄZANIE ZADANIA
    wyniki = []

    przetworzone_dokumenty = []
    for dokument in dokumenty:
        dokument = dokument.lower()
        dokument = dokument.replace(",", "")
        dokument = dokument.replace(".", "")
        slowa = dokument.split()
        przetworzone_dokumenty.append(slowa)

    for zapytanie in zapytania:
        zapytanie = zapytanie.lower()
        dopasowania = []

        for numer in range(len(przetworzone_dokumenty)):
            dokument = przetworzone_dokumenty[numer]
            ile_razy = dokument.count(zapytanie)

            if ile_razy > 0:
                dopasowania.append([numer, ile_razy])

        for i in range(len(dopasowania)):
            for j in range(len(dopasowania) - 1):
                pierwsze = dopasowania[j]
                drugie = dopasowania[j + 1]

                if pierwsze[1] < drugie[1]:
                    dopasowania[j], dopasowania[j + 1] = drugie, pierwsze
                elif pierwsze[1] == drugie[1] and pierwsze[0] > drugie[0]:
                    dopasowania[j], dopasowania[j + 1] = drugie, pierwsze

        lista_numerow=[]
        for para in dopasowania:
            lista_numerow.append(para[0])

        wyniki.append(lista_numerow)

    ### return [[]] - powinno być zmienione i zwrócić prawdziwy wynik (zgodny z oczekiwaniami)
    return wyniki


# Przykładowe wywołanie:
if __name__ == "__main__":
    # Pobranie liczby dokumentów
    liczba_dokumentow = int(input("Podaj liczbę dokumentów: "))
    dokumenty = []
    print("Wprowadź kolejne dokumenty:")
    for _ in range(liczba_dokumentow):
        dokumenty.append(input())

    # Pobranie liczby zapytań
    liczba_zapytan = int(input("Podaj liczbę zapytań: "))
    zapytania = []
    print("Wprowadź kolejne zapytania:")
    for _ in range(liczba_zapytan):
        zapytania.append(input().strip())

    # Przetworzenie zapytań
    wyniki = index_documents(dokumenty, zapytania)

    # Wypisanie wyników
    print("Wyniki:")
    for wynik in wyniki:
        print(wynik)