num1=float(input("Introducir primer numero: "))
num2=float(input("Introducir segundo numero: "))
num3=float(input("Introducir tercer numero:"))

if num1 >= num2 and num1 >= num3:
    mayor = num1

elif num2 >= num1 and num2 >= num3:
    mayor = num2

else:
    mayor=num3

if num1 <= num2 and num1 <= num3:
    menor = num1

elif num2 <= num1 and num2 <= num3:
    menor = num2

else:
    menor = num3

print("El numero mayor es:", mayor)
print("El numero menor es:",menor)