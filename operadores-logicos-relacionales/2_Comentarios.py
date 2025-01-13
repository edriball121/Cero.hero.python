# Este es un comentario de una sola línea

"""
Este es un comentario de múltiples líneas
o una cadena de documentación (docstring)
que puede ser utilizada para describir un módulo, clase o función.
"""

'''
Este es otro comentario de múltiples líneas
usando comillas simples.
'''

def ejemplo_funcion(param1, param2):
    """
    Esta es una cadena de documentación para la función `ejemplo_funcion`.

    Args:
        param1 (int): El primer parámetro.
        param2 (int): El segundo parámetro.

    Returns:
        int: La suma de los dos parámetros.
    """
    # Este es un comentario dentro de una función
    resultado = param1 + param2  # Este es un comentario al final de una línea de código
    return resultado

class EjemploClase:
    """
    Esta es una cadena de documentación para la clase `EjemploClase`.
    """

    def __init__(self, atributo):
        """
        Inicializa una nueva instancia de `EjemploClase`.

        Args:
            atributo (str): Un atributo de ejemplo.
        """
        self.atributo = atributo  # Comentario sobre el atributo

    def metodo_ejemplo(self):
        """
        Este es un método de ejemplo.

        Returns:
            str: Un mensaje de ejemplo.
        """
        # Comentario dentro de un método de clase
        return f"El atributo es: {self.atributo}"