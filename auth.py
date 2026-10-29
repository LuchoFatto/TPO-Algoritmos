import re
import base_datos

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

def iniciar_sesion(lista_usuarios):

    print()
    print("===================================")
    print("          INICIAR SESION")
    print("===================================")

    cuit = input("Ingrese su CUIT: ")

    # Validamos el formato
    if not validar_cuit(cuit):
        print("CUIT invalido")
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
        print("Usuario no encontrado")
        return None

    intentos = 3

    while intentos > 0:

        password = input("Ingrese su contraseña: ")

        if password == usuario_encontrado["Password"]:

            if usuario_encontrado["Deudor"] == True:
                print("No puede iniciar sesion porque posee una deuda.")
                print("Debe regularizar su situacion.")
                return None

            print("Inicio de sesion exitoso")
            print("Bienvenido/a", usuario_encontrado["Nombre"])

            return usuario_encontrado

        else:
            intentos -= 1
            print("Contraseña incorrecta")
            print("Intentos restantes:", intentos)

    print("Se agotaron los intentos")
    return None


def iniciar_sesion_admin():

    print()
    print("===================================")
    print("          INICIAR SESION")
    print("===================================")

    user = input("Ingrese su USER de ADMIN: ")


    if base_datos.Admin["Usuario"] == user:
        intentos = 3
        while intentos > 0:
            password = input("Ingrese su contraseña: ")
            if base_datos.Admin["Contraseña"] == password:
                return True
            else:
                intentos -= 1
                print("Contraseña incorrecta")
                print("Intentos restantes:", intentos)
                print("Se agotaron los intentos")
                return None
    else:
        print("Usuario incorrecto")
        return False
