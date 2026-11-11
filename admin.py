import usuarios
import auth
import base_datos
from usuarios import esperar,RUTA_ARCHIVO
import os

def baja_usuario():
    Flag = True
    while Flag:
        print('Ingrese el cuit del usuario que desea dar de baja o ingrese 0 para volver')
        esperar()
        cuit = input('>> ')
        if cuit == '0':
            return
        elif auth.validar_cuit(cuit):
            usuarios.eliminar_usuario(cuit)
            return
        else:
            print('Ingrese un CUIT valido')


def deudores():
    Flag = True
    lista_u = auth.abrir_archivo(RUTA_ARCHIVO)
    while Flag:
        print('[1] Cancelar una deuda\n[2] Marcar usuario como deudor\n[0] Volver')
        esperar()
        opcion = input('>> ')
        if opcion == '1':
            indice,usuario = usuario_pago()
            if indice is not None:
                lista_u[indice] = usuario
        elif opcion == '2':
            indice,usuario = usuario_deudor()
            if indice is not None:
                lista_u[indice] = usuario
        elif opcion == '0':
            return
        else:
            print('Ingrese una opcion correcta')

        auth.cargar_archivo(lista_u,RUTA_ARCHIVO)


def usuario_pago():

    Flag = True
    while Flag:
        print('Ingrese el cuit del usuario que desea dar de autorizar el pago o ingrese 0 para volver')
        esperar()
        cuit = input('>> ')
        if cuit == '0':
            return None,None
        elif auth.validar_cuit(cuit):
            indice, usuario = usuarios.buscar_usuarios(cuit)
            if indice == None:
                print('El usuario ingresado no existe')
            else:
                if usuario['Deudor'] == False:
                    print('El usuario ya esta libre de deuda')
                    esperar()
                    input('Ingrese Enter para volver')
                    os.system('cls')
                else:
                    usuario['Deudor'] = False
                    print('Se ha confirmado la cancelacion de deuda del usuario')
                    esperar()
                    input('Ingrese Enter para volver')
                    os.system('cls')
                return indice,usuarios
        else:
            print('Ingrese un CUIT valido')
            esperar()


def usuario_deudor():
    Flag = True
    while Flag:
        print('Ingrese el cuit del usuario que desea dar de autorizar el pago o ingrese 0 para volver')
        esperar()
        cuit = input('>> ')
        if cuit == '0':
            return None, None
        elif auth.validar_cuit(cuit):
            indice, usuario = usuarios.buscar_usuarios(cuit)
            if indice == None:
                print('El usuario ingresado no existe')
                esperar()
                input('Ingrese Enter para volver')
                os.system('cls')
            else:
                if usuario['Deudor'] == True:
                    print('El usuario ya es deudor')
                    esperar()
                    input('Ingrese Enter para volver')
                    os.system('cls')
                else:
                    usuario['Deudor'] = True
                    print('Se ha cambiado el estado del usuario a deudor')
                    esperar()
                    input('Ingrese Enter para volver')
                    os.system('cls')
                return indice,usuario
        else:
            print('Ingrese un CUIT valido')


def iniciar_sesion_admin():

    print()
    print("===================================")
    print("          INICIAR SESION")
    print("===================================")

    user = input("Ingrese su USER de ADMIN: ")


    if base_datos.Admin["Usuario"] == user:
        intentos = 3
        while intentos > 0:
            password = input("Ingrese su contraseña: ")
            if base_datos.Admin["Contraseña"] == password:
                return True
            else:
                intentos -= 1
                print("Contraseña incorrecta")
                esperar()
                print("Intentos restantes:", intentos)
                esperar()
                print("Se agotaron los intentos")
                return None
    else:
        print("Usuario incorrecto")
        return False