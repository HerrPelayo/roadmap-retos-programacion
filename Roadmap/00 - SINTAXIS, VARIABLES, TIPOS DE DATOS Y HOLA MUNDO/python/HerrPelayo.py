""" EJERCICIO:
 * - Crea un comentario en el código y coloca la URL del sitio web oficial del
 *   lenguaje de programación que has seleccionado.
 * - Representa las diferentes sintaxis que existen de crear comentarios
 *   en el lenguaje (en una línea, varias...).
 * - Crea una variable (y una constante si el lenguaje lo soporta).
 * - Crea variables representando todos los tipos de datos primitivos
 *   del lenguaje (cadenas de texto, enteros, booleanos...).
 * - Imprime por terminal el texto: "¡Hola, [y el nombre de tu lenguaje]!
 """

# https://python.org

# Comentario en una línea

""" Esto es un 
comentario
en varias
líneas """

''' Que también
puede realizarse
con comillas simples '''

MI_CONSTANTE = "Mi constante"  # Python no tiene constantes.

mi_cadena_string = "HerrPelayo"     # Estoy creando una variable de tipo string
mi_numero_entero = 10               # Estoy creando e inicializando otra variable de tipo entero.
mi_numero_flotante = 10.5   # Estamos creando otra variable de tipo float, es decir, un número con decimales.
mi_booleano = True          # Booleano inicializado a True
mi_boobleano_2 = False      # Booleano inicializado a False

mi_lista = []  # También puedo crear una lista vacía, aunque esto lo veremos en otros ejercicios.

mi_lenguaje = "Python"

# Imprimo Hola y lo que tenga en mi variable, mi_lenguaje.
print(f'Hola {mi_lenguaje}')
