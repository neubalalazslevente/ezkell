# a = 10
# print(a)
# print(a.__str__())

# l = [1,2,3,4,5]
# print(l)
# print(l.__str__())
# print(len(l))
# print(l.__len__())
# print(sum(l))
# # print(l.__sum__())   ilyen nincs!

# class int:
#     def __init__(self, value) -> None:
#         self.value = value
        
#     def __str__(self) -> str:
#         return str(self.value)

class Adat(object):

    # osztályváltozó
    szamlalo = 0

    # osztálymetódus
    @staticmethod
    def darabszam() -> int:
        return Adat.szamlalo

    # konstruktor szerepet betöltő példánymetódus. Feladatai:
    # 1. felépíti (kivitelezi) a leendő objektumot
    # 2. definiálja az objektum leendő példány-referencia-változóit
    # 3. vezényleheti a saját példánymetódusait illetve az osztálymetódusokat (staticmethod)
    def __init__(self, tulajdonsagok: list[str]) -> None:
        self.evszam = int(tulajdonsagok[0])
        self.nyelv = tulajdonsagok[1]
        self.keresztnev = tulajdonsagok[2]
        self.vezeteknev = tulajdonsagok[3]
        self.elemszam = tulajdonsagok.__len__()
        Adat.szamlalo += 1
        self.sorszam = Adat.szamlalo

    @property
    def teljes_nev(self) -> str:
        return f'{self.vezeteknev} {self.keresztnev}'
    
    def __str__(self) -> str:
        return f'{self.sorszam:>02}.  {str(self.evszam):10} {self.nyelv:20} {self.keresztnev:20} {self.vezeteknev:10}'
    
    def __len__(self) -> int:
        return self.elemszam

# adat1 = Adat([1987, 'Perl', 'Larry', 'Wall'])
# print(adat1)
# print(len(adat1))

class Program:
    def __init__(self) -> None:
        self.adatok: list[Adat] = []
        # vezénylés
        self.f0()
        self.f1()
        self.f2()

    def f2(self) -> None:
        # A fájlban található programozási nyelvek közül melyik jelent meg elsőnek?
        print('\n2. feladat')


    def f1(self) -> None:
        # Hány darab programozási nyelv van eltárolva a fájlban?
        print('\n1. feladat')

        # KIVÁLOGATÁS ELDÖNTÉSSEL (s) - mindenből egyet
         
        # 1.a. halmazzal - generátor-kifejezéssel
        # nyelvek = set(adat.nyelv for adat in self.adatok) - generátor-kifejezéssel

        # print(len(nyelvek))

        # 1.a. halmazzal - másolással
        # nyelvek: set[str] = set()   # a halmaz adattípus ezt megcsinálja, mivel nem tárol ismétlődő elemeket
        # for adat in self.adatok:
        #     nyelvek.add(adat.nyelv)

        # print(len(nyelvek))

        # 2. listával - in operátorral
        # nyelvek: list[str] = []                 # 1. eredmény-objektum
        # for adat in self.adatok:                # 2. sorozat elemeinek bejárása
        #     if adat.nyelv not in nyelvek:       # 3. sorozatelem vizsgálata
        #         nyelvek.append(adat.nyelv)      # 4. eredmény-objektum alakítása

        # print(len(nyelvek))

        # 3. listával - hagyományosan
        nyelvek: list[str] = []
        for adat in self.adatok:
            # eldöntés (semelyikes) - állítás: adott adat programnyelve EGYIK 'nyelvek' lista elemmel SEM egyezik
            ellentalalat = False
            for nyelv in nyelvek:
                if adat.nyelv == nyelv:      # megdöntési kísérlet
                    ellentalalat = True
                    break
            # eldöntés (s) vége, kiértékelés
            if not ellentalalat:           # ha nem találtunk egyezést
                nyelvek.append(adat.nyelv)

        print(len(nyelvek))

    def f0(self) -> None:
        # Fájl beolvasása
        print('\n0. feladat')

        try:
            fajl = open('prognyelvek.txt')
            # első sor eldobása
            fajl.readline()
            # többi sor beolvasása
            for sor in fajl:
                if len(sor.strip()) > 0:
                    tulajdonsagok = sor.strip().split(';')
                    self.adatok.append(Adat(tulajdonsagok))

        except FileNotFoundError:
            print("A fájl nem található!")
            exit(123)
        except FileExistsError:
            print("A fájl nem megnyitható!")
            exit(124)
        
        # kiírási opció
        if input('Az importálás sikeres, kiírjam? (i): ')  == 'i':
            for adat in self.adatok:
                print(adat)

# Program objektum indítása
if __name__ == '__main__':
    Program()

# a = 10;
# print(a, id(a))

# a += 1
# print(a, id(a))


# lista = [1, 2.0, [], 'fsf']

# def hozzaad(lista: list[int]) -> list[int]:
#     lista.append(4);
#     return lista

# print(lista, id(lista))
# l = hozzaad(lista)
# print(l, id(l))

# szoveg = 'Hello'

# def bovit(szoveg: str) -> str:
#     szoveg += ' Balázs!'
#     return szoveg

# print(szoveg, id(szoveg))
# bovit(szoveg)
# sz = bovit(szoveg)
# print(sz, id(sz))