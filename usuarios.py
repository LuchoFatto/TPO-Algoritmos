import re
import auth
import base_datos
import time
import os

#Todos los planes disponibles y sus descripciones (Nombre, Precio Mensual, Descripcion)
PLANES = (
        ('Basico',5000,"Covertura del 40%"),
        ('Plus',10000,"Covertura del 65%"),
        ('Familiar',12000,"Covertura del 50% y posibilidad de añadir hasta 2 hijos y 1 conyuge")
)




#funciones auxiliares
def imprimir_usuario(dic:dict):
    """Imprime el diccionario ingresado de usuario bonito

    Args:
        dic (dict): usuario a imprimir
    """    
    for key,valor in dic.items():
        print('-'*30)
        print(f'| {key} : {valor} |')
        esperar(0.2)
    print('-'*30)

def esperar(num = 0.3):
    """Esperar para imprimir proxima linea

    Args:
        num (float, optional): Tiempo a esperar. Defaults to 0.3.
    """    
    time.sleep(num)

def verificar_decision(elemento):
    """Modo de verificar si la decision del usuario fue correcta

    Args:
        elemento->any: Solo utilizado para mostrar en texto lo que escribio el usuario

    Returns:
        boolean: False si esta de acuerdo con lo escrito, True si no
    """
    Flag = True
    while Flag:
        print('-=-'*10)
        print(f'Usted ha ingresado {elemento}')
        esperar()
        print(f'Si esta bien ingresado ingrese "1"')
        esperar()
        print(f'Si desea reingresar ingrese "2"')
        esperar()
        dec = input('>> ')
        match dec:
            case '1':
                return False
            case '2':
                return True
            case _:
                print('Ingrese una opcion adecuada')
                input('Presione Enter para reintentar')
                os.system('cls')


#funciones para modificar o crear elementos de Usuario
def pedido_datos(mensaje:str, funcion_auth, mensaje_error:str, transformar = False, es_cuit = False):
    """Funcion Generalizada para carga de datos de usuario

    Args:
        mensaje (str): Mensaje a mostrar
        funcion_auth (funcion): Funcion autenticadora
        mensaje_error (str): Mensaje de error a mostrar si falla la funcion
        transformar (bool, optional): Si debe ejecutar "limpiar_nro" o no. Defaults to False.
        es_cuit (bool, optional): Si debe verificar si el cuit existe en la DB. Defaults to False.

    Returns:
        str | int: Devuelve el valor pedido validado y verificado
    """    
    Flag = True

    while Flag:
        dato = input(f'{mensaje}\n>> ')

        if not funcion_auth(dato):
            print(mensaje_error)
            input('Presione Enter para reintentar')
            os.system('cls')
        else:
            if transformar:
                dato = auth.limpiar_nro(dato)

            if es_cuit:
                cuit_duplicado = False
                for i in base_datos.lista_usuarios:
                    if i['CUIT'] == dato:
                        cuit_duplicado = True
                        break
                
                if cuit_duplicado:
                    print('El CUIT ingresado ya existe')
                    input('Ingrese Enter para reintentar')
                    os.system('cls')
                    continue #VERIFICAR SI SE PUEDE USAR

        if not verificar_decision(dato):
            return dato

def elegir_plan():
    """Imprime las posibles elecciones y permite eleccion, para devolver la elegida

    Returns:
        str: Nombre del plan elegido
    """    
    print('Elija un Plan de Pago')
    Flag = True
    while Flag:
        #Muestra los Planes en pantalla
        try:
            for Num,i in enumerate(PLANES):
                print(f'{Num+1}- {i[0]} >> {i[2]} << ${i[1]} x Mes')
                esperar()
            print('--------------------')
            eleccion = int(input('\n--Ingrese el numero de la opcion acorde--\n>> '))
        except:
            print('Ingreso Invalido')
            esperar()
            input('Presione Enter Para reintentar')
            os.system('cls')

        if (eleccion > len(PLANES)) or (eleccion < 1):
            print('Numero Invalido')
            esperar()
            input('Presione Enter Para reintentar')
            os.system('cls')
        else:
            Flag = False

    return PLANES[eleccion-1][0]

