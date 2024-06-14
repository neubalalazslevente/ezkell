class Robot:
    def __init__(self, args: list[str]) -> None:
        self.tanulo = args[0]
        self.kodok = args[1]
        self.helyes_e = True
    
    def __str__(self) -> str:
        return f"{self.tanulo:10} | {self.kodok}"

class Program:
    def __init__(self) -> None:
        self.adatok: list[Robot] = []
        self.adatok2: list[Robot] = []
        self.importal()
        self.f2()
        self.f3()
        self.f3a()
        self.f3b()
        self.f3c()

    def f3c(self) -> None:
        # megszámlálás eldöntéssel (melyik tanuló kódsorozatában NINCS hibás kód)
        szamlalo = 0   # hibátlan kódsorozatok száma
        for adat in self.adatok:
            # döntéshalasztás elve miatt idekombinálunk egy ELDÖNTÉS algoritmust
            # eldöntés (s) - állítás: adott 'adat' obj. kódsorozatában EGYIK kód SEM hibás
            ellentalalat = False
            for kod in adat.kodok:
                if kod != "E" and kod != "B" and kod != "J" and kod != "H":  # az állítást megdönteni akarjuk
                    ellentalalat = True
                    break
            # eldöntés (m) vége, kiértékelés
            if not ellentalalat:
                szamlalo += 1

        print(f"Hibátlan kódsorozatok száma: {szamlalo}")  

    def f3b(self) -> None:
        # megszámlálás eldöntéssel (melyik tanuló kódsorozata helyes MINDEN kód)
        szamlalo = 0   # hibátlan kódsorozatok száma
        for adat in self.adatok:
            # döntéshalasztás elve miatt idekombinálunk egy ELDÖNTÉS algoritmust
            # eldöntés (m) - állítás: adott 'adat' obj. kódsorozatának MINDEN kódja hibátlan
            ellentalalat = False
            for kod in adat.kodok:
                if kod != "E" and kod != "B" and kod != "J" and kod != "H":  # az állítást megdönteni akarjuk
                    ellentalalat = True
                    break
            # eldöntés (m) vége, kiértékelés
            if not ellentalalat:
                szamlalo += 1

        print(f"Hibátlan kódsorozatok száma: {szamlalo}")  

    def f3a(self) -> None:
        helyes_kodok = ('E', 'B', 'J', 'H')

        # megszámlálás eldöntéssel (melyik tanulónak van LEGALÁBB EGY hibás kódja)
        szamlalo = 0   # hibás kódsorozatok száma
        for adat in self.adatok:
            # döntéshalasztás elve miatt idekombinálunk egy ELDÖNTÉS algoritmust
            # eldöntés (l1) - állítás: adott 'adat' obj. kódsorozata tartalmaz LEGALÁBB EGY hibás kódot
            talalat = False
            for kod in adat.kodok:
                # eldöntés (s) - állítás: adott kód EGYIK helyes kódnak SEM felel meg
                ellentalalat = False
                for helyes_kod in helyes_kodok:
                    if kod == helyes_kod:  # az állítást megdönteni akarjuk
                        ellentalalat = True
                        break
                # eldöntés (s) vége, kiértékelés
                if not ellentalalat:       # az állítást igazolni akarjuk
                    talalat = True
                    break
            # eldöntés (l1) vége, kiértékelés
            if talalat:
                szamlalo += 1
                adat.helyes_e = False   # elég vagy ez...
            else:
                self.adatok2.append(adat)   # vagy ez.

        print(f"Hibás kódsorozatok száma: {szamlalo}")

    def f3(self) -> None:
        # megszámlálás eldöntéssel (melyik tanulónak van LEGALÁBB EGY hibás kódja)
        szamlalo = 0   # hibás kódsorozatok száma
        for adat in self.adatok:
            # döntéshalasztás elve miatt idekombinálunk egy ELDÖNTÉS algoritmust
            # eldöntés (l1) - állítás: adott 'adat' obj. kódsorozata tartalmaz LEGALÁBB EGY hibás kódot
            talalat = False
            for kod in adat.kodok:
                if kod != "E" and kod != "B" and kod != "J" and kod != "H":  # az állítást igazolni akarjuk
                    talalat = True
                    break
            # eldöntés (l1) vége, kiértékelés
            if talalat:
                szamlalo += 1

        print(f"Hibás kódsorozatok száma: {szamlalo}")
    
    def f2(self) -> None:
        print(f"Tanulók száma: {len(self.adatok)}")
    
    def importal(self) -> None:
        file = open("progs.txt")
        for line in file:
            args = line.strip().split(" ")
            self.adatok.append(Robot(args))
        if input("Kiírjam a beolvasott adatokat? (i) ") == "i":
            for adat in self.adatok:
                print(adat)

if __name__ == "__main__":
    Program()