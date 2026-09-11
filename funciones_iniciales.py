#from base_datos import usuarios
# Usuarios
def alta_usuario(usuarios):
    usuario_nombre = input("Ingrese su nombre: ")
    usuario_apellido = input("Ingrese su apellido: ")
    usuario_email = input("Ingrese su email: ")
    usuario_rol = input("Ingrese su rol: ")
    usuarios.append({"nombre":usuario_nombre, "apellido":usuario_apellido, "email":usuario_email, "rol":usuario_rol})

def modificar_usuario():
    pass

def eliminar_usuario():
    pass

def verificar_estado_pagos():
    pass

def buscar_usuarios():
    pass

# Afiliados / médicos
def alta_medico():
    pass

def modificar_medico():
    pass

def eliminar_medico():
    pass

# Farmacias
def cargar_farmacia():
    pass


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
