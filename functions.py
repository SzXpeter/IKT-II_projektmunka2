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
    file.write("Név;Darabszám;Raktár;Polc\n")
    for r in rendelesek:
        file.write("{0};{1};{2};{3}\n".format(
            r.termeknev,
            r.darab,
            r.raktar,
            r.polc
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
            eladasok.append(Eladas(f'{polc.termeknev};{polc.raktar};{db}'))
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
        print(f'\nA(z) {termek} termék:\n'
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

def rendeles_leadas(termeknev: str, darab: int):
    i = 0
    while i < len(polcok) and polcok[i].termeknev != termeknev:
        i += 1
    
    if i < len(polcok):
        rendelesek.append(Rendeles(f'{termeknev};{darab};{polcok[i].raktar};{polcok[i].polc}'))
        print('A rendelés sikeresen leadva.')
        input('<ENTER>')
    else:
        print('Nincs ilyen termékünk')
        input('<ENTER>')

    

def rendeles_teljesites():
    if len(rendelesek) == 0:
        print('Nincs leadott rendelés.')
        input('<ENTER>')
        return
    
    for r in rendelesek:
        polc_szam = ((int(r.raktar) - 1) * 15 + int(r.polc)) - 1
        polcok[polc_szam].darab += r.darab
        print(f'\tA(z) {r.termeknev} termék rendelése {r.darab} darabszámra teljesítve.')
        print('\nA rendelések teljesítve lettek.')

        rendelesek.clear()
        mentes()
        input('<ENTER>')

def fajl_urites():
    for p in polcok:
        p.termeknev = ''
        p.darab = 0
    eladasok.clear()
    rendelesek.clear()

    mentes()
    print('\nA fájlok ürítve lettek.')
    input('<ENTER>')

def polc_listazas():
    for p in polcok:
        if p.termeknev != '':
            print(f"\t{p.raktar}. raktár, {p.polc}. polc, {p.termeknev}: {p.darab} db")

    print('\nAz összes telített polc listázva')
    input('<ENTER>')

def raktar_statisztika():
    print('Raktár statisztika')
    stat = dict()
    for e in eladasok:
        if e.raktar in stat.keys():
            stat[e.raktar] += e.eladasok_szama
        else:
            stat[e.raktar] = e.eladasok_szama

    for k, v in stat.items():
        print(f'\tLegtöbbször használt raktár eladásokra: {k}. raktár - {v} eladás')
    

def legeladott_termek():
    print('Legeladottabb termék')
    stat = dict()
    for e in eladasok:
        if e.termeknev in stat.keys():
            stat[e.termeknev] += e.eladasok_szama
        else:
            stat[e.termeknev] = e.eladasok_szama

    termek_nevek: list[str] = []
    for k in stat.keys():
        termek_nevek.append(k)

    if len(termek_nevek) != 0:
        max = stat[termek_nevek[0]]
        max_nev = termek_nevek[0]
        for tn in termek_nevek:
            if stat[tn] > max:
                max = stat[tn]
                max_nev = tn
                
        print(f'\tLegeladottabb termék: {max_nev} - {max} db.')
    
    else:
        print('\tNincs még eladott termék.')

def osszes_eladott():
    print('Összes eladott termékszám')
    db = 0
    for e in eladasok:
        db += e.eladasok_szama
    
    print(f'\tÖsszes eladott termékszám: {db}')
