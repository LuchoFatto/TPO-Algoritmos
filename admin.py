import usuarios
import auth

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
