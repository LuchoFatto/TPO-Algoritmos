import validaciones
import os
import auth

from colorama import Fore, Style, init
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)

consola = Console()

RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "farmacias.json")

RUTA_USUARIOS = os.path.join(os.path.dirname(__file__), "lista_usuarios.json")


def leer_farmacias():
    """Lee y devuelve la lista de farmacias guardada en el archivo JSON."""
    return auth.abrir_archivo(RUTA_ARCHIVO)


def leer_usuarios():
    """Lee y devuelve la lista de afiliados guardada en el archivo JSON."""
    return auth.abrir_archivo(RUTA_USUARIOS)


def guardar_farmacias(farmacias):
    """Guarda la lista de farmacias en el archivo JSON."""
    auth.cargar_archivo(farmacias, RUTA_ARCHIVO)


def buscar_farmacia_por_cuit(farmacias, cuit):
    """Busca una farmacia por CUIT y devuelve sus datos si existe."""
    try:
        cuit_limpio = auth.limpiar_nro(cuit)

        for farmacia in farmacias:
            if farmacia["CUIT"] == cuit_limpio:
                return farmacia

    except (TypeError, ValueError) as error:
        print(f"No se pudo buscar la farmacia: {error}")

    return None


def consultar_estado_afiliado(usuarios, cuit):
    """Devuelve ACTIVO o INACTIVO según el estado del afiliado."""
    try:
        cuit_limpio = auth.limpiar_nro(cuit)

        for usuario in usuarios:
            if usuario["CUIT"] == cuit_limpio:
                if usuario["Activo"]:
                    return "ACTIVO"
                return "INACTIVO"

    except (TypeError, ValueError, KeyError) as error:
        print(f"No se pudo consultar el estado del afiliado: {error}")

    return None


def consultar_estado_afiliado_por_consola():
    """Solicita un CUIT y muestra el estado del afiliado por consola."""
    usuarios = leer_usuarios()

    cuit = input(Fore.YELLOW + "Ingrese el CUIT del afiliado (0 para volver): ")

    while cuit != "0" and not auth.validar_cuit(cuit):
        cuit = input(
            Fore.YELLOW + "Ingrese un CUIT válido de 11 dígitos (0 para volver): "
        )

    if cuit == "0":
        return None

    estado = consultar_estado_afiliado(usuarios, cuit)

    if estado is None:
        print(Fore.YELLOW + "No se encontró un afiliado con ese CUIT.")
        return None

    print(Fore.GREEN + f"El afiliado se encuentra {estado}.")
    return estado


# Farmacias
def imprimir_lista_farmacias(farmacias):
    for farmacia in farmacias:
        if farmacia["estado_farmacia"] == 1:
            estado = "ACTIVA"
        else:
            estado = "INACTIVA"

        print(Fore.YELLOW + "\nNombre: {0}".format(farmacia["nombre"]))
        print(Fore.YELLOW + "CUIT: {0}".format(farmacia["CUIT"]))
        print(Fore.YELLOW + "Email: {0}".format(farmacia["email"]))
        print(Fore.YELLOW + "Direccion: {0}".format(farmacia["direccion"]))
        print(Fore.YELLOW + "Telefono: {0}".format(farmacia["telefono"]))
        print(Fore.YELLOW + "Estado de la farmacia: {0}".format(estado))


