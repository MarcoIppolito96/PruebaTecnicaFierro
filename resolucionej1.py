# Ejercicio 1

def EsHappy(numero: int) -> bool:
    """Funcion que verifica si un numero es un Happy Number o no"""
    
    historial = set()

    while numero != 1 and numero not in historial:
        historial.add(numero)

        suma_cuadrados = 0
        for digito in str(numero):
            suma_cuadrados += int(digito) ** 2

        numero = suma_cuadrados

    return numero == 1

def Happynumbers()-> list:
    """La funcion devuelve los primeros 'x' Happy Numbers que se quieran saber"""

    happy = set()
    nro = int(input("Los primeros cuántos Happy Numbers quiere ver? "))#8
    
    i = 1
    while len(happy) < nro:
        if EsHappy(i): #Cambiar aca si se quiere usar la funcion parametrizada. En ese caso es EsHappyParametrizada(i)
            happy.add(i)
        i += 1
    happy_ord = sorted(list(happy))
    return print(f"Los primeros {nro} Happy Numbers son: {happy_ord}")

Happynumbers()

# 1.A)
def EsHappyParametrizada(numero: int, nroALlegar: any, potencia: any) -> bool:
    """Funcion que verifica si un numero es un Happy Number o no, PARAMETRIZADA"""

    historial = set()

    while numero != nroALlegar and numero not in historial:
        historial.add(numero)

        suma_cuadrados = 0
        for digito in str(numero):
            suma_cuadrados += int(digito) ** potencia

        numero = suma_cuadrados

    return numero == nroALlegar
