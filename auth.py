import re
import base_datos

from colorama import Fore, Style, init
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)

consola = Console()

# ==========================================
# FUNCIONES DE VALIDACIÓN (EXPRESIONES REGULARES)
# ==========================================

def validar_email(email):
    """Validar formato de email.

    Args:
        email (string): Email ingresado por el usuaio.

    Returns:
        boolean: Si el email cumple con el formato establecido.
    """

    patron_email = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    return bool(re.match(patron_email, email))


def validar_cuit(cuit):
    """Validar formato de CUIT Argentino.

    Args:
        cuit (string): CUIT ingresado por usuario.

    Returns:
        boolean: Si el CUIT cumple con el formato establecido y no contenga letras.
    """

    patron_limpiar = re.compile(r"[\.\-\s]")

    cuit_limpio = re.sub(patron_limpiar, "", cuit)

    return len(cuit_limpio) == 11 and cuit_limpio.isdigit()

def obtener_cuit_limpio(cuit):
    """Retorna el CUIT únicamente como números enteros.

    Args:
        cuit (string): CUIT ingresado por el usuario

    Returns:
        integer: Devuelve el CUIT como numero
    """
    return int(re.sub(r"[\.\-\s]", "", cuit))


def validar_numero_telefono(num_telefono):
    """Validar formato de numero de telefono Argentino.

    Args:
        num_telefono (string): Numero de telefono ingresado por el usuario.

    Returns:
        boolean: Si el numero de telefono cumple con el formato establecido.
    """

    patron_no_digito = re.compile(r"\D")
    patron_cantidad_numeros = re.compile(r"^11[0-9]{8}$")

    num_limpio = re.sub(patron_no_digito, "", num_telefono)

    return bool(re.match(patron_cantidad_numeros, num_limpio))


def validar_contrasenia(contrasenia):
    """Validar formato de contrasenia de telefono Argentino.

    Args:
        contrasenia (string): Contrasenia ingresada por el usuario.

    Returns:
        boolean: Si la contrasenia cumple con el formato establecido (Mínimo 8 caracteres, al menos 1 Mayúscula, 1 Número y 1 Símbolo).
    """

    patron_contrasenia = re.compile(r"^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$")

    return bool(re.match(patron_contrasenia, contrasenia))


