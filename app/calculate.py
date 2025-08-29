import math

def calcular_hipotenusa(cateto_a, cateto_b):
    
    if cateto_a <= 0 or cateto_b <= 0:
        raise ValueError("Los catetos deben ser números positivos")
    
    hipotenusa = math.sqrt(cateto_a**2 + cateto_b**2)
    return hipotenusa

def validar_entrada(valor):
    
    try:
        numero = float(valor)
        if numero <= 0:
            raise ValueError("El valor debe ser un número positivo")
        return numero
    except ValueError as e:
        
        if "El valor debe ser un número positivo" in str(e):
            raise e
        
        raise ValueError("Por favor ingrese un número válido")