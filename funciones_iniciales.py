import validaciones

# Usuarios
def alta_usuario(usuarios):
    pass

def modificar_usuario():
    pass

def eliminar_usuario():
    pass

def verificar_estado_pagos():
    pass

def buscar_usuarios():
    pass

# Afiliados / médicos
def alta_medico(usuarios):

    medico_nombre = validaciones.bucle_medico("Ingrese su nombre: ", "SOLO LETRAS - Ingrese su nombre: ", validaciones.validador_solo_letras) #verifica solo letras sin limite de caracteres

    medico_apellido = validaciones.bucle_medico("ingrse su apellido: ", "SOLO LETRAS - Ingrese su apellido: ", validaciones.validador_solo_letras)

    medico_matricula = input("Ingrese su NRO de matricula: ")
    flag_matricula = validaciones.validador_solo_numeros(medico_matricula)
    while flag_matricula == False:
        medico_matricula = input("SOLO NUMEROS SIN GUIONES - Ingrese su NRO de matricula: ")
        flag_matricula = validaciones.validador_solo_numeros(medico_matricula)
    
    medico_email = input("Ingrese su email: ")
    flag_email = validaciones.validar_email(medico_email)
    while flag_email == False:
        medico_email = input("ERROR - Ingrese su email correctamente: ")
        flag_email = validaciones.validar_email(medico_email)

    usuarios.append({"nombre":medico_nombre, "apellido":medico_apellido, "matricula":medico_matricula, "email":medico_email})

def modificar_medico(usuarios):
    matricula_medico_eliminar = input("Para modificar un medico ingrese el numero de matricula: ")
    flag = None
    for user in usuarios:
        if user["rol"] == "medico" and user["matricula"] == str(matricula_medico_eliminar):
            opcion = input("que desea modificar: 1) mail - 2) contraseña")    
            if opcion == "1":
                user["email"] = input("Ingrese el nuevo Email del Medico/a: ")#agregar validacion de email y letras
                flag_email = validaciones.validar_email(user["email"])
                while flag_email == False:
                    user["email"] = input("Ingrese su mail correctamente: ")
                    flag_email = validaciones.validar_email(user["email"])
 
    
def eliminar_medico(usuarios):
    matricula_medico_eliminar = input("Para darse de baja ingrese el numero de matricula: ")
    for user in usuarios:
        if user["rol"] == "medico" and user["matricula"] == str(matricula_medico_eliminar):
            confirmacion = input("Confirmacion, desea eliminar? SI/NO:  ") #hay que agregar que preguntar para confirmar
            if confirmacion == "SI": 
                usuarios.remove(user)
            else:
                pass #se vuelve al menu donde se eligio eliminar medico
            #hay que añadir que si entra a la lista de medicos y no hay nadie con el rol medico que te diga no hay medicos para eliminar

def imprimir_lista_medicos(usuarios):
    for user in usuarios:
            if user["rol"] == "medico":
                print("\nNombre: {0}".format(user["nombre"],))
                print("Apellido: {0}".format(user["apellido"]))
                print("Email: {0}".format(user["email"]))
                print("Rol: {0}".format(user["rol"]))
                print("Matricula: {0}".format(user["matricula"]))
                print("Contraseña: {0}".format(user["contraseña"]))
                print("Telefono: {0}".format(user["telefono"]))

def imprimir_lista_farmacias(farmacias):
    for farmacia in farmacias:
            print("\nID Farmacia: {0}".format(farmacia["id"],))
            print("Direccion: {0}".format(farmacia["direccion"]))
            print("Beneficiaria: {0}".format(farmacia["beneficiaria"]))

# Farmacias
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



# Menus
def menu_gestion():
    pass


def menu_usuario():
    pass


def menu_medico():
    pass


def menu_farmacia():
    pass


def menu_alta_usuario():
    pass


# Turnos
def pedir_turno():
    pass


# Login y permisos
def mostrar_menu_segun_rol():
    pass


"""
funciones reempalzadas:

    medico_apellido = input("Ingrese su apellido: ")
    flag_apellido = validaciones.validador_solo_letras(medico_apellido)
    while flag_apellido == False:
        medico_apellido = input("SOLO LETRAS - Ingrese su apellido: ")
        flag_apellido = validaciones.validador_solo_letras(medico_apellido)
"""