import usuarios
import auth
import base_datos

def baja_usuario():
    Flag = True
    while Flag:
        print('Ingrese el cuit del usuario que desea dar de baja o ingrese 0 para volver')
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
    while Flag:
        print('Ingrese 1 si desea cancelar una deuda\nIngrese 2 si desea marcar usuario como deudor\nIngrese 0 si desea volver')
        opcion = input('>> ')
        if opcion == '1':
            usuario_pago()
            return
        elif opcion == '2':
            usuario_deudor()
            return
        elif opcion == '0':
            return
        else:
            print('Ingrese una opcion correcta')


def usuario_pago():
    Flag = True
    while Flag:
        print('Ingrese el cuit del usuario que desea dar de autorizar el pago o ingrese 0 para volver')
        cuit = input('>> ')
        if cuit == '0':
            return
        elif auth.validar_cuit(cuit):
            indice, usuario = usuarios.buscar_usuarios(cuit)
            if indice == None:
                print('El usuario ingresado no existe')
            else:
                if usuario['Deudor'] == False:
                    print('El usuario ya esta libre de deuda')
                    input('Ingrese Enter para volver')
                else:
                    usuario['Deudor'] = False
                    base_datos.lista_usuarios[indice] = usuario
                    print('Se ha confirmado la cancelacion de deuda del usuario')
                    input('Ingrese Enter para volver')
                return
        else:
            print('Ingrese un CUIT valido')


def usuario_deudor():
    Flag = True
    while Flag:
        print('Ingrese el cuit del usuario que desea dar de autorizar el pago o ingrese 0 para volver')
        cuit = input('>> ')
        if cuit == '0':
            return
        elif auth.validar_cuit(cuit):
            indice, usuario = usuarios.buscar_usuarios(cuit)
            if indice == None:
                print('El usuario ingresado no existe')
                input('Ingrese Enter para volver')
            else:
                if usuario['Deudor'] == True:
                    print('El usuario ya es deudor')
                    input('Ingrese Enter para volver')
                else:
                    usuario['Deudor'] = True
                    base_datos.lista_usuarios[indice] = usuario
                    print('Se ha cambiado el estado del usuario a deudor')
                    input('Ingrese Enter para volver')
                return
        else:
            print('Ingrese un CUIT valido')