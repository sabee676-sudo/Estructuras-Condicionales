
an = int(input("Introduce un año: "))

if (an % 4 == 0 and an % 100 != 0) and(an % 400 == 0):
    print(f"El año",an" es bisiesto.")
else:
    print(f"El año",an "no es bisiesto.")
