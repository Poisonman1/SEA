beregning = input("Indtast udregning: ").split(" ")

def calc():
    # Find the first * or /, otherwise the first + or -
    idx = next((i for i, t in enumerate(beregning) if t in ("*", "/","%")), None)
    if idx is None:
        idx = next(i for i, t in enumerate(beregning) if t in ("+", "-"))

    symbol = beregning[idx]
    tal = float(beregning[idx - 1])
    tal2 = float(beregning[idx + 1])

    if symbol == "*":
        total = tal * tal2
    elif symbol == "/":
        total = tal / tal2
    elif symbol == "%":
            total = tal % tal2
    elif symbol == "+":
        total = tal + tal2
    else:
        total = tal - tal2

    beregning[idx - 1:idx + 2] = [total]

while len(beregning) > 1:
    calc()

print(float(beregning[0]))
