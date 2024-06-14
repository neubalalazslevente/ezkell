# 0.feladat
class Alloviz:
    def __init__(self, args: list[str]) -> None:
        self.nev = args[0]
        self.tipus = args[1]
        self.terulet = float(args[2])
        self.vizgyujto = float(args[3])
    def __str__(self) -> str:
        return f"| {self.nev:90} | {self.tipus:15} | {self.terulet:7} | {self.vizgyujto:5} |"

class Program:
    def __init__(self) -> None:
        self.allovizek: list[Alloviz] = []
        # vezénylés
        self.importal()
        self.f1()
        self.f2()
        self.f3()
        self.f4()
        self.f5()

    def f5(self) -> None:
        # Igaz-e, hogy minden mesterséges tó vízgyűjtő területe legalább tízszerese a saját vízfelszínének
        # eldöntés
        ellentalalat = False
        for alloviz in self.allovizek:
            if alloviz.tipus == "mesterséges" and alloviz.vizgyujto / alloviz.terulet < 10:
                ellentalalat = True
                break
            
        print(f'{"Igaz" if not ellentalalat else "Hamis"}, hogy minden mesterséges tó vízgyűjtő területe legalább tízszerese a saját vízfelszínének')

    def f4(self) -> None:
        # kiválogatás, közvetlenül fájlba
        file = open("kozepes.txt", "w", encoding="UTF-8")
        for alloviz in self.allovizek:
            if 3 <= alloviz.terulet <= 10 and alloviz.vizgyujto / alloviz.terulet >= 10:
                file.write(f"{alloviz.nev};{alloviz.tipus}\n")
        
        print("A fájlba írás sikeres!")

    def f3(self) -> None:
        # I. holtversenyes verzió, ha több is van maximális, mind kiírjuk
        # 1. maximumérték kiválasztása
        # max_ertek = self.allovizek[0].vizgyujto
        # for alloviz in self.allovizek:
        #     if max_ertek < alloviz.vizgyujto:
        #         max_ertek = alloviz.vizgyujto

        # # 2. kiválogatás maximumérték szerint - konzolra (így nincs eredményobjektum!)
        # print('A legnagyobb vízgyűjtő területű állóvíz:')
        # for alloviz in self.allovizek:
        #     if max_ertek == alloviz.vizgyujto:
        #         print(f"{alloviz.nev}\n\tTípusa: {alloviz.tipus}\n\tVízfelszíne: {alloviz.terulet} km2\n\tVizgyűjtő területe {alloviz.vizgyujto} km2")

        # II. Nem holtversenyes verzió, ha több is van maximális, csak az elsőt irjuk ki
        # maximumértékű objektum referenciájának kiválasztása
        max_r = self.allovizek[0]
        for alloviz in self.allovizek:
            if max_r.vizgyujto < alloviz.vizgyujto:
                max_r = alloviz

        print(f"{max_r.nev}\n\tTípusa: {max_r.tipus}\n\tVízfelszíne: {max_r.terulet} km2\n\tVizgyűjtő területe {max_r.vizgyujto} km2")

        # Módosítás: csak a mesterséges tavak közül... Csak kereséssel!
        # 1. kiválogatás
        mestersegesTavak: list[Alloviz] = []
        for alloviz in self.allovizek:
            if alloviz.tipus == "mesterséges":
                mestersegesTavak.append(alloviz)

        # 2. maximumértékű objektum referenciájának kiválasztása
        if len(mestersegesTavak) > 0:
            max_r = mestersegesTavak[0]
            for alloviz in mestersegesTavak:
                if max_r.vizgyujto < alloviz.vizgyujto:
                    max_r = alloviz

            print(f"{max_r.nev}\n\tTípusa: {max_r.tipus}\n\tVízfelszíne: {max_r.terulet} km2\n\tVizgyűjtő területe {max_r.vizgyujto} km2")
        else:
            print('Nincs mesterséges tó a listában!')

        # Ugyanez, csak egyszerűbben
        #  maximumértékű objektum referenciájának megkeresése
        max_r = None
        for alloviz in self.allovizek:
            if alloviz.tipus == "mesterséges" and (max_r is None or max_r.vizgyujto < alloviz.vizgyujto):
                max_r = alloviz

        if max_r is not None:
            print(f"{max_r.nev}\n\tTípusa: {max_r.tipus}\n\tVízfelszíne: {max_r.terulet} km2\n\tVizgyűjtő területe {max_r.vizgyujto} km2")
        else:
            print('Nincs mesterséges tó a listában!')

    def f2(self) -> None:
        # összegzés
        osszeg = 0
        for alloviz in self.allovizek:
            osszeg += alloviz.terulet
        
        print(f"\n3.b feladat\nMagyarország {osszeg / 93036 * 100:.2f}%-át fedik le a tavak.")

    def f1(self) -> None:
        print(f"\n3.a feladat\n{len(self.allovizek)} tó adatait olvastuk be.")

    def importal(self) -> None:
        file = open("alloviz.txt", "r", encoding="UTF-8")
        file.readline()
        for line in file:
            args = line.strip().split("\t")
            self.allovizek.append(Alloviz(args))

        if input("\nAz importálás sikeres, kiírjam? (i): ") == "i": 
            for alloviz in self.allovizek:
                print(alloviz)

if __name__ == "__main__":
    Program()






# class Karakter(Program):
#     pass

# class Szorny(Karakter):
#     pass

# class Katona(Karakter):
#     pass


# p = Katona(3)

# class Valami:
#     pass

# v = Valami()

# v.nev = "Józsika"


# vv = Valami()

# vv.nev = "Gézuka"


# print(v.nev, vv.nev)