def validacion_letras(texto):
    """Verificar que un texto contenga letras del abecedario, tildes y eñes.

    Args:
        texto (string): Texto ingresado por el usuario.

    Returns:
        boolean: Validar que el texto ingresado no contenga numeros o caracteres especiales.
    """

    patron_letras = re.compile(r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$")

    return bool(re.match(patron_letras, texto))


def validar_direccion(direccion):
    """Validar dirección con nombre de calle y altura numérica.

    Args:
        direccion (string): Direccion ingresada por el usuario.

    Returns:
        boolean: Validar que el texto ingresado contenga la informacion de la direccion
    """
    patron_direccion = re.compile(r"^[a-zA-Z0-9À-ÿñÑ.°]+(?:\s+[a-zA-Z0-9À-ÿñÑ.°]+)*\s+\d+\s*[a-zA-Z]?$", re.IGNORECASE)
    return bool(re.match(patron_direccion, direccion))


# ==========================================
# UTILIDADES DE ENTRADA DE DATOS
# ==========================================

def solicitar_dato_validado(mensaje, mensaje_error, funcion_validadora):
    """Solicita un dato por consola y lo reitera hasta que cumpla con la función validadora.

    Args:
        mensaje (string): Mensaje del input.
        mensaje_error (string): Mensaje de error.
        funcion_validadora (def): Validacion a aplicar en el input.

    Returns:
        string: Dato ingresado por el usuario validado.
    """
    dato = input(mensaje)
    while not funcion_validadora(dato):
        dato = input(mensaje_error)
    return dato

# Revisar funciones de inicio de sesion de por que estan puestas aca
# usuario no es afiliado
                #_usuario  agregar
def iniciar_sesion(lista_usuarios):

    print()
    print("===================================")
    consola.print(Panel("   INICIAR SESION AFILIADO", border_style= "green", width=44))
    print("===================================")

    cuit = input(Fore.YELLOW + "Ingrese su CUIT: ")

    # Validamos el formato
    if not validar_cuit(cuit):
        print(Fore.YELLOW + "CUIT invalido")
        return None

    # Sacamos puntos, guiones y espacios
    cuit_limpio = re.sub(r"[.\-\s]", "", cuit)
    cuit_limpio = int(cuit_limpio)

    usuario_encontrado = None

    # Busqueda secuencial
    for usuario in lista_usuarios:
        if usuario["CUIT"] == cuit_limpio:
            usuario_encontrado = usuario
            break

    if usuario_encontrado == None:
        print(Fore.YELLOW + "Usuario no encontrado")
        return None

    intentos = 3

    while intentos > 0:

        password = input(Fore.YELLOW + "Ingrese su contraseña: ")

        if password == usuario_encontrado["Password"]:

            if usuario_encontrado["Deudor"] == True:
                print(Fore.YELLOW + "No puede iniciar sesion porque posee una deuda.")
                print(Fore.YELLOW + "Debe regularizar su situacion.")
                return None

            print(Fore.YELLOW + "Inicio de sesion exitoso")
            print(Fore.YELLOW + "Bienvenido/a", usuario_encontrado["Nombre"])

            return usuario_encontrado

        else:
            intentos -= 1
            print(Fore.YELLOW + "Contraseña incorrecta")
            print(Fore.YELLOW + "Intentos restantes:", intentos)

    print(Fore.YELLOW + "Se agotaron los intentos")
    return None


def iniciar_sesion_medicos(Medicos):

    print()
    print("===================================")
    consola.print(Panel("   INICIAR SESION MEDICOS", border_style= "green", width=44))
    print("===================================")

    cuit = input(Fore.YELLOW + "Ingrese su CUIT: ")
    
        # Validamos el formato
    if not validar_cuit(cuit):
        print(Fore.YELLOW + "CUIT invalido")
        return None
    
        # Sacamos puntos, guiones y espacios
    cuit_limpio = re.sub(r"[.\-\s]", "", cuit)
    cuit_limpio = int(cuit_limpio)
    
    medico_encontrado = None
    
        # Busqueda secuencial
    for medico in Medicos:
        if medico["cuit"] == cuit_limpio:
            medico_encontrado = medico
            break
    
    if medico_encontrado == None:
        print(Fore.YELLOW + "Medico no encontrado")
        return None

    intentos = 3

    while intentos > 0:

        contraseña = input(Fore.YELLOW + "Ingrese su contraseña: ")

        if contraseña == medico_encontrado["contraseña"]:

            print(Fore.YELLOW + "Inicio de sesion exitoso")
            print(Fore.YELLOW + "Bienvenido/a", medico_encontrado["nombre"])

            return medico_encontrado

        else:
            intentos -= 1
            print(Fore.YELLOW + "Contraseña incorrecta")
            print(Fore.YELLOW + "Intentos restantes:", intentos)

    print(Fore.YELLOW + "Se agotaron los intentos")
    return None

def iniciar_sesion_farmacia(Farmacias):

    print()
    print("===================================")
    consola.print(Panel("   INICIAR SESION FARMACIA", border_style= "green", width=44))
    print("===================================")

    cuit = input(Fore.YELLOW + "Ingrese su CUIT: ")
    
        # Validamos el formato
    if not validar_cuit(cuit):
        print(Fore.YELLOW + "CUIT invalido")
        return None
    
        # Sacamos puntos, guiones y espacios
    cuit_limpio = re.sub(r"[.\-\s]", "", cuit)
    cuit_limpio = int(cuit_limpio)
    
    farmacia_encontrado = None
    
        # Busqueda secuencial
    for farmacia in Farmacias:
        if farmacia["cuit"] == cuit_limpio:
            farmacia_encontrado = farmacia
            break
    
    if farmacia_encontrado == None:
        print(Fore.YELLOW + "Farmacia no encontrado")
        return None

    intentos = 3

    while intentos > 0:

        contraseña = input(Fore.YELLOW + "Ingrese su contraseña: ")

        if contraseña == farmacia_encontrado["contraseña"]:

            print(Fore.YELLOW + "Inicio de sesion exitoso")
            print(Fore.YELLOW + "Bienvenido/a", farmacia_encontrado["nombre"])

            return farmacia_encontrado

        else:
            intentos -= 1
            print(Fore.YELLOW + "Contraseña incorrecta")
            print(Fore.YELLOW + "Intentos restantes:", intentos)

    print(Fore.YELLOW + "Se agotaron los intentos")
    return None




def iniciar_sesion_admin():

    print()
    print("===================================")
    consola.print(Panel("   INICIAR SESION", border_style= "green", width=44))
    print("===================================")

    user = input(Fore.YELLOW + "Ingrese su USER de ADMIN: ")


    if base_datos.Admin["Usuario"] == user:
        intentos = 3
        while intentos > 0:
            password = input(Fore.YELLOW + "Ingrese su contraseña: ")
            if base_datos.Admin["Contraseña"] == password:
                return True
            else:
                intentos -= 1
                print(Fore.YELLOW + "Contraseña incorrecta")
                print(Fore.YELLOW + "Intentos restantes:", intentos)
                print(Fore.YELLOW + "Se agotaron los intentos")
                return None
    else:
        print(Fore.YELLOW + "Usuario incorrecto")
        return False
