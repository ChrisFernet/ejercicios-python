x = float(input("Ingrese x: "))
n = int(input("Ingrese n: "))

suma = 1
factorial = 1

for i in range(1, n + 1):
    factorial *= i   # calcula i!
    suma += (x ** i) / factorial

print("Aproximación de e^x:", suma)
