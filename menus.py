import usuarios
import admin
import base_datos
import Medicos
import Farmacias
import auth
import time
import os

from colorama import Fore, Style, init
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)

consola = Console()


def mostrar_menu_principal():
    opcion = ""

    while opcion != "3":
        print()
        print("=" * 40)
        time.sleep(0.1)
        consola.print(Panel("   SISTEMA DE GESTION OBRA SOCIAL", border_style= "green", width=44))
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print(Fore.GREEN + "1. Iniciar sesion")
        time.sleep(0.1)
        print(Fore.GREEN + "2. Registrarse")
        time.sleep(0.1)
        print(Fore.RED + "3. Salir")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input(Fore.YELLOW + "Seleccione una opcion: ")

        if opcion == "1":
            print(Fore.YELLOW + "\nIniciando sesion...")
            time.sleep(1)
            os.system("cls")
            mostrar_menu_login()

        elif opcion == "2":
            print(Fore.YELLOW + "\nCargando registro...")
            time.sleep(1)
            os.system("cls")
            usuarios.alta_usuario()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")
            os.system("cls")

        elif opcion == "3":
            print(Fore.YELLOW + "\nSaliendo del sistema...")
            time.sleep(2)
            os.system("cls")
            print(Fore.YELLOW + "Hasta luego!")

        else:
            os.system("cls")
            print(Fore.YELLOW + "\nOpcion invalida...")
            time.sleep(1)


def mostrar_menu_login():
    opcion = ""

    while opcion != "5":
        print()
        print("=" * 40)
        time.sleep(0.1)
        consola.print(Panel("   INICIAR SESION", border_style= "green", width=44))
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print(Fore.GREEN + "1. Ingresa como afiliado")
        time.sleep(0.1)
        print(Fore.GREEN + "2. Ingresa como medico")
        time.sleep(0.1)
        print(Fore.GREEN + "3. Ingresa como farmacia")
        time.sleep(0.1)
        print(Fore.GREEN + "4. Ingresa como Admin / Gestion")
        time.sleep(0.1)
        print(Fore.RED + "5. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input(Fore.YELLOW + "Seleccione una opcion: ")

        if opcion == "1":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando inicio de sesion...")
            time.sleep(1)

            cuit = usuarios.iniciar_sesion_usuario()

            if cuit != None:
                os.system("cls")
                print(Fore.YELLOW + "\nIngresando al sistema...")
                time.sleep(1)
                mostrar_menu_afiliados(cuit)

        elif opcion == "2":
            os.system("cls")
            if auth.iniciar_sesion_medicos():
                os.system("cls")
                print(Fore.YELLOW + "\nAcceso autorizado...")
                time.sleep(1)
                mostrar_menu_medico()
            else:
                return

        elif opcion == "3":
            os.system("cls")
            print("\nFuncion deshabilitada")
            input("\nPresione ENTER para volver...")
            # mostrar_menu_farmacia()

        elif opcion == "4":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando acceso de administrador...")
            time.sleep(1)

            if admin.iniciar_sesion_admin():
                os.system("cls")
                print(Fore.YELLOW + "\nAcceso autorizado...")
                time.sleep(1)
                mostrar_menu_admin()
            else:
                return

        elif opcion == "5":
            os.system("cls")
            print(Fore.YELLOW + "\nVolviendo al menu principal...")
            time.sleep(1)

        else:
            os.system("cls")
            print(Fore.YELLOW + "\nOpcion invalida...")
            time.sleep(1)


def mostrar_menu_afiliados(cuit):
    opcion = ""

    while opcion != "6":
        print()
        print("=" * 40)
        time.sleep(0.1)
        consola.print(Panel("   MENU DE AFILIADOS", border_style= "green", width=44))
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print(Fore.GREEN + "1. Ver perfil.")
        time.sleep(0.1)
        print(Fore.GREEN + "2. Ver cobertura.")
        time.sleep(0.1)
        print(Fore.GREEN + "3. Seleccionar / Cambiar plan. DESHABILITADO")
        time.sleep(0.1)
        print(Fore.GREEN + "4. Turnos. DESHABILITADO")
        time.sleep(0.1)
        print(Fore.RED + "5. Darse de baja")
        time.sleep(0.1)
        print(Fore.RED + "6. Volver.")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input(Fore.YELLOW + "Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando perfil...")
            time.sleep(1)
            usuarios.ver_mi_perfil_user(cuit)  # Ingresar cuit de usuario loggeado
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando cobertura...")
            time.sleep(1)
            usuarios.ver_beneficios(cuit)
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "3":
            os.system("cls")
            print(Fore.YELLOW + "\nSeleccionar / Cambiar plan")
            print("Funcion deshabilitada")
            input("\nPresione ENTER para volver...")

        elif opcion == "4":
            os.system("cls")
            print(Fore.YELLOW + "\nVer mis turnos")
            input("\nPresione ENTER para volver...")

        elif opcion == "5":
            os.system("cls")
            print(Fore.YELLOW + "\nProcesando solicitud de baja...")
            time.sleep(1)
            usuarios.baja_usuario(cuit)
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "6":
            os.system("cls")
            print(Fore.YELLOW + "\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            print(Fore.YELLOW + "\nOpcion invalida")
            time.sleep(1)


def mostrar_menu_medico():
    opcion = ""

    while opcion != "5":
        print()
        print("=" * 40)
        time.sleep(0.1)
        consola.print(Panel("   MENU DE MEDICOS", border_style= "green", width=44))
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print(Fore.GREEN + "1. Darse de alta")
        time.sleep(0.1)
        print(Fore.RED + "2. Modificar Medico")
        time.sleep(0.1)
        print(Fore.GREEN + "3. Darse de baja")
        time.sleep(0.1)
        print("4. Imprimir lista de medicos")
        time.sleep(0.1)
        print(Fore.RED + "5. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input(Fore.YELLOW + "Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando alta de medico...")
            time.sleep(1)

            medico = Medicos.alta_medico()

            rutaDirectorio = os.path.dirname(__file__)
            rutaArchivo = os.path.join(rutaDirectorio,"medicos.json")
            Medicos.generarArchivo(medico, rutaArchivo)
            
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "2":
            # MODIFICAR DATOS MAIL Y CONTRASEÑA #
            os.system("cls")
            print("\nModificar Mail o Contraseña")
            Medicos.modificar_medico()
            input("\nPresione ENTER para volver...")

        elif opcion == "3":
            # DAR DE BAJA #
            os.system("cls")
            print(Fore.YELLOW + "\nCargando solicitud de baja...")
            time.sleep(1)
            Medicos.dar_baja_medico()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")  

        elif opcion == "4":
            os.system("cls")
            print("\nImprimir lista de medicos")
            time.sleep(1)
            Medicos.imprimir_lista_medicos()
            input("\nPresione ENTER para continuar...")

        elif opcion == "5":
            os.system("cls")
            print(Fore.YELLOW + "\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            os.system("cls")
            print(Fore.YELLOW + "\nOpcion invalida")
            time.sleep(1)


def mostrar_menu_farmacia():
    opcion = ""

    while opcion != "2":
        print()
        print("=" * 40)
        time.sleep(0.1)
        consola.print(Panel("   MENU DE FARMACIAS", border_style= "green", width=44))
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print(Fore.GREEN + "1. Consultar estado de afiliado")
        time.sleep(0.1)
        print(Fore.RED + "2. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input(Fore.YELLOW + "Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print(Fore.YELLOW + "\nConsultando estado de afiliado...")
            time.sleep(1)
            print(Fore.YELLOW + "Consulta de afiliado")
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print(Fore.YELLOW + "\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            os.system("cls")
            print(Fore.YELLOW + "\nOpcion invalida")
            time.sleep(1)


def mostrar_menu_admin():
    opcion = ""

    while opcion != "8":
        print()
        print("=" * 40)
        time.sleep(0.1)
        consola.print(Panel("   MENU DE GESTION / ADMIN", border_style= "green", width=44))
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print(Fore.GREEN + "1. Dar de alta usuario")
        time.sleep(0.1)
        print(Fore.GREEN + "2. Dar de baja usuario")
        time.sleep(0.1)
        print(Fore.GREEN + "3. Manejar usuarios deudores")
        time.sleep(0.1)
        print(Fore.BLUE + "4. Ver lista de afiliados")
        time.sleep(0.1)
        print(Fore.BLUE + "5. Ver lista de medicos")
        time.sleep(0.1)
        print(Fore.BLUE + "6. Ver lista de farmacias")
        time.sleep(0.1)
        print(Fore.BLUE + "7. Ver historial - DESHABILITADO")
        time.sleep(0.1)
        print(Fore.RED + "8. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input(Fore.YELLOW + "Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando alta de usuario...")
            time.sleep(1)
            usuarios.alta_usuario()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando baja de usuario...")
            time.sleep(1)
            admin.baja_usuario()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "3":
            os.system("cls")
            print(Fore.YELLOW + "\nConsultando usuarios deudores...")
            time.sleep(1)
            admin.deudores()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "4":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando lista de afiliados...")
            time.sleep(1)
            usuarios.ver_lista_usuarios()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "5":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando lista de medicos...")
            time.sleep(1)
            Medicos.imprimir_lista_medicos()
            input(Fore.YELLOW + "\nPresione ENTER para continuar...")

        elif opcion == "6":
            os.system("cls")
            print(Fore.YELLOW + "\nCargando lista de farmacias...")
            time.sleep(1)
            Farmacias.imprimir_lista_farmacias(base_datos.Farmacias) #retirar base datos y poner 
            input(Fore.YELLOW +"\nPresione ENTER para continuar...")

        elif opcion == "7":
            os.system("cls")
            print("\nFuncion deshabilitada para la entrega del 40%")
            input("\nPresione ENTER para volver...")

        elif opcion == "8":
            os.system("cls")
            print(Fore.YELLOW + "\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            os.system("cls")
            print(Fore.YELLOW + "\nOpcion invalida")
            time.sleep(1)