def incluirse_plan_familiar(cuit):
    """Verifica si el CUIT del Dueño es correcto, existe y si no esta lleno su lista de familia. Luego se añade el CUIT
    del usuario a dicha lista si cumple y retorna

    Args:
        cuit (str): Cuit del usuario ingresando

    Returns:
        Dict: Diccionario de hijo completo
        None: Si no se completa el ingreso
    """
    #Validar que exista algun usuario en la DB
    if (base_datos.lista_usuarios == []):
        print('No hay usuarios afiliados aun, elija otra opcion') 
    else:
        Valido = True
        while Valido:
            print('Ingrese el CUIT de la persona a la cual se va a incluir, si quiere volver ingrese 0')
            CUIT_principal = input('>> ')

            #Salir del Case, Volver a elegir
            if CUIT_principal == '0':
                Valido = False

            #Validar que sea CUIT
            elif auth.validar_cuit(CUIT_principal):
                print('Ingrese un CUIT valido')
                esperar()
                input('Presione Enter para reintentar')
                os.system('cls')

            else:
                CUIT_principal = auth.limpiar_nro(CUIT_principal)
                #Buscamos el dueño al que se quiere incluir
                for i in base_datos.lista_usuarios:
                    if i['CUIT'] == CUIT_principal and (i['Plan'] == 'Familiar Dueño'):

                        #Si esta lleno, no lo añade
                        if len(i['Familia']) > 2:
                            print('Se ha encontrado el CUIT indicado pero se encuentra en el maximo de afiliados')
                            esperar()
                            input('Presione Enter para reintentar')
                            os.system('cls')
                            break

                        #Sino lo añade al dueño y retorna
                        else:
                            i['CUIT'].append(cuit)
                            return {
                                    'Plan': 'Familiar Hijo',
                                    'Dueño': CUIT_principal
                                }
                
                print('No se ha encontrado ningun afiliado con el plan familiar dueño con ese CUIT')
            
    input('Presione Enter para volver')
    os.system('cls')
    return None

def plan_familiar(cuit):
    """Eleccion de tipo de plan familiar, devolucion de diccionario con datos en base a eleccion

    Args:
        cuit (str): cuit de usuario ingresando

    Returns:
        Dict: Diccionario con keys a añadir a diccionario base
    """    
    Flag = True
    print('Usted ha seleccionado el plan familiar')
    esperar()
    while Flag:
        print('[1] Incluirse a un Plan existente\n !!No puede haber mas de 3 afiliados + titular en el mismo plan familiar!!')
        esperar()
        print('[2] Ser Dueño principal')
        esperar()
        Check = input('>> ')

        match Check:
            case '2':
                print('Se ha guardado como dueño del plan familiar')
                esperar()
                input('Presione Enter para continuar')
                os.system('cls')
                return {
                    'Plan': 'Familiar Dueño',
                    'Familia':[]
                }

            
            case '1':
                hijo = incluirse_plan_familiar(cuit)
                if hijo:
                    return hijo

            case _:
                print('Ingrese uno de los valores indicados')
                esperar()
                os.system('cls')

def pedir_plan(cuit):
    """Eleccion de plan y sus opciones

    Args:
        cuit (str): Cuit del usuario ingresando

    Returns:
        Dict: Diccionario con keys a añadir a diccionario base
    """    

    plan = {
        'Plan' : elegir_plan()
    }

    if plan['Plan'] == 'Familiar':
        plan.update(plan_familiar(cuit))
    
    return plan



