def mostrar_menu_principal():
    opcion = ""

    while opcion !="3":
        print ()
        print("===================================")
        print("   SISTEMA DE GESTION OBRA SOCIALL")
        print("===================================")
        print("1. Iniciar sesion")
        print("2. Registrarse")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_menu_login()
        elif opcion == "2":
            print("registro del nuevo usuario")
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


def mostrar_menu_afiliados():
    opcion = ""

    while opcion != "6":
        print()
        print("===================================")
        print("       MENU DE AFILIADOS")
        print("===================================")
        print("1. Ver perfil.")
        print("2. Ver cartilla.") #detalla que servicios de salud cubre el plan...
        print("3. Seleccionar / Cambiar plan.")
        print("4. Turnos.")
        print("5. Darse de baja")
        print("6. Volver.")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("MI PERFIL")
        elif opcion == "2":
            print("Ver mi cartilla")
        elif opcion == "3":
            print("Seleccionar / Cambiar plan")
        elif opcion == "4":
            print("Ver mis Turnos")
        elif opcion == "5":
            print("Darse de baja")
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
        print("1. Darse de baja")
        print("2. Ver agenda de turnos - DESHABILITADO")
        print("3. Ver pacientes asignados - DESHABILITADO")
        print("4. Volver")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("Solicitud de baja")

        elif opcion == "2":
            print("Funcion deshabilitada para la entrega del 40%")

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

    while opcion != "7":
        print()
        print("===================================")
        print("        MENU GESTION / ADMIN")
        print("===================================")
        print("1. Dar de alta usuario")
        print("2. Dar de baja usuario")
        print("3. Ver lista de afiliados")
        print("4. Ver lista de medicos")
        print("5. Ver lista de farmacias")
        print("6. Ver historial - DESHABILITADO")
        print("7. Volver")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("Alta de usuario")

        elif opcion == "2":
            print("Baja de usuario")

        elif opcion == "3":
            print("Lista de afiliados")

        elif opcion == "4":
            print("Lista de medicos")

        elif opcion == "5":
            print("Lista de farmacias")

        elif opcion == "6":
            print("Funcion deshabilitada para la entrega del 40%")

        elif opcion == "7":
            print("Volviendo al menu principal...")

        else:
            print("Opcion invalida")
