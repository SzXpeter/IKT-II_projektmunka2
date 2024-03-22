# Leltározó program

### Classes.py

- Polc
    - Felépítése:
        - Raktár
        - Polc
        - Terméknév
        - Darabszám
- Eladás
    - Felépítése:
        - Név
        - Raktár
        - Eladás száma
- Rendelés
    - Felépítése:
        - Név
        - Darabszám

### Functions.py

- Beolvasás
    - Beolvassa a fájlok tartalmait, hogy az újra megnyitott alkalmazást feltöltsük az eddigi adatokkal
- Mentés
    - Menti az adatokat fájlba, hogy később is újra tudjuk használni az adatokat
- Új termék hozzáadás
    - Új termék hozzáadása polchoz, ezzel kirendel egy polcot az azonos termékeknek, ahol raktározva lesznek
    - *Bekért adatok:*
        - Terméknév
        - Darabszám
- Eladás
    - Termékek eladása
    - *Bekért adatok:*
        - Név
        - Eladandó darabszám
- Termék törlés
    - Termék törlése és a polc felszabadítása<br>
        - *A polc szabaddá vál és újra lehet terméket rendelni hozzá*
    - *Bekért adatok:*
        - Termék neve
- Termék/Polc keresése
    - Bekért polcra/terméknévre rákeress és kijeleníti a kapcsolodó adatokat
    - *Bekért adatok:*
        - Termék neve *vagy* raktár száma, polc száma
- Rendelés
    - Meglévő termékek *(van kijelölt polcuk)* rendelésének leadása
    - Rendelés teljesítése
    - *Bekért adatok:*
        - Rendelés leadása *vagy* a rendeléslista teljesítése
        - Rendelés leadáshoz bekért adatok:
            - Terméknév
            - Darabszám
- Fájlok alaphelyzetbe állítása
- Raktáron lévő termékek listázása

### Main.py

- Menü
    - Összes function behívása menüpontként
    - Számbekérés function -> számbekérés ellenőrzéssel
- Statisztika
    - Statisztika készítése az eladásokról (hány termék, honnan)