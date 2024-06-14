# adatbekérés
bekertSzam = int(input("Adj meg egy egész számot: "))

# 0,1 esek kiírása egy sorba
jel = 1
for _ in range(bekertSzam):
    print(jel, end="")
    jel = 0 if jel == 1 else 1   # ternary kifejezés
    # if jel == 1:
    #     jel = 0
    # else:
    #     jel = 1
print()

# 1 -> 1
# 3 -> 101
# 4 -> 1010