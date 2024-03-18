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
        if polcok[i].termeknev == termeknev:
            print('\nMár van ilyen termék.')
            input('<ENTER>')
            return
        i += 1

    if i < len(polcok):
        p = polcok[i]
    else:
        print('\nNincs üres polc a raktárokban.')
        input('<ENTER>')
        return

    p.termeknev = termeknev
    p.darab = db
    print('\nA termék fel lett véve.')
    input('<ENTER>')

def eladas(termeknev: str, db: int):
    i = 0
    while i < len(polcok) and polcok[i].termeknev != termeknev:
        i += 1

    if i >= len(polcok):    #Hamis eset
        print('\nIlyen terméket nem találtunk.')
        input('<ENTER>')
    else:
        polc: Polc = polcok[i]

        if polc.darab < db:
            print('\nNincs ennyi termék a polcon.')
            input('<ENTER>')
        else:
            polc.darab -= db
            eladasok.append(f'{polc.termeknev};{polc.raktar};{db}')
            print('\nA terméket sikeresen eladtuk.')
            input('<ENTER>')

def termek_torles(termeknev:str):
    i = 0
    while i < len(polcok) and polcok[i].termeknev != termeknev:
        i += 1
    
    if i < len(polcok):
        polcok[i].termeknev = ''
        polcok[i].darab = 0
        print('\nA termék sikeresen törölve lett.')
        input('<ENTER>')
    else:
        print('\nNincs ilyen termék.')
        input('<ENTER>')

def termek_kereses(termek: str):
    i = 0
    while i < len(polcok) and polcok[i].termeknev != termek:
        i += 1
    if i >= len(polcok):
        print('\nA termék nem létezik vagy nincs raktáron.')
        input('<ENTER>')
    else:
        print(f'A(z) {termek} termék:\n'
              f'\tA(z) {polcok[i].raktar}. raktárban,\n'
              f'\tA(z) {polcok[i].polc}. polcon található.\n'
              f'\tRaktáron lévő darabszám: {polcok[i].darab}')
        input('<ENTER>')

def polc_kereses(raktar, polc):
    i = 0
    while i < len(polcok) and (polcok[i].raktar != raktar or polcok[i].polc != polc):
        i += 1

    if i < len(polcok):
        print(f'A(z) {raktar}. számú raktár {polc}. polcán a következő termék található:')
        print('\t{0}\n\t{1}'.format(
            f'Név: {polcok[i].termeknev}',
            f'Raktáron lévő darabszám: {polcok[i].darab}'
        ))
        input('<ENTER>')
    else:
        print('\nNem találtunk ilyen polcot.')
        input('<ENTER>')
