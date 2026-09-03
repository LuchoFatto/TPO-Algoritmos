#Datos iniciales
def cargar_datos_iniciales():
    usuarios = []
    return usuarios

# Usuarios
def alta_usuario(Lista_usuario):
    cuit = input("Ingrese CUIT/DNI: ")
    nombre = input("Ingrese nombre y apellido: ")
    email = input("Ingrese email: ")
    telefono = input("Ingrese telefono: ")

    nuevo_usuario = [cuit,nombre,email,telefono]

    Lista_usuario.append(nuevo_usuario)

    print("'usuario cargado correctamente'")
  

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