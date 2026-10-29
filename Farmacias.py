import validaciones

# Farmacias
def imprimir_lista_farmacias(farmacias):
    for farmacia in farmacias:
            print("\nID Farmacia: {0}".format(farmacia["id"],))
            print("Direccion: {0}".format(farmacia["direccion"]))
            print("Beneficiaria: {0}".format(farmacia["beneficiaria"]))

def cargar_farmacia(farmacias):

    id_farmacia = input("ingrese el nombre de la farmacia: ")
    flag_id_farmacia = validaciones.validador_solo_letras(id_farmacia)
    while flag_id_farmacia == False:
        id_farmacia = input("ingrese el nombre de la farmacia: ")
        flag_id_farmacia = validaciones.validador_solo_letras(id_farmacia)

    direccion_farmacia = input("Ingrese la direccion: ")
    flag = validaciones.validar_direccion(direccion_farmacia)
    while flag == False:
        direccion_farmacia = input("Ingrese la direccion correctamente: ")
        flag = validaciones.validar_direccion(direccion_farmacia)

    numero_farmacia = input("indique nro de telefono: ")
    flag_numero_farmacia = validaciones.validador_solo_numeros(numero_farmacia)
    while flag_numero_farmacia == False:
        numero_farmacia = input("indique nro de telefono: ")
        flag_numero_farmacia = validaciones.validador_solo_numeros(numero_farmacia)

    farmacias.append({"id": id_farmacia, "direccion": direccion_farmacia, "numero": numero_farmacia})

def eliminar_farmacia(farmacias):
    id_farmacia_eliminar = input("Para eliminar la farmacia ingrese su ID: ")
    for farmacia in farmacias:
        if farmacia["id"] == str(id_farmacia_eliminar):
            farmacias.remove(farmacia)
            #confirmacion = input("Confirmacion: desea eliminar? SI/NO") #hay que agregar que preguntar para confirmar
            #if confirmacion == "SI":
            #    usuarios.remove(user)
            #else:
            #    pass #se vuelve al menu donde se eligio eliminar medico

