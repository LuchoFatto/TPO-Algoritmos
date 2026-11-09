import re
import base_datos
import os
import json
from time import sleep

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
    patron_direccion = re.compile(
        r"^[a-zA-Z0-9À-ÿñÑ.°]+(?:\s+[a-zA-Z0-9À-ÿñÑ.°]+)*\s+\d+\s*[a-zA-Z]?$",
        re.IGNORECASE,
    )
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
def limpiar_nro(nro):
    nro = str(nro)
    return int(re.sub(r"[\.\-\s]", "", nro))


def abrir_archivo(ruta):
    """Verifica y abre el archivo json, devuelve su contenido

    Args:
        ruta (str): ruta de donde se encuentra el archivo

    Returns:
        _type_: Contenido del archivo, generalmente lista de diccionarios
    """
    try:
        with open(ruta, "r") as Archivo:
            return json.load(Archivo)
    except Exception as a:
        print(f'Error "{a}" al abrir el archivo, reiniciar y verificar su integridad')
        sleep(0.3)
        input("Presione Enter para Continuar")
        os.system("cls")
        exit


def cargar_archivo(datos, ruta):
    """Recive los datos a cargar, verifica y abre el archivo y lo carga dentro de el con indent=4

    Args:
        datos (_type_): Los datos a cargar dentro del json
        ruta (str): ruta de donde se encuentra el archivo
    """
    try:
        with open(ruta, "w", encoding="utf8") as Archivo:
            json.dump(datos, Archivo, indent=4)
    except Exception as a:
        print(f'Error "{a}" al abrir el archivo, reiniciar y verificar su integridad')
        sleep(0.3)
        input("Presione Enter para Continuar")
        os.system("cls")
        exit
