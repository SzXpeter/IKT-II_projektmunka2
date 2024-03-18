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
        print('\t2..Termék eladása')
        print('\t3..Termék törlése')
        
        print('\t6..Mentés a fájlba')
        
        print('\n\t0..Kilépés')
        m = input('\nMenüpont: ')
        match m:
            case '1':
                system('cls')
                print('Termék hozzáadása')
                tn = input('\n\tKérem az új termék nevét: ')
                db = szam_bekeres('\tTermék induló darabszáma: ')
                uj_termek(tn, db)
            case '2':
                system('cls')
                print('Termék eladása')
                tn = input('\n\tKérem az eladandó termék nevét: ')
                db = szam_bekeres('\tEladni kívánt darabszám: ')
                eladas(tn, db)

            case '3':
                system("cls")
                print("Termék törlése")
                tn = input("\n\tKérem a törölni kívánt termék nevét: ")
                termek_torles(tn)

            case '6':
                mentes()
    mentes()

def szam_bekeres(kiiras_db: str) -> int:
    szam = False
    while szam == False:
        try:
            szam = True
            db = int(input(kiiras_db))
        except:
            szam = False
    return db

main()