def cargar_farmacia(farmacias):
    """Solicita los datos de una farmacia y la guarda en el archivo JSON."""

    nombre = input(Fore.YELLOW + "Ingrese el nombre de la farmacia: ")
    while not auth.validacion_letras(nombre):
        nombre = input(
            Fore.YELLOW + "Ingrese un nombre compuesto solamente por letras: "
        )

    cuit = input(Fore.YELLOW + "Ingrese el CUIT de la farmacia: ")
    while not auth.validar_cuit(cuit):
        cuit = input(Fore.YELLOW + "Ingrese un CUIT válido de 11 dígitos: ")

    cuit = auth.limpiar_nro(cuit)
    while buscar_farmacia_por_cuit(farmacias, cuit) is not None:
        print(Fore.YELLOW + "El CUIT ingresado ya está registrado.")
        cuit = input(Fore.YELLOW + "Ingrese otro CUIT: ")
        while not auth.validar_cuit(cuit):
            cuit = input(Fore.YELLOW + "Ingrese un CUIT válido de 11 dígitos: ")
        cuit = auth.limpiar_nro(cuit)

    email = input(Fore.YELLOW + "Ingrese el email de la farmacia: ")
    while not auth.validar_email(email):
        email = input(Fore.YELLOW + "Ingrese un email válido: ")

    direccion = input(Fore.YELLOW + "Ingrese la dirección de la farmacia: ")
    while not auth.validar_direccion(direccion):
        direccion = input(
            Fore.YELLOW + "Ingrese una dirección válida, por ejemplo: Alvear 1234: "
        )

    telefono = input(Fore.YELLOW + "Ingrese el teléfono de la farmacia: ")
    while not auth.validar_numero_telefono(telefono):
        telefono = input(
            Fore.YELLOW + "Ingrese un teléfono válido, por ejemplo: 1122334455: "
        )
    telefono = auth.limpiar_nro(telefono)

    contraseña = input(Fore.YELLOW + "Ingrese la contraseña de la farmacia: ")
    while not auth.validar_contrasenia(contraseña):
        contraseña = input(
            Fore.YELLOW
            + "La contraseña debe tener 8 caracteres, una mayúscula, un número y un símbolo: "
        )

    farmacia_nueva = {
        "nombre": nombre,
        "CUIT": cuit,
        "email": email,
        "direccion": direccion,
        "telefono": telefono,
        "contraseña": contraseña,
        "estado_farmacia": 1,
    }

    print(Fore.YELLOW + "\nDatos de la nueva farmacia:")
    imprimir_lista_farmacias([farmacia_nueva])

    confirmacion = (
        input(Fore.YELLOW + "\n¿Desea guardar esta farmacia? Ingrese SI o NO: ")
        .strip()
        .upper()
    )

    while confirmacion not in ("SI", "NO"):
        print(Fore.YELLOW + "Respuesta inválida. Ingrese únicamente SI o NO.")
        confirmacion = (
            input(Fore.YELLOW + "¿Desea guardar esta farmacia? Ingrese SI o NO: ")
            .strip()
            .upper()
        )

    if confirmacion == "SI":
        farmacias.append(farmacia_nueva)
        guardar_farmacias(farmacias)
        print(Fore.GREEN + "Farmacia guardada correctamente.")
        return farmacia_nueva

    print(Fore.YELLOW + "Carga de farmacia cancelada.")
    return None


def dar_de_baja_farmacia(farmacia, farmacias, mensaje_confirmacion):
    """Realiza la baja lógica de una farmacia y guarda el cambio."""
    if farmacia["estado_farmacia"] == 0:
        print(Fore.YELLOW + "La farmacia ya se encuentra inactiva.")
        return False

    print(Fore.YELLOW + "\nFarmacia seleccionada:")
    imprimir_lista_farmacias([farmacia])

    confirmacion = (
        input(Fore.YELLOW + f"\n{mensaje_confirmacion} Ingrese SI o NO: ")
        .strip()
        .upper()
    )

    while confirmacion not in ("SI", "NO"):
        print(Fore.YELLOW + "Respuesta inválida. Ingrese únicamente SI o NO.")
        confirmacion = (
            input(Fore.YELLOW + f"{mensaje_confirmacion} Ingrese SI o NO: ")
            .strip()
            .upper()
        )

    if confirmacion == "SI":
        farmacia["estado_farmacia"] = 0
        guardar_farmacias(farmacias)
        print(Fore.GREEN + "Farmacia dada de baja correctamente.")
        return True

    print(Fore.YELLOW + "Baja de farmacia cancelada.")
    return False


def dar_de_baja_farmacia_por_cuit(farmacias):
    """Permite al administrador dar de baja una farmacia por CUIT."""
    cuit = input(
        Fore.YELLOW
        + "Ingrese el CUIT de la farmacia que desea dar de baja (0 para salir): "
    )

    while cuit != "0" and not auth.validar_cuit(cuit):
        cuit = input(
            Fore.YELLOW + "Ingrese un CUIT válido de 11 dígitos (0 para salir): "
        )

    if cuit == "0":
        return False

    cuit = auth.limpiar_nro(cuit)
    farmacia = buscar_farmacia_por_cuit(farmacias, cuit)

    if farmacia is None:
        print(Fore.YELLOW + "No se encontró una farmacia con ese CUIT.")
        return False

    return dar_de_baja_farmacia(farmacia, farmacias, "¿Confirma la baja?")


def darse_de_baja(farmacia_actual):
    """Permite que una farmacia activa solicite su propia baja lógica."""
    farmacias = leer_farmacias()
    farmacia = buscar_farmacia_por_cuit(farmacias, farmacia_actual["CUIT"])

    if farmacia is None:
        print(Fore.YELLOW + "No se encontró la farmacia en el archivo.")
        return False

    return dar_de_baja_farmacia(farmacia, farmacias, "¿Confirma su baja?")
