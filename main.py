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
        print('\t4..Keresés')
        print('\t5..Rendelés leadása/teljesítése')
        print('\t6..Polcok listázása')
        print('\t7..Eladások statisztika')
        print('\t8..Fájlok ürítése')
        print('\t9..Mentés a fájlba')
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
                system('cls')
                print('Termék törlése')
                tn = input('\n\tKérem a törölni kívánt termék nevét: ')
                termek_torles(tn)

            case '4':
                    
                
                m = ''
                while m != '1' and m != '2':
                    system('cls')
                    print('Termék/Polc keresése')

                    print('\t1..Termék keresése')
                    print('\t2..Polc keresése')

                    m = input('Menüpont: ')
                
                match m:
                    case '1':
                        system('cls')
                        print('Termék keresése')
                        tn = input('\n\tKérem a keresett termék nevét: ')
                        termek_kereses(tn)
                    case '2':
                        system('cls')
                        print('Polc keresése')
                        raktar = input('Kérem a raktár számát: ')
                        polc = input('Kérem a polc számát: ')
                        polc_kereses(raktar, polc)

            case '5':
                system('cls')
                print('Rendelés leadása/teljesítése')

                m = ''
                while m != '1' and m != '2':
                    system('cls')
                    print('Rendelés leadása/teljesítése')

                    print('\n\t1..Rendelés leadása')
                    print('\t2..Rendelés teljesítése')

                    m = input('\nMenüpont: ')
                
                match m:
                    case '1':
                        system('cls')
                        print('Rendelés leadás')
                        tn = input('\n\tKérem a rendelni kívánt termék nevét: ')
                        db = szam_bekeres('\tRendelni kívánt darabszám: ')
                        rendeles_leadas(tn, db)
                    case '2':
                        system('cls')
                        print('Rendelés teljesítése\n')
                        rendeles_teljesites()

            case '6':
                system('cls')
                print('Polcok listázása\n')
                polc_listazas()

            case '7':
                
                m = ''
                while m != '0' and m != '1' and m != '2' and m != '3':
                    system('cls')
                    print('Eladások statisztika')
                    
                    print('\n\t1..Raktárok statisztikája')
                    print('\t2..Termék eladások')
                    print('\t3..Összes eladott termékszám')

                    print('\n\t0..Vissza')

                    m = input('\nMenüpont: ')

                match m:
                    case '0':
                        pass
                    case '1':
                        system('cls')
                        print('Raktár statisztika\n')
                        raktar_statisztika()
                    case '2':
                        system('cls')
                        print('Termék eladások')
                        legeladott_termek()
                    case '3':
                        system('cls')
                        print('Összes eladott termékszám')
                        # osszes_eladott()


                    

            case '8':
                system('cls')
                print('Fájl ürítés')
                fajl_urites()
            case '9':
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
