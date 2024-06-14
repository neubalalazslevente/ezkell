szam1 = int(input("Add meg az első számot! "))
szam2 = int(input("Add meg a második számot! "))

if szam1 % szam2 == 0:
    print("Az első szám osztható a második számmal.")
elif szam2 % szam1 == 0:
    print("A második szám osztható az első számmal.")
elif szam1 == szam2:
    print("Az első szám egyenlő a másodikkal, és oszthatók egymással.")
else:
    print("A számok nem oszthatók egymással.")