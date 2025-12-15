class OperadorInvalidoError(Exception):
    """Excepción personalizada para operador inválido"""
    pass

def realizar_operacion(expresion):
    try:
        partes = expresion.split()
        if len(partes) != 3:
            raise ValueError("Formato incorrecto. Usa: 'numero operador numero'")
        
        num1_str, operador, num2_str = partes
        
        # Validar números
        num1 = float(num1_str)
        num2 = float(num2_str)
        
        # Validar operador
        operadores_validos = {'+', '-', '*', '/'}
        if operador not in operadores_validos:
            raise OperadorInvalidoError(f"Operador '{operador}' no válido")
        
        # Realizar operación
        if operador == '+':
            resultado = num1 + num2
        elif operador == '-':
            resultado = num1 - num2
        elif operador == '*':
            resultado = num1 * num2
        elif operador == '/':
            if num2 == 0:
                raise ZeroDivisionError("División entre cero")
            resultado = num1 / num2
        
        return f"Resultado: {resultado}"
        
    except ZeroDivisionError as e:
        return f"Error: {e}"
    except ValueError as e:
        return f"Error: Valor numérico inválido - {e}"
    except OperadorInvalidoError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error inesperado: {e}"

# Pruebas
if __name__ == "__main__":
    pruebas = [
        "10 / 2",
        "5 * 3",
        "8 + 4",
        "10 - 7",
        "10 / 0",
        "abc + 2",
        "5 ^ 3",
        "10 + 2 + 3",
    ]
    
    for prueba in pruebas:
        print(f"\nExpresión: {prueba}")
        print(realizar_operacion(prueba))