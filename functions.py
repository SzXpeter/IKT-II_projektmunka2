from classes import Polc, Eladas, Rendeles

polcok: list[Polc] = []
eladasok: list[Eladas] = []
rendelesek: list[Rendeles] = []

def polc_beolvasas(filename):
    file = open(filename, 'r', encoding="utf-8")
    file.readline()
    for row in file:
        polcok.append(Polc(row))
    file.close()

def eladas_beolvasas(filename):
    file = open(filename, 'r', encoding="utf-8")
    file.readline()
    for row in file:
        eladasok.append(Eladas(row))
    file.close()

def rendeles_beolvasas(filename):
    file = open(filename, 'r', encoding="utf-8")
    file.readline()
    for row in file:
        rendelesek.append(Rendeles(row))
    file.close()

def polc_beiras(filename):
    file = open(filename, 'w', encoding="utf-8")
    file.write("Raktár;Polc;Terméknév;Darabszám\n")
    for p in polcok:
        file.write("{0};{1};{2};{3}\n".format(
            p.raktar,
            p.polc,
            p.termeknev,
            p.darab
        ))
    file.close()

def eladas_beiras(filename):
    file = open(filename, 'w', encoding="utf-8")
    file.write("Név;Raktár;Eladás száma\n")
    for e in eladasok:
        file.write("{0};{1};{2}\n".format(
            e.termeknev,
            e.raktar,
            e.eladasok_szama
        ))
    file.close()

def rendelesek_beiras(filename):
    file = open(filename, 'w', encoding="utf-8")
    file.write("Név;Darabszám\n")
    for r in rendelesek:
        file.write("{0};{1}\n".format(
            r.termeknev,
            r.darab
        ))
    file.close()


def beolvasas():
    polc_beolvasas('polcok.csv')
    eladas_beolvasas('eladasok.csv')
    rendeles_beolvasas('rendelesek.csv')

def mentes():
    polc_beiras('polcok.csv')
    eladas_beiras('eladasok.csv')
    rendelesek_beiras('rendelesek.csv')

def uj_termek(termeknev: str, db: int):
    i = 0
    while i < len(polcok) and polcok[i].termeknev != '':
        i += 1 

    if i < len(polcok):
        p = polcok[i] 
    else:
        print('Nincs üres polc a raktárokban.')
        return
    
    p.termeknev = termeknev
    p.darab = db