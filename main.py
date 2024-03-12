from functions import *
from os import system

def main():
    beolvasas()

    menu_valasztas()

def menu_valasztas():
    m = '-1'
    while m != '0':
        system('cls')
        print('Menüpontok:')
        print('\t1..Új termék hozzáadása')
        
        print('\t6..Mentés a fájlba')
        
        print('\n\t0..Kilépés')
        m = input('Menüpont: ')
        match m:
            case '1':
                system('cls')
                print('Termék hozzáadása')
                tn = input('\n\tKérem a termék nevét: ')
                szam = False
                while szam == False:
                    try:
                        szam = True
                        db = int(input('\tTermék darabszáma: '))
                    except:
                        szam = False
                uj_termek(tn, db)

            case '6':
                mentes()
    mentes()

main()