def je_prvocislo(cislo):
    if cislo <= 1:
        return False
    delitel = 2
    while delitel * delitel <= cislo:
        if cislo % delitel == 0:
            return False
        delitel += 1
    return True

def vrat_prvocisla(maximum):
    maximum = int(maximum)
    prvocisla = []
    for cislo in range(1, maximum + 1):
        if je_prvocislo(cislo):
            prvocisla.append(cislo)
    return prvocisla

if __name__ == "__main__":
    cislo = input("Zadej maximum: ")
    prvocisla = vrat_prvocisla(cislo)
    print(prvocisla)
