import math

def je_prvocislo(cislo: int) -> bool:
    if cislo <= 1:
        return False
    if cislo == 2:
        return True
    if cislo % 2 == 0:
        return False
    hranice = int(math.isqrt(cislo))
    for delitel in range(3, hranice + 1, 2):
        if cislo % delitel == 0:
            return False
            
    return True


def vrat_prvocisla(maximum: int) -> list[int]:
    prvocisla = []
    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla


if __name__ == "__main__":
    assert je_prvocislo(1) is False
    assert je_prvocislo(2) is True
    assert je_prvocislo(3) is True
    assert je_prvocislo(100) is False
    assert je_prvocislo(101) is True

    assert vrat_prvocisla(1) == []
    assert vrat_prvocisla(2) == [2]
    assert vrat_prvocisla(3) == [2, 3]
    assert vrat_prvocisla(10) == [2, 3, 5, 7]

    print("Všechny testy proběhly úspěšně!")
