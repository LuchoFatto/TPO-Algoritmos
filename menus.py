def mostar_menu_principal():
    opcion = ""

    while opcion != "5":

        print()
        print("===================================")
        print("   SISTEMA DE GESTION OBRA SOCIAL")
        print("===================================")
        print("1. ingresa como afiliado")
        print("2. ingresa como medico")
        print("3. ingresa como farmacia")
        print("4. ingresa como Admin/ Gestion")
        print("5. Salir")

        opcion = input("selecciones una opcion: ")

        if opcion == "1":
            print("Ingreso como afiliado")
        elif opcion == "2":
            print("Ingreso como medico")
        elif opcion == "3":
            print("Ingreso como farmacia")
        elif opcion == "4":
            print("Ingreso como Admin/ Gestion")
        elif opcion == "5":
            print("Saliste!")
        else:
            print("opcion invalida. ")