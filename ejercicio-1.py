capital = float(input("Ingrese el capital: "))

def interes(): 
    i = int(input("Ingrese el interés: "))
    return i/100

años = int(input("Ingrese el plazo a pagar en años: "))

while capital < 0:
        print("Monto invàlido.") 

print(f"El monto generado fue de: {capital*interes()*años:.0f}$")        
        

