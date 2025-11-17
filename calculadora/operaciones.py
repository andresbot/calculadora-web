"""
Módulo que contiene las operaciones básicas de la calculadora.
"""

class Calculadora:
    @staticmethod
    def suma(a, b):
        """Realiza la suma de dos números."""
        try:
            return float(a) + float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def resta(a, b):
        """Realiza la resta de dos números."""
        try:
            return float(a) - float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def multiplicacion(a, b):
        """Realiza la multiplicación de dos números."""
        try:
            return float(a) * float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def division(a, b):
        """Realiza la división de dos números."""
        try:
            a_float = float(a)
            b_float = float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")
        
        if b_float == 0:
            raise ValueError("No se puede dividir entre cero")
        
        return a_float / b_float

    @staticmethod
    def potencia(a, b):
        """Calcula la potencia de a elevado a b."""
        try:
            return float(a) ** float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")

    @staticmethod
    def raiz_cuadrada(a):
        """Calcula la raíz cuadrada de un número."""
        try:
            a_float = float(a)
        except (ValueError, TypeError):
            raise ValueError("El operando debe ser un número válido")
        
        if a_float < 0:
            raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
        
        return a_float ** 0.5

    @staticmethod
    def porcentaje(a, b):
        """Calcula el porcentaje de a respecto a b."""
        try:
            a_float = float(a)
            b_float = float(b)
        except (ValueError, TypeError):
            raise ValueError("Los operandos deben ser números válidos")
        
        if b_float == 0:
            raise ValueError("El divisor no puede ser cero para calcular porcentaje")
        
        return (a_float / b_float) * 100

    @staticmethod
    def evaluar_expresion(expresion):
        """
        Evalúa una expresión matemática simple.
        Solo permite operaciones básicas y números.
        """
        if not expresion or expresion.strip() == '':
            raise ValueError("La expresión no puede estar vacía")
        
        expresion = expresion.strip()
        
        # Primero validar palabras prohibidas
        palabras_prohibidas = ['import', 'exec', 'eval', 'open', 'file', '__']
        for palabra in palabras_prohibidas:
            if palabra in expresion.lower():
                raise ValueError("Expresión no permitida")
    
        # Luego validar caracteres
        caracteres_permitidos = set('0123456789.+-*/() ')
        if not all(c in caracteres_permitidos for c in expresion):
            raise ValueError("La expresión contiene caracteres no permitidos")
    
        try:
            # Usar eval con precaución (en un entorno controlado)
            resultado = eval(expresion, {'__builtins__': None}, {})
            return float(resultado)
        except ZeroDivisionError:
            raise ValueError("División por cero no permitida")
        except:
            raise ValueError("Expresión matemática inválida")    
