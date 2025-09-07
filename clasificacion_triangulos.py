print("========TIPOS DE TRIANGULOS======== ")

med1=float(input("Ingresala primera medida"))
med2=float(input("Ingresala segunda  medida"))
med3=float(input("Ingresala tercera medida"))

if med1 == med2 == med3:
    print("Triangulo Equilatero")

elif med1 == med3 or med1== med2 or med2==med3:
    print("Triangulo isoceles")

else:
    print("Escaleno")

