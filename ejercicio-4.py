"""
4. Escribir un algoritmo que invierta los dígitos de un número positivo entero. Usar
operadores módulo y división para ir obteniendo los dígitos uno a uno. Por ejemplo, si
se ingresa 37368 debe retornar el numero 86373. (No se puede usar métodos de cadena,
solo usar operaciones matemáticas y ciclos).
"""

numero = int(input("Ingrese un número: "))

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)
