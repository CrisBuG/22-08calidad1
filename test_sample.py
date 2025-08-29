

import unittest
import math
from app.calculate import calcular_hipotenusa, validar_entrada


class TestCalcularHipotenusa(unittest.TestCase):
    

    def test_triangulo_3_4_5(self):
        
        resultado = calcular_hipotenusa(3, 4)
        self.assertEqual(resultado, 5.0)

    def test_triangulo_5_12_13(self):
        
        resultado = calcular_hipotenusa(5, 12)
        self.assertEqual(resultado, 13.0)

    def test_triangulo_8_15_17(self):
        
        resultado = calcular_hipotenusa(8, 15)
        self.assertEqual(resultado, 17.0)

    def test_catetos_iguales(self):
        
        resultado = calcular_hipotenusa(1, 1)
        esperado = math.sqrt(2)
        self.assertAlmostEqual(resultado, esperado, places=10)

    def test_catetos_decimales(self):
        
        resultado = calcular_hipotenusa(1.5, 2.0)
        esperado = math.sqrt(1.5**2 + 2.0**2)
        self.assertAlmostEqual(resultado, esperado, places=10)

    def test_catetos_grandes(self):
        
        resultado = calcular_hipotenusa(100, 200)
        esperado = math.sqrt(100**2 + 200**2)
        self.assertAlmostEqual(resultado, esperado, places=10)

    def test_catetos_pequenos(self):
        
        resultado = calcular_hipotenusa(0.001, 0.002)
        esperado = math.sqrt(0.001**2 + 0.002**2)
        self.assertAlmostEqual(resultado, esperado, places=10)

    def test_cateto_a_cero(self):
    
        with self.assertRaises(ValueError) as context:
            calcular_hipotenusa(0, 5)
        self.assertIn("Los catetos deben ser números positivos", str(context.exception))

    def test_cateto_b_cero(self):
        
        with self.assertRaises(ValueError) as context:
            calcular_hipotenusa(5, 0)
        self.assertIn("Los catetos deben ser números positivos", str(context.exception))

    def test_cateto_a_negativo(self):
        
        with self.assertRaises(ValueError) as context:
            calcular_hipotenusa(-3, 4)
        self.assertIn("Los catetos deben ser números positivos", str(context.exception))

    def test_cateto_b_negativo(self):
        
        with self.assertRaises(ValueError) as context:
            calcular_hipotenusa(3, -4)
        self.assertIn("Los catetos deben ser números positivos", str(context.exception))

    def test_ambos_catetos_negativos(self):
        
        with self.assertRaises(ValueError) as context:
            calcular_hipotenusa(-3, -4)
        self.assertIn("Los catetos deben ser números positivos", str(context.exception))


class TestValidarEntrada(unittest.TestCase):
   

    def test_numero_entero_positivo(self):
       
        resultado = validar_entrada("5")
        self.assertEqual(resultado, 5.0)

    def test_numero_decimal_positivo(self):
        
        resultado = validar_entrada("3.14")
        self.assertEqual(resultado, 3.14)

    def test_numero_con_espacios(self):
        
        resultado = validar_entrada(" 2.5 ")
        self.assertEqual(resultado, 2.5)

    def test_numero_cero(self):
    
        with self.assertRaises(ValueError) as context:
            validar_entrada("0")
        self.assertIn("El valor debe ser un número positivo", str(context.exception))

    def test_numero_negativo(self):
        
        with self.assertRaises(ValueError) as context:
            validar_entrada("-5")
        self.assertIn("El valor debe ser un número positivo", str(context.exception))

    def test_texto_no_numerico(self):
        
        with self.assertRaises(ValueError) as context:
            validar_entrada("abc")
        self.assertIn("Por favor ingrese un número válido", str(context.exception))

    def test_cadena_vacia(self):
        
        with self.assertRaises(ValueError) as context:
            validar_entrada("")
        self.assertIn("Por favor ingrese un número válido", str(context.exception))

    def test_solo_espacios(self):
        
        with self.assertRaises(ValueError) as context:
            validar_entrada("   ")
        self.assertIn("Por favor ingrese un número válido", str(context.exception))

    def test_numero_muy_pequeno(self):
        
        resultado = validar_entrada("0.0001")
        self.assertEqual(resultado, 0.0001)

    def test_numero_muy_grande(self):
       
        resultado = validar_entrada("999999.999")
        self.assertEqual(resultado, 999999.999)


class TestIntegracion(unittest.TestCase):
    

    def test_flujo_completo_valido(self):
        
        cateto_a = validar_entrada("3")
        cateto_b = validar_entrada("4")
        hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
        self.assertEqual(hipotenusa, 5.0)

    def test_flujo_completo_decimales(self):
        
        cateto_a = validar_entrada("1.5")
        cateto_b = validar_entrada("2.0")
        hipotenusa = calcular_hipotenusa(cateto_a, cateto_b)
        esperado = math.sqrt(1.5**2 + 2.0**2)
        self.assertAlmostEqual(hipotenusa, esperado, places=10)


if __name__ == '__main__':
    unittest.main(verbosity=2)