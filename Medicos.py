import validaciones
import usuarios
import os
import json
import re
import auth
import turnos
import random

from colorama import Fore, Style, init
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)

consola = Console()


# Afiliados / médicos

def alta_medico():

    medico_nombre = validaciones.bucle_medico(Fore.YELLOW +
        "Ingrese su nombre: ",
        "SOLO LETRAS - Ingrese su nombre: ",
        validaciones.validador_solo_letras) #verifica solo letras sin limite de caracteres

    medico_apellido = validaciones.bucle_medico(Fore.YELLOW +
        "Ingrese su apellido: ",
        "SOLO LETRAS - Ingrese su apellido: ",
        validaciones.validador_solo_letras)

    medico_cuit = validar_cuit_medicos()

    medico_matricula = validaciones.bucle_medico(
        "Ingrese su NRO de matricula: ",
        "SOLO NUMEROS SIN GUIONES - Ingrese su NRO de matricula: ",
        validaciones.validador_solo_numeros
    )

    medico_email = validaciones.bucle_medico(
        "Ingrese su email: ",
        "ERROR - Ingrese su email correctamente: ",
        validaciones.validar_email
    )

    medico_contraseña = validaciones.bucle_medico(
        "Contraseña: ",
        "ERROR: ingrese una contraseña de solo numero: ",
        validaciones.validador_solo_numeros
    )

    medico_especialidad = validaciones.bucle_medico(
    "Seleccione su especialidad (Cardiologia, Dermatologia, Pediatria o Traumatologia): ",
    "ERROR: seleccione una especialidad válida (Cardiología, Dermatología, Pediatría o Traumatología): ",
    validaciones.validador_especialidad
    )

    medico = {
        "nombre":medico_nombre,
        "apellido":medico_apellido,
        "CUIT":medico_cuit,
        "email":medico_email,
        "matricula":medico_matricula,
        "contraseña":medico_contraseña,
        "estado_socio": 1,
        "especialidad": medico_especialidad
        }

    turnos.agregarMedicoTurnos(medico["CUIT"])
    return(medico)


def generarArchivo(medico, ruta_archivo):
    print("""Agregar un médico al archivo JSON""")

    try:
        # Intentar leer los médicos existentes
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                medicos = json.load(archivo)

        except FileNotFoundError:
            medicos = []

        # Agregar el nuevo diccionario a la lista
        medicos.append(medico)

        # Guardar la lista actualizada
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(medicos, archivo, indent=4, ensure_ascii=False)

        print("Médico agregado con éxito")

    except Exception as e:
        print(e)        


def validar_cuit_medicos():
    """Ingreso, Validacion y verificacion de CUIT de Usuario

    Returns:
        int: CUIT Validado y no repetido ingresado por el Usuario
    """

    RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__),"medicos.json")
    Medicos = auth.abrir_archivo(RUTA_ARCHIVO)

    Flag = True
    while Flag:
        try:
            cuit = input('Ingrese el CUIT\n>> ')

            if not auth.validar_cuit(cuit):
                print('Ingrese correctamente el CUIT')
                input('Ingrese Enter para reintentar')
                print('\n\n')
            else:
                cuit = auth.limpiar_nro(cuit)

                for i in Medicos:
                    if i['CUIT'] == cuit:
                        print('El CUIT ingresado ya existe')
                        input('Ingrese Enter para reintentar')
                        cuit = None
                        break
                if cuit != None:
                    Flag = usuarios.verificar_decision(cuit)

        except Exception as e:
            print(type(e))
            print('Ocurrió un error. Intente nuevamente.')
    return cuit

def modificar_medico():

    cuit_medico_modificar = input("Para modificar sus datos ingrese su CUIT: ")

    if not auth.validar_cuit(cuit_medico_modificar):
        print("El CUIT ingresado no es válido")
        return

    cuit_medico_modificar = auth.limpiar_nro(cuit_medico_modificar)

    RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "medicos.json")
    medicos = auth.abrir_archivo(RUTA_ARCHIVO)

    for medico in medicos:
        if medico["CUIT"] == cuit_medico_modificar:
            opcion = input("¿Qué desea modificar? 1) Mail - 2) Contraseña: ")
            if opcion == "1":
                medico["email"] = validaciones.bucle_medico(
                    "Ingrese el nuevo email del médico/a: ",
                    "Ingrese su mail correctamente: ",
                    validaciones.validar_email)

            elif opcion == "2":
                medico["contraseña"] = validaciones.bucle_medico(
                    "Ingrese la nueva contraseña: ",
                    "ERROR: ingrese una contraseña de solo números: ",
                    validaciones.validador_solo_numeros)
            else:
                print("Opción incorrecta")
                return

            # Guardar los cambios en el JSON
            with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                json.dump(medicos, archivo, indent=4, ensure_ascii=False)

            print("Datos del médico modificados correctamente")
            return

    print("No se encontró ningún médico con ese CUIT")



def dar_baja_medico(cuit_medico=None):

    RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "medicos.json")
    medicos = auth.abrir_archivo(RUTA_ARCHIVO)

    if cuit_medico is None:
        cuit_medico_eliminar = input("Para darse de baja ingrese su NUMERO de CUIT: ")
    else:
        cuit_medico_eliminar = str(cuit_medico)

    if not auth.validar_cuit(cuit_medico_eliminar):
        print("El CUIT ingresado no es válido")
        return False

    cuit_medico_eliminar = auth.limpiar_nro(cuit_medico_eliminar)

    for medico in medicos:
        if medico["CUIT"] == cuit_medico_eliminar:
            confirmacion = input("Confirmacion, desea eliminar? SI/NO: ")
            if confirmacion.strip().upper() == "SI":
                medico["estado_socio"] = 0
                # Guardar los cambios en el JSON
                with open(RUTA_ARCHIVO, "w", encoding="utf-8") as archivo:
                    json.dump(medicos, archivo, indent=4, ensure_ascii=False)
                print("Médico dado de baja correctamente")
                return True
            else:
                print("Operación cancelada")
            return False

    print("No se encontró ningún médico con ese CUIT")
    return False


def imprimir_lista_medicos():

    RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__), "medicos.json")

    medicos = auth.abrir_archivo(RUTA_ARCHIVO)

    for medico in medicos:
        print("\nNombre: {0}".format(medico["nombre"]))
        print("Apellido: {0}".format(medico["apellido"]))
        print("CUIT: {0}".format(medico["CUIT"]))
        print("Email: {0}".format(medico["email"]))
        print("Matricula: {0}".format(medico["matricula"]))
        print("Estado del Socio: {0}".format(medico["estado_socio"]))
