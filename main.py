'''
csapat;versenyzo;eletkor;palya;korido;kor
Versenylovak;Fürge Ferenc;29;Gran Prix Circuit;00:01:11;1
'''
class Koridok:
    def __init__(self, sor):
        csapat, versenyzo, eletkor, palya, korido, kor = sor.strip().split(";")
        self.csapat = csapat
        self.versenyzo = versenyzo
        self.eletkor = eletkor
        self.palya = palya
        self.korido = korido
        self.kor = kor

lista = []
with open("autoverseny.csv") as f:
    f.readline()
    for sor in f:
        lista.append(Koridok(sor))
        
#3. feladat
print(f"3. feladat: {len(lista)}")

#4. feladat
szam = 0
for sor in lista:
    if sor.versenyzo == "Fürge Ferenc" and sor.palya == "Gran Prix Circuit" and sor.kor == "3":
        if int(sor.korido[:2]) > 0:
            szam += int(sor.korido[:2]) * 3600
        if int(sor.korido[3:5]) > 0:
            szam += int(sor.korido[3:5]) * 60
        if int(sor.korido[6:8]) > 0:
            szam += int(sor.korido[6:8]) 
        print(f"4. feladat: {szam} másodperc")
        
#5. feladat
print(f"5. feladat")
szemely = input("Kérem egy versenyző nevét: ")

#6. feladat
for sor in lista:
    if sor.versenyzo == szemely:
        leggyorsabb = min(lista, key=lambda x:x.korido)
        print(f"6. feladat: {leggyorsabb.palya}, {leggyorsabb.korido} ")
        break
    if sor.versenyzo != szemely:
        print(f"6. feladat: Nincs ilyen versenyző az állományban!")
        break


