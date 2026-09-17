import usuarios
import admin
import base_datos
import MedicosFarmacias
import auth


def mostrar_menu_principal():
    opcion = ""

    while opcion != "3":
        print()
        print("===================================")
        print("   SISTEMA DE GESTION OBRA SOCIALL")
        print("===================================")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuario = auth.iniciar_sesion(base_datos.lista_usuarios)

            if usuario != None:
                mostrar_menu_afiliados(usuario["CUIT"])

        elif opcion == "2":
            usuarios.alta_usuario()
        # Acá pondriamos el alta del user

        elif opcion == "3":
            print("Saliste")
        else:
            print("Opción invalida...")


def mostrar_menu_login():
    opcion = ""

    while opcion != "5":

        print()
        print("===================================")
        print("         INICIAR SESIÓN")
        print("===================================")
        print("1. Ingresa como afiliado")
        print("2. Ingresa como medico")
        print("3. Ingresa como farmacia")
        print("4. Ingresa como Admin/ Gestion")
        print("5. Salir")

        opcion = input("Selecciones una opcion: ")

        if opcion == "1":
            mostrar_menu_afiliados()
        elif opcion == "2":
            mostrar_menu_medico()
        elif opcion == "3":
            mostrar_menu_farmacia()
        elif opcion == "4":
            mostrar_menu_admin()


def mostrar_menu_afiliados(cuit):
    opcion = ""

    while opcion != "6":
        print()
        print("===================================")
        print("       MENU DE AFILIADOS")
        print("===================================")
        print("1. Ver perfil.")
        print("2. Ver cobertura.")  # detalla que servicios de salud cubre el plan...
        print("3. Seleccionar / Cambiar plan. DESHABILITADO")
        print("4. Turnos. DESHABILITADO")
        print("5. Darse de baja")
        print("6. Volver.")

        opcion = input("Ingrese una opcion: ")
        cuit = 20444555666  # VARIABLE PARA EVITAR ERRORES Y PROBAR, CAMBIAR POR EL CUIT DEL USER QUE INICIO SESION
        if opcion == "1":
            usuarios.ver_mi_perfil_user(cuit)  # Ingresar cuit de usuario loggeado
        elif opcion == "2":
            usuarios.ver_cartilla(cuit)
        elif opcion == "3":
            print("Seleccionar / Cambiar plan")
        elif opcion == "4":
            print("Ver mis Turnos")
        elif opcion == "5":
            usuarios.baja_usuario(cuit)  # Ingresar cuit de usuario loggeado
        elif opcion == "6":
            print("Volviste al menu principal...")
        else:
            print("Opcion invalida")


def mostrar_menu_medico():
    opcion = ""

    while opcion != "4":
        print()
        print("===================================")
        print("          MENU DE MEDICO")
        print("===================================")
        print("1. Darse de alta")
        print("2. Darse de baja")
        print("3. Ver pacientes asignados - DESHABILITADO")
        print("4. Volver")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("Darse de alta")
            MedicosFarmacias.alta_medico(base_datos.Medicos)
        elif opcion == "2":
            print("Solicitud de baja")
            MedicosFarmacias.eliminar_medico(base_datos.Medicos)
        elif opcion == "3":
            print("Funcion deshabilitada para la entrega del 40%")

        elif opcion == "4":
            print("Volviendo al menu principal...")

        else:
            print("Opcion invalida")


def mostrar_menu_farmacia():
    opcion = ""

    while opcion != "2":

        print()
        print("===================================")
        print("         MENU DE FARMACIA")
        print("===================================")
        print("1. Consultar estado de afiliado")
        print("2. Volver")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("Consulta de afiliado")

        elif opcion == "2":
            print("Volviendo al menu principal...")

        else:
            print("Opcion invalida")


def mostrar_menu_admin():
    opcion = ""

    while opcion != "8":
        print()
        print("===================================")
        print("        MENU GESTION / ADMIN")
        print("===================================")
        print("1. Dar de alta usuario")
        print("2. Dar de baja usuario")
        print("3. Manejar usuarios deudores")
        print("4. Ver lista de afiliados")
        print("5. Ver lista de medicos")
        print("6. Ver lista de farmacias")
        print("7. Ver historial - DESHABILITADO")
        print("8. Volver")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            usuarios.alta_usuario()

        elif opcion == "2":
            admin.baja_usuario()

        elif opcion == "3":
            admin.deudores()

        elif opcion == "4":
            usuarios.ver_lista_usuarios()

        elif opcion == "5":
            MedicosFarmacias.imprimir_lista_medicos(base_datos.Medicos)

        elif opcion == "6":
            MedicosFarmacias.imprimir_lista_farmacias(base_datos.Farmacias)

        elif opcion == "7":
            print("Funcion deshabilitada para la entrega del 40%")

        elif opcion == "8":
            print("Volviendo al menu principal...")

        else:
            print("Opcion invalida")
