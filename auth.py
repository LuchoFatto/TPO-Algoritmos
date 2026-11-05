import re
import base_datos
import os
import json
from time import sleep


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
        boolean: Si la contrasenia cumple con el formato establecido (Mayus, Min, Simbolo y Numero).
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

def limpiar_nro(nro):
    nro = str(nro)
    return int(re.sub(r'[\.\-\s]', "", nro))

def abrir_archivo(ruta):
    """Verifica y abre el archivo json, devuelve su contenido

    Args:
        ruta (str): ruta de donde se encuentra el archivo

    Returns:
        _type_: Contenido del archivo, generalmente lista de diccionarios
    """    
    try:
        with open(ruta,"r") as Archivo:
            return json.load(Archivo)
    except Exception as a:
        print(f'Error "{a}" al abrir el archivo, reiniciar y verificar su integridad')
        sleep(0.3)
        input("Presione Enter para Continuar")
        os.system('cls')
        exit

def cargar_archivo(datos, ruta):
    """Recive los datos a cargar, verifica y abre el archivo y lo carga dentro de el con indent=4

    Args:
        datos (_type_): Los datos a cargar dentro del json
        ruta (str): ruta de donde se encuentra el archivo
    """    
    try:
        with open(ruta,"w") as Archivo:
            json.dump(datos, Archivo, indent=4)
    except Exception as a:
        print(f'Error "{a}" al abrir el archivo, reiniciar y verificar su integridad')
        sleep(0.3)
        input("Presione Enter para Continuar")
        os.system('cls')
        exit





