import re
import validaciones


#Todos los planes disponibles y sus descripciones (Nombre, Precio Mensual, Descripcion)
Planes = (('Basico',5000,"Covertura del 40%"),('Plus',10000,"Covertura del 65%"),('Familiar',12000,"Covertura del 50% y posibilidad de añadir hasta 2 hijos y 1 conyuge"))


#Base del tipo Usuario
diccionario_usuario = {
    'Nombre' : str,
    'Apellido' : str,
    'CUIT' : int,
    'Telefono' : int,
    'Plan' : str,
    'Password' : str,
    'Email' : str,
    'Historial':[]
}

#Lista de todos los usuarios
lista_usuarios = []

def imprimir_usuario(dic):
    for key,valor in dic.items():
        print('-'*30)
        print(f'{key} : {valor}')
    print('-'*30)



def alta_usuario():

    Reinicio = True

    while Reinicio:
        print('-'*50)
        #Ingreso de Nombre de Usuario
        diccionario_usuario['Nombre'] = input('Ingrese el Nombre\n>> ')
        Flag = True
        while Flag:
            if not validaciones.validacion_letras(diccionario_usuario['Nombre']):
                print('Ingrese exclusivamente letras')
                input('Ingrese Enter para reintentar')
                print('\n\n')
                diccionario_usuario['Nombre'] = input('Ingrese el Nombre\n>> ')
            else:
                Flag = False
            
        print('-'*50)

        #Ingreso de Apellido de Usuario
        diccionario_usuario['Apellido'] = input('Ingrese el Apellido\n>> ')
        Flag = True
        while Flag:
            if not validaciones.validacion_letras(diccionario_usuario['Apellido']):
                print('Ingrese exclusivamente letras')
                input('Ingrese Enter para reintentar')
                print('\n\n')
                diccionario_usuario['Apellido'] = input('Ingrese el Apellido\n>> ')
            else:
                Flag = False
        print('-'*50)

        #Ingreso de CUIT de Usuario
        diccionario_usuario['CUIT'] = validaciones.validar_cuit(input('Ingrese el CUIT\n>> '))
        Flag = True
        while Flag:
            if diccionario_usuario['CUIT'] == None or Flag == True:
                print('Ingrese correctamente el CUIT')
                input('Ingrese Enter para reintentar')
                print('\n\n')
                diccionario_usuario['CUIT'] = validaciones.validar_cuit(input('Ingrese el CUIT\n>> '))
            else:
                for i in lista_usuarios:
                    if i['CUIT'] == diccionario_usuario['CUIT']:
                        print('El CUIT ingresado ya existe')
                        input('Ingrese Enter para reintentar')
                        Flag = True
                        break
                    else:
                        Flag = False


        print('-'*50)

        #Ingreso de Telefono de Usuario
        diccionario_usuario['Telefono'] = validaciones.validar_telefono(input('Ingrese el Telefono (Sin el 15 ni 0)\n>> '))
        Flag = True
        while Flag:
            if diccionario_usuario['Telefono'] == None:
                print('Ingrese correctamente el Telefono')
                input('Ingrese Enter para reintentar')
                print('\n\n')
                diccionario_usuario['Telefono'] = validaciones.validar_telefono(input('Ingrese el Telefono (Sin el 15 ni 0)\n>> '))
            else:
                Flag = False
        print('-'*50)

        #Eleccion de Plan de Usuario
        print('Elija un Plan de Pago')
        Contador = 0

        #Muestra los Planes en pantalla
        for i in Planes:
            Contador += 1
            print(f'{Contador}- {i[0]} >> {i[2]} << ${i[1]} x Mes')
        eleccion = int(input('\n--Ingrese el numero de la opcion acorde--\n>> ')) #Falta verificar que sea numero

        Flag = True
        while Flag:
            if eleccion > Contador:
                print('Numero Invalido')
                input('Presione Enter Para reintentar')
                print('\n\n')
                Contador = 0
                for i in Planes:
                    Contador += 1
                    print(f'{Contador}- {i[0]} >> {i[2]} << ${i[1]} x Mes')
                eleccion = int(input('\n--Ingrese el numero de la opcion acorde--\n>> ')) #Falta verificar que sea numero
            else:
                Flag = False

        #Se guarda el plan en Usuario
        diccionario_usuario['Plan'] = Planes[eleccion-1][0]
        print('-'*50)
        print('\n\n')
        imprimir_usuario(diccionario_usuario)
        print('\n')
        print('Revise los datos, si desea salir sin cargar ingrese 2\nSi desea volver a intentar ingrese 0\nSi esta todo correcto ingrese 0') #Posible recursividad en el futuro
        Check,Flag = True,True
        while Flag:
            Check = input('>> ')
            if Check == '2':
                return
            if Check == '1':
                lista_usuarios.append(diccionario_usuario)
                print('Usuario ingresado con exito')
                input('Presione Enter para volver al menu anterior')
                print('\n')
                Flag,Reinicio = False,False
            elif Check == '0':
                print('Reiniciando proceso de carga')
                input('Presione Enter para seguir')
                print('\n')
                Flag = False
            else:
                print('Ingrese uno de los valores indicados')
                print('Revise los datos, si esta todo correcto ingrese 1, sino ingrese 0 y vuelva a intentar')
                print('\n')




def modificar_usuario():
    pass

def baja_usuario():
    pass

def buscar_usuarios():
    pass

def menu_alta_usuario():
    pass

alta_usuario()
