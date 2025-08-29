
from app.calculate import calcular_hipotenusa, validar_entrada

def mostrar_menu():
    
    print("\n" + "="*50)
    print("    CALCULADORA DE HIPOTENUSA")
    print("="*50)
    print("Calcula la hipotenusa usando el teorema de Pitágoras")
    print("Fórmula: c = √(a² + b²)")
    print("="*50)

def obtener_catetos():
    
    while True:
        try:
            print("\nIngrese los valores de los catetos:")
            cateto_a_str = input("Cateto A: ")
            cateto_a = validar_entrada(cateto_a_str)
            
            cateto_b_str = input("Cateto B: ")
            cateto_b = validar_entrada(cateto_b_str)
            
            return cateto_a, cateto_b
            
        except ValueError as e:
            print(f"\nError: {e}")
            print("Por favor, intente nuevamente.")

def mostrar_resultado(cateto_a, cateto_b, hipotenusa):
   
    print("\n" + "-"*40)
    print("RESULTADO:")
    print("-"*40)
    print(f"Cateto A: {cateto_a}")
    print(f"Cateto B: {cateto_b}")
    print(f"Hipotenusa: {hipotenusa:.4f}")
    print("-"*40)
    print(f"Verificación: {cateto_a}² + {cateto_b}² = {cateto_a**2} + {cateto_b**2} = {cateto_a**2 + cateto_b**2}")
    print(f"√{cateto_a**2 + cateto_b**2} = {hipotenusa:.4f}")
    print("-"*40)

def main():
   
    while True:
        try:
            mostrar_menu()
            
            cateto_a, cateto_b = obtener_catetos()
            
            hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
             
            mostrar_resultado(cateto_a, cateto_b, hipotenusa)
            
            continuar = input("\n¿Desea calcular otra hipotenusa? (s/n): ").lower().strip()
            if continuar not in ['s', 'si', 'sí', 'y', 'yes']:
                break
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrumpido por el usuario.")
            break
        except Exception as e:
            print(f"\nError inesperado: {e}")
            print("Por favor, intente nuevamente.")
    
   

if __name__ == "__main__":
    main()