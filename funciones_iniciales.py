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

    medico_nombre = validaciones.bucle_medico("Ingrese su nombre: ", "SOLO LETRAS - Ingrese su nombre: ", validaciones.validador_solo_letras)

    medico_apellido = input("Ingrese su apellido: ")
    flag_apellido = validaciones.validador_solo_letras(medico_apellido)
    while flag_apellido == False:
        medico_apellido = input("SOLO LETRAS - Ingrese su apellido: ")
        flag_apellido = validaciones.validador_solo_letras(medico_apellido)

    medico_matricula = input("Ingrese su NRO de matricula: ")
    flag_matricula = validaciones.validador_solo_numeros(medico_matricula)
    while flag_matricula == False:
        medico_matricula = input("SOLO NUMEROS SIN GUIONES - Ingrese su NRO de matricula: ")
        flag_matricula = validaciones.validador_solo_numeros(medico_matricula)
    
    medico_email = input("Ingrese su mail: ")
    flag_email = validaciones.validar_mail(medico_email)
    while flag_email == False:
        medico_email = input("Ingrese su mail correctamente: ")
        flag_email = validaciones.validar_mail(medico_email)

    usuarios.append({"nombre":medico_nombre, "apellido":medico_apellido, "matricula":medico_matricula, "email":medico_email})

def modificar_medico(usuarios):
    matricula_medico_eliminar = input("Para modificar un medico ingrese el numero de matricula: ")
    flag = None
    for user in usuarios:
        if user["rol"] == "medico" and user["matricula"] == str(matricula_medico_eliminar):
            opcion = input("que desea modificar: 1) mail - 2) contraseña")    
            if opcion == "1":
                user["email"] = input("Ingrese el nuevo Email del Medico/a: ")#agregar validacion de email y letras
                flag_email = validaciones.validar_mail(user["email"])
                while flag_email == False:
                    medico_email = input("Ingrese su mail correctamente: ")
                    flag_email = validaciones.validar_mail(medico_email)
                print("salio")
    
def eliminar_medico(usuarios):
    matricula_medico_eliminar = input("Para eliminar un medico ingrese el numero de matricula: ")
    for user in usuarios:
        if user["rol"] == "medico" and user["matricula"] == str(matricula_medico_eliminar):
            confirmacion = input("Confirmacion: desea eliminar? SI/NO") #hay que agregar que preguntar para confirmar
            if confirmacion == "SI": 
                usuarios.remove(user)
            

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

def eliminar_farmacia():
    pass


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
