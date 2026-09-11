def mostar_menu_principal():
    opcion = ""

    while opcion != "5":

        print()
        print("===================================")
        print("    SISTEMA DE GESTION OBRA SOCIAL")
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
            print("Ingreso como medico")
        elif opcion == "3":
            print("Ingreso como farmacia")
        elif opcion == "4":
            print("Ingreso como Admin/ Gestion")
        elif opcion == "5":
            print("Saliste!")
        else:
            print("Opcion invalida. ")


def mostrar_menu_afiliados():
    opcion = ""

    while opcion != "5":
        print()
        print("===================================")
        print("    MENU DE AFILIADOS    ")
        print("===================================")
        print("1. Ver perfil.")
        print("2. Ver cartilla.") #detalla que servicios de salud cubre el plan...
        print("3. Cambiar plan.")
        print("4. Turnos.")
        print("5. Volver.")

        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            print("MI PERFIL")
        elif opcion == "2":
            print("Ver mi cartilla")
        elif opcion == "3":
            print("Cambiar plan")
        elif opcion == "4":
            print("Ver mis Turnos")
        elif opcion == "5":
            print("Volviste al menu principal...")
        else:
            print("Opcion invalida")

