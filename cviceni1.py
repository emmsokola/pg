def add(a, b):
    c = a + b
    return c 

def mul(a, b, c):
    vysledek = a * b * c
    return vysledek

def div(a, b):
    if b == 0:
        # prvni čast kdy je b 0
        vysledek = 0
    else:
        # druha cast, kdy b je nenulové
        vysledek = a / b
    return vysledek

def je_delitelne_beze_zbytku(a, b):
    x = a % b
    if x == 0:
        return "je delitelne beze zbytku"
    else:
        return "neni delitelne beze zbytku"
    # pro formátování  return f"(a) je delitelne beze zbytku (b)"

def je_delitelne_3(a):
    return je_delitelne_beze_zbytku(a, 3)
    # svolám tu funkci, kterou jsem použila už předtím, než abych to kopírovala a přepisovala

if __name__ == "__main__":
    # x = add(1, 2)
    # x = mul(100, 2, 3)
    # x = div(10, 0)
    # vysledek = je_delitelne_beze_zbytku(10, 5)
    vysledek = je_delitelne_3(10)
    print(vysledek)