def alta_usuario():
    """
        Creacion de Usuario, Verificacion de Datos Ingresados y posibilidad de reincio de ingreso
    """

    Reinicio = True

    while Reinicio:
        diccionario_usuario = {

        #Ingreso de Nombre de Usuario
        'Nombre': pedido_datos('Ingrese el nombre', auth.validacion_letras, 'Ingrese exclusivamente letras'),

        #Ingreso de Apellido de Usuario
        'Apellido' : pedido_datos('Ingrese el apellido', auth.validacion_letras, 'Ingrese exclusivamente letras'),

        #Ingreso de CUIT de Usuario
        'CUIT' : pedido_datos('Ingrese el CUIT', auth.validar_cuit, 'Ingrese correctamente el CUIT', True, True),

        #Ingreso de Telefono de Usuario
        'Telefono' : pedido_datos('Ingrese el Telefono (Sin el 15 ni 0)', auth.validar_numero_telefono, 'Ingrese correctamente el Telefono',True),

        #Ingreso de Email de Usuario
        'Email' : pedido_datos('Ingrese el E-Mail', auth.validar_email, 'Ingrese un Email Valido'),

        #Ingreso de Contraseña de Usuario
        'Password' : pedido_datos('Ingrese su contraseña (Debe tener al menos 8 elementos, uno especial y un numero)',auth.validar_contrasenia,'Ingrese un Contraseña adecuada'),

        'Historial': [],

        'Deudor' : True,

        'Activo' : True
        }

        #Ingreso Plan de Usuario
        diccionario_usuario.update(pedir_plan(diccionario_usuario['CUIT']))



        Check,Flag = True,True
        while Flag:
            print('\n')
            imprimir_usuario(diccionario_usuario)
            print('\n')
            print('Revise los datos, si desea:') #Posible recursividad en el futuro
            esperar()
            print('[2] Salir sin cargar')
            esperar()
            print('[1] Volver a Reingresar')
            esperar()
            print('[0] Todo correcto, continuar')
            Check = input('>> ')
            match Check:
                #Salir SIN CARGAR
                case '2':
                    return

                #Reingreso de datos
                case '1':
                    print('Reiniciando proceso de carga...')
                    esperar(2)
                    input('Presione Enter para seguir')
                    print('\n')
                    Flag = False


                #Todo correcto, carga de datos
                case '0':
                    if 'Dueño' in diccionario_usuario:
                        for i in base_datos.lista_usuarios:
                            if i['CUIT'] == diccionario_usuario['Dueño']:
                                i['Familia'].append(diccionario_usuario['CUIT'])
                                break
                    base_datos.lista_usuarios.append(diccionario_usuario)
                    print('Usuario ingresado con exito')
                    esperar()
                    print('Comuniquese con un encargado de la empresa para cancelar su deuda, al nro 11-22334455')
                    esperar()
                    input('Presione Enter para volver al menu anterior')
                    os.system('cls')
                    Flag,Reinicio = False,False
                
                case _:
                    print('Ingrese uno de los valores indicados')
                    esperar()
                    input('Ingrese Enter para reintentar')
                    os.system('cls')

def baja_usuario(cuit):
    if not verificar_decision('Darse de Baja'):
        eliminar_usuario(cuit)
    else:
        print('Volviendo al menu anterior')

def eliminar_usuario(cuit):
    indice, usuario = buscar_usuarios(cuit)
    if usuario:
        base_datos.lista_usuarios.pop(indice)
        print('Usuario Eliminado')
        input('Presione Enter para volver')
    else:
        print('El usuario ingresado no existe')
        input('Presione Enter para volver')


def buscar_usuarios(cuit):
    for indice, usuario in enumerate(base_datos.lista_usuarios):
        if usuario['CUIT'] == auth.limpiar_nro(cuit):
            return indice, usuario
    return None, None

def ver_lista_usuarios():
    for i in base_datos.lista_usuarios:
        imprimir_usuario(i)

def ver_mi_perfil_user(cuit): #asumo que el cuit existe
    _, user = buscar_usuarios(cuit)
    print('Este es tu usuario')
    imprimir_usuario(user)

def ver_cartilla(cuit):
    print('Esta es tu cartilla')
    indice, user = buscar_usuarios(cuit)
    for i in PLANES:
        if (user['Plan'].split()[0] == i[0]):
            print(i[2])
            break

def modificar_usuario_admin():
    if base_datos.lista_usuarios == []:
        print('La lista de usuarios se encuentra vacia')
        return
    Flag = True
    while Flag:
        print('Indique el CUIT del usuario que desee modificar o ingrese 0 para volver')
        cuit = input('>> ')
        if cuit == '0':
            return
        if auth.validar_cuit(cuit):
            cuit = auth.limpiar_nro(cuit)
            print('Este es el usuario que desea modificar?')
            indice, usuario = buscar_usuarios(cuit)
            if usuario:
                imprimir_usuario(usuario)
            else:
                print('Usuario no encontrado intente nuevamente')
            if not verificar_decision(cuit):
                Flag = False
    modificar = base_datos.lista_usuarios.pop(indice)
    #incompleto, se continua para el 100%

def modificar_user(dic):
    print('Que desea modificar?')
    contador = 0
    for key,item in dic.items():
        contador += 1
        print(f'[{contador}] {key} : {item}')
    #incompleto, se continua para el 100%





