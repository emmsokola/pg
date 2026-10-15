def cislo_text(cislo):
	jednotky = {
		0: "nula",
		1: "jedna",
		2: "dva",
		3: "tři",
		4: "čtyři",
		5: "pět",
		6: "šest",
		7: "sedm",
		8: "osm",
		9: "devět",
	}
	desitky = {
		2: "dvacet",
		3: "třicet",
		4: "čtyřicet",
		5: "padesát",
		6: "šedesát",
		7: "sedmdesát",
		8: "osmdesát",
		9: "devadesát",
	}
	mezi_desitky = {
		10: "deset",
		11: "jedenáct",
		12: "dvanáct",
		13: "třináct",
		14: "čtrnáct",
		15: "patnáct",
		16: "šestnáct",
		17: "sedmnáct",
		18: "osmnáct",
		19: "devatenáct",
	}

	if type(cislo) is not int or not 0 <= cislo <= 100:
		raise ValueError("Jenom celá čísla od 0 do 100.")

	if cislo == 100:
		return "sto"
	if cislo < 10:
		return jednotky[cislo]
	if cislo < 20:
		return mezi_desitky[cislo]

	desitka = cislo // 10
	jednotka = cislo % 10
	if jednotka == 0:
		return desitky[desitka]
	return f"{desitky[desitka]} {jednotky[jednotka]}"
cislo = int(input("Zadejte celé číslo od 0 do 100: "))
print(cislo_text(cislo))
