from random import randint

telkek = int(input("Add meg a telkek számát! "))

def terulet(a: float, b: float) -> float:
    return a * b / 3.6

for i in range(telkek):
    x = randint(20, 100)
    y = randint(20, 100)
    terulet_r = terulet(x, y)
    print(f"{i+1}. telek: \n\toldalai: {x} és {y} m\n\tterülete: {terulet_r:.0f} négyszögöl" + ("" if terulet_r >= 1000 else "\n\tTúl kicsi a telek!"))