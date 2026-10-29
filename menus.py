
import usuarios
import admin
import base_datos
import MedicosFarmacias
import auth
import time
import os


def mostrar_menu_principal():
    opcion = ""

    while opcion != "3":
        print()
        print("=" * 40)
        time.sleep(0.1)
        print("   SISTEMA DE GESTION OBRA SOCIAL")
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print("1. Iniciar sesion")
        time.sleep(0.1)
        print("2. Registrarse")
        time.sleep(0.1)
        print("3. Salir")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            print("\nIniciando sesion...")
            time.sleep(1)
            os.system("cls")
            mostrar_menu_login()

        elif opcion == "2":
            print("\nCargando registro...")
            time.sleep(1)
            usuarios.alta_usuario()
            input("\nPresione ENTER para continuar...")
            os.system("cls")

        elif opcion == "3":
            print("\nSaliendo del sistema...")
            time.sleep(2)
            os.system("cls")
            print("Hasta luego!")

        else:
            os.system("cls")
            print("\nOpcion invalida...")
            time.sleep(1)


def mostrar_menu_login():
    opcion = ""

    while opcion != "5":
        print()
        print("=" * 40)
        time.sleep(0.1)
        print("           INICIAR SESION")
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print("1. Ingresa como afiliado")
        time.sleep(0.1)
        print("2. Ingresa como medico")
        time.sleep(0.1)
        print("3. Ingresa como farmacia")
        time.sleep(0.1)
        print("4. Ingresa como Admin / Gestion")
        time.sleep(0.1)
        print("5. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            os.system("cls")
            print("\nCargando inicio de sesion...")
            time.sleep(1)

            usuario = auth.iniciar_sesion(base_datos.lista_usuarios)

            if usuario != None:
                os.system("cls")
                print("\nIngresando al sistema...")
                time.sleep(1)
                mostrar_menu_afiliados(usuario["CUIT"])
                

        elif opcion == "2":
            os.system("cls")
            print("\nFuncion deshabilitada")
            input("\nPresione ENTER para volver...")
            # mostrar_menu_medico()

        elif opcion == "3":
            os.system("cls")
            print("\nFuncion deshabilitada")
            input("\nPresione ENTER para volver...")
            # mostrar_menu_farmacia()

        elif opcion == "4":
            os.system("cls")
            print("\nCargando acceso de administrador...")
            time.sleep(1)

            if auth.iniciar_sesion_admin():
                os.system("cls")
                print("\nAcceso autorizado...")
                time.sleep(1)
                mostrar_menu_admin()
            else:
                return

        elif opcion == "5":
            os.system("cls")
            print("\nVolviendo al menu principal...")
            time.sleep(1)

        else:
            os.system("cls")
            print("\nOpcion invalida...")
            time.sleep(1)


def mostrar_menu_afiliados(cuit):
    opcion = ""

    while opcion != "6":
        print()
        print("=" * 40)
        time.sleep(0.1)
        print("         MENU DE AFILIADOS")
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print("1. Ver perfil.")
        time.sleep(0.1)
        print("2. Ver cobertura.")
        time.sleep(0.1)
        print("3. Seleccionar / Cambiar plan. DESHABILITADO")
        time.sleep(0.1)
        print("4. Turnos. DESHABILITADO")
        time.sleep(0.1)
        print("5. Darse de baja")
        time.sleep(0.1)
        print("6. Volver.")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print("\nCargando perfil...")
            time.sleep(1)
            usuarios.ver_mi_perfil_user(cuit)
            input("\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print("\nCargando cobertura...")
            time.sleep(1)
            usuarios.ver_cartilla(cuit)
            input("\nPresione ENTER para continuar...")

        elif opcion == "3":
            os.system("cls")
            print("\nSeleccionar / Cambiar plan")
            print("Funcion deshabilitada")
            input("\nPresione ENTER para volver...")

        elif opcion == "4":
            os.system("cls")
            print("\nVer mis turnos")
            print("Funcion deshabilitada")
            input("\nPresione ENTER para volver...")

        elif opcion == "5":
            os.system("cls")
            print("\nProcesando solicitud de baja...")
            time.sleep(1)
            usuarios.baja_usuario(cuit)
            input("\nPresione ENTER para continuar...")

        elif opcion == "6":
            os.system("cls")
            print("\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            print("\nOpcion invalida")
            time.sleep(1)


def mostrar_menu_medico():
    opcion = ""

    while opcion != "4":
        print()
        print("=" * 40)
        time.sleep(0.1)
        print("           MENU DE MEDICO")
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print("1. Darse de alta")
        time.sleep(0.1)
        print("2. Darse de baja")
        time.sleep(0.1)
        print("3. Ver pacientes asignados - DESHABILITADO")
        time.sleep(0.1)
        print("4. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print("\nCargando alta de medico...")
            time.sleep(1)
            MedicosFarmacias.alta_medico(base_datos.Medicos)
            input("\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print("\nCargando solicitud de baja...")
            time.sleep(1)
            MedicosFarmacias.eliminar_medico(base_datos.Medicos)
            input("\nPresione ENTER para continuar...")

        elif opcion == "3":
            os.system("cls")
            print("\nFuncion deshabilitada para la entrega del 40%")
            input("\nPresione ENTER para volver...")

        elif opcion == "4":
            os.system("cls")
            print("\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            os.system("cls")
            print("\nOpcion invalida")
            time.sleep(1)


def mostrar_menu_farmacia():
    opcion = ""

    while opcion != "2":
        print()
        print("=" * 40)
        time.sleep(0.1)
        print("          MENU DE FARMACIA")
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print("1. Consultar estado de afiliado")
        time.sleep(0.1)
        print("2. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print("\nConsultando estado de afiliado...")
            time.sleep(1)
            print("Consulta de afiliado")
            input("\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print("\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            os.system("cls")
            print("\nOpcion invalida")
            time.sleep(1)


def mostrar_menu_admin():
    opcion = ""

    while opcion != "8":
        print()
        print("=" * 40)
        time.sleep(0.1)
        print("       MENU GESTION / ADMIN")
        time.sleep(0.1)
        print("=" * 40)
        time.sleep(0.1)
        print("1. Dar de alta usuario")
        time.sleep(0.1)
        print("2. Dar de baja usuario")
        time.sleep(0.1)
        print("3. Manejar usuarios deudores")
        time.sleep(0.1)
        print("4. Ver lista de afiliados")
        time.sleep(0.1)
        print("5. Ver lista de medicos")
        time.sleep(0.1)
        print("6. Ver lista de farmacias")
        time.sleep(0.1)
        print("7. Ver historial - DESHABILITADO")
        time.sleep(0.1)
        print("8. Volver")
        time.sleep(0.1)
        print("=" * 40)

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            os.system("cls")
            print("\nCargando alta de usuario...")
            time.sleep(1)
            usuarios.alta_usuario()
            input("\nPresione ENTER para continuar...")

        elif opcion == "2":
            os.system("cls")
            print("\nCargando baja de usuario...")
            time.sleep(1)
            admin.baja_usuario()
            input("\nPresione ENTER para continuar...")

        elif opcion == "3":
            os.system("cls")
            print("\nConsultando usuarios deudores...")
            time.sleep(1)
            admin.deudores()
            input("\nPresione ENTER para continuar...")

        elif opcion == "4":
            os.system("cls")
            print("\nCargando lista de afiliados...")
            time.sleep(1)
            usuarios.ver_lista_usuarios()
            input("\nPresione ENTER para continuar...")

        elif opcion == "5":
            os.system("cls")
            print("\nCargando lista de medicos...")
            time.sleep(1)
            MedicosFarmacias.imprimir_lista_medicos(base_datos.Medicos)
            input("\nPresione ENTER para continuar...")

        elif opcion == "6":
            os.system("cls")
            print("\nCargando lista de farmacias...")
            time.sleep(1)
            MedicosFarmacias.imprimir_lista_farmacias(base_datos.Farmacias)
            input("\nPresione ENTER para continuar...")

        elif opcion == "7":
            os.system("cls")
            print("\nFuncion deshabilitada para la entrega del 40%")
            input("\nPresione ENTER para volver...")

        elif opcion == "8":
            os.system("cls")
            print("\nVolviendo al menu anterior...")
            time.sleep(1)

        else:
            os.system("cls")
            print("\nOpcion invalida")
            time.sleep(1)
