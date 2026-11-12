import re
import auth
import time
import os
import json

from colorama import Fore, Style, init
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)

consola = Console()

#Todos los planes disponibles y sus descripciones (Nombre, Precio Mensual, Descripcion)
PLANES = (
        ('Basico',5000,"Covertura del 40%"),
        ('Plus',10000,"Covertura del 65%"),
        ('Familiar',12000,"Covertura del 50% y posibilidad de añadir hasta 2 hijos y 1 conyuge")
)

RUTA_ARCHIVO = os.path.join(os.path.dirname(__file__),"lista_usuarios.json")


#funciones auxiliares
def imprimir_usuario(dic:dict):
    """Imprime los datos visibles del usuario, omitiendo su contraseña.

    Args:
        dic (dict): usuario a imprimir
    """
    for key, valor in dic.items():
        if key.lower() in ('password', 'contraseña'):
            continue

        print('-'*30)
        print(Fore.YELLOW + f'| {key} : {valor} |')
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
        print(Fore.YELLOW + f'Usted ha ingresado {elemento}')
        esperar()
        print(Fore.YELLOW + f'Si esta bien ingresado ingrese "1"')
        esperar()
        print(Fore.YELLOW + f'Si desea reingresar ingrese "2"')
        esperar()
        dec = input('>> ')
        match dec:
            case '1':
                esperar(1)
                os.system('cls')
                return False
            case '2':
                esperar(1)
                os.system('cls')
                return True
            case _:
                print(Fore.YELLOW + 'Ingrese una opcion adecuada')
                input(Fore.YELLOW + 'Presione Enter para reintentar')
                os.system('cls')


#funciones para modificar o crear elementos de Usuario
def pedido_datos(mensaje:str, funcion_auth, mensaje_error:str, lista_u, transformar = False, es_cuit = False):
    """Funcion Generalizada para carga de datos de usuario

    Args:
        mensaje (str): Mensaje a mostrar
        funcion_auth (funcion): Funcion autenticadora
        mensaje_error (str): Mensaje de error a mostrar si falla la funcion'
        lista_u (list): Lista de diccionarios del archivo json
        transformar (bool, optional): Si debe ejecutar "limpiar_nro" o no. Defaults to False.
        es_cuit (bool, optional): Si debe verificar si el cuit existe en la DB. Defaults to False.

    Returns:
        str | int: Devuelve el valor pedido validado y verificado
    """
    Flag = True

    while Flag:
        esperar()
        dato = input(Fore.YELLOW + f'{mensaje}\n>> ')
        esperar()

        if not funcion_auth(dato):
            print(Fore.YELLOW + mensaje_error)
            esperar()
            input(Fore.YELLOW + 'Presione Enter para reintentar')
            os.system('cls')
        else:

            if transformar:
                dato = auth.limpiar_nro(dato)

            if es_cuit:
                lista_u = auth.abrir_archivo(RUTA_ARCHIVO)
                if lista_u == None:
                    esperar()
                    continue
                cuit_duplicado = False
                for i in lista_u:
                    if i['CUIT'] == dato:
                        cuit_duplicado = True
                        break

                if cuit_duplicado:
                    print(Fore.YELLOW + 'El CUIT ingresado ya existe')
                    esperar()
                    input(Fore.YELLOW + 'Ingrese Enter para reintentar')
                    os.system('cls')
                    continue

            if not verificar_decision(dato):
                return dato

def elegir_plan():
    """Imprime las posibles elecciones y permite eleccion, para devolver la elegida

    Returns:
        str: Nombre del plan elegido
    """
    while True:
        print(Fore.YELLOW + 'Elija un Plan de Pago')
        for numero, plan in enumerate(PLANES, start=1):
            print(Fore.YELLOW + f'[{numero}] {plan[0]} >> {plan[2]} << ${plan[1]} x Mes')

        try:
            eleccion = int(input(Fore.YELLOW + '\n--Ingrese el numero de la opcion acorde--\n>> '))
        except ValueError:
            print(Fore.YELLOW + 'Ingrese un numero valido')
            input(Fore.YELLOW + 'Presione Enter para reintentar')
            os.system('cls')
            continue

        if eleccion < 1 or eleccion > len(PLANES):
            print(Fore.YELLOW + 'Numero invalido')
            input(Fore.YELLOW + 'Presione Enter para reintentar')
            os.system('cls')
            continue

        return PLANES[eleccion - 1][0]

def pedir_password():
    """Ingreso, Validacion y Verificacion de Contraseña

    Returns:
        str: Contraseña Validad de Usuario
    """
    Flag = True
    while Flag:
        password = input(Fore.YELLOW + 'Ingrese su contraseña (Debe tener al menos 8 elementos, uno especial y un numero)\n>> ')
        if not auth.validar_contrasenia(password):
            print(Fore.YELLOW + 'Ingrese un Contraseña adecuada')
            input(Fore.YELLOW + 'Ingrese Enter para reintentar')
            print('\n\n')
        else:
            Flag = verificar_decision(password)
    return password

def incluirse_plan_familiar(cuit, lista_u):
    """Verifica si el CUIT del dueño es correcto, existe y tiene espacio.
    Si cumple, devuelve los datos necesarios para asociar el nuevo usuario
    cuando se confirme el alta.

    Args:
        cuit (str): Cuit del usuario ingresando
        lista_u (list): Lista de diccionarios del archivo json

    Returns:
        Dict: Diccionario de hijo completo
        None: Si no se completa el ingreso
    """
    #Validar que exista algun usuario en la DB
    if (lista_u == []):
        print(Fore.YELLOW + 'No hay usuarios afiliados aun, elija otra opcion')
    else:
        Valido = True
        while Valido:
            print(Fore.YELLOW + 'Ingrese el CUIT de la persona a la cual se va a incluir, si quiere volver ingrese 0')
            CUIT_principal = input('>> ')

            #Salir del Case, Volver a elegir
            if CUIT_principal == '0':
                Valido = False

            #Validar que sea CUIT
            elif not auth.validar_cuit(CUIT_principal):
                print(Fore.YELLOW + 'Ingrese un CUIT valido')
                esperar()
                input(Fore.YELLOW + 'Presione Enter para reintentar')
                os.system('cls')

            else:
                CUIT_principal = auth.limpiar_nro(CUIT_principal)
                #Buscamos el dueño al que se quiere incluir
                for i in lista_u:
                    if i['CUIT'] == CUIT_principal and (i['Plan'] == 'Familiar Dueño'):

                        #Si esta lleno, no lo añade
                        if len(i['Familia']) >= 3:
                            print(Fore.YELLOW + 'Se ha encontrado el CUIT indicado pero se encuentra en el maximo de afiliados')
                            esperar()
                            input(Fore.YELLOW + 'Presione Enter para reintentar')
                            os.system('cls')
                            break

                        # Se agrega al dueño cuando el nuevo usuario confirma el alta.
                        else:
                            return {
                                    'Plan': 'Familiar Hijo',
                                    'Dueño': CUIT_principal
                                }

                print(Fore.YELLOW + 'No se ha encontrado ningun afiliado con el plan familiar dueño con ese CUIT')

    input(Fore.YELLOW + 'Presione Enter para volver')
    os.system('cls')
    return None

def plan_familiar(cuit, lista_u):
    """Eleccion de tipo de plan familiar, devolucion de diccionario con datos en base a eleccion

    Args:
        cuit (str): cuit de usuario ingresando
        lista_u (list): Lista de diccionarios del archivo json

    Returns:
        Dict: Diccionario con keys a añadir a diccionario base
    """
    Flag = True
    print(Fore.YELLOW + 'Usted ha seleccionado el plan familiar')
    esperar()
    while Flag:
        print(Fore.YELLOW + '[1] Incluirse a un Plan existente\n !!No puede haber mas de 3 afiliados + titular en el mismo plan familiar!!')
        esperar()
        print(Fore.YELLOW + '[2] Ser Dueño principal')
        esperar()
        Check = input('>> ')

        match Check:
            case '2':
                print(Fore.YELLOW + 'Se ha guardado como dueño del plan familiar')
                esperar()
                input(Fore.YELLOW + 'Presione Enter para continuar')
                os.system('cls')
                return {
                    'Plan': 'Familiar Dueño',
                    'Familia':[]
                }


            case '1':
                hijo = incluirse_plan_familiar(cuit, lista_u)
                if hijo:
                    return hijo

            case _:
                print(Fore.YELLOW + 'Ingrese uno de los valores indicados')
                esperar()
                os.system('cls')

def pedir_plan(cuit, lista_u):
    """Eleccion de plan y sus opciones

    Args:
        cuit (str): Cuit del usuario ingresando
        lista_u (list): Lista de diccionarios del archivo json

    Returns:
        Dict: Diccionario con keys a añadir a diccionario base
    """

    plan = {
        'Plan' : elegir_plan()
    }

    if plan['Plan'] == 'Familiar':
        plan.update(plan_familiar(cuit, lista_u))

    return plan



def alta_usuario():
    """
        Creacion de Usuario, Verificacion de Datos Ingresados y posibilidad de reincio de ingreso
    """

    Reinicio = True

    lista_u = auth.abrir_archivo(RUTA_ARCHIVO)

    while Reinicio:
        diccionario_usuario = {

        #Ingreso de Nombre de Usuario
        'Nombre': pedido_datos('Ingrese el nombre', auth.validacion_letras, 'Ingrese exclusivamente letras', lista_u),

        #Ingreso de Apellido de Usuario
        'Apellido' : pedido_datos('Ingrese el apellido', auth.validacion_letras, 'Ingrese exclusivamente letras', lista_u),

        #Ingreso de CUIT de Usuario
        'CUIT' : pedido_datos('Ingrese el CUIT', auth.validar_cuit, 'Ingrese correctamente el CUIT', lista_u, True, True),

        #Ingreso de Telefono de Usuario
        'Telefono' : pedido_datos('Ingrese el Telefono (Sin el 15 ni 0)', auth.validar_numero_telefono, 'Ingrese correctamente el Telefono', lista_u,True),

        #Ingreso de Email de Usuario
        'Email' : pedido_datos('Ingrese el E-Mail', auth.validar_email, 'Ingrese un Email Valido', lista_u),

        #Ingreso de Contraseña de Usuario
        'Password' : pedido_datos('Ingrese su contraseña (Debe tener al menos 8 elementos, uno especial y un numero)',auth.validar_contrasenia,'Ingrese un Contraseña adecuada', lista_u),

        'Historial': [],

        'Deudor' : True,

        'Activo' : True
        }

        #Ingreso Plan de Usuario
        diccionario_usuario.update(pedir_plan(diccionario_usuario['CUIT'], lista_u))



        Check,Flag = True,True
        while Flag:
            print('\n')
            imprimir_usuario(diccionario_usuario)
            print('\n')
            print(Fore.YELLOW + 'Revise los datos, si desea:') #Posible recursividad en el futuro
            esperar()
            print(Fore.GREEN + '[1] Volver a Reingresar')
            esperar()
            print(Fore.RED + '[2] Salir sin cargar')
            esperar()
            print(Fore.YELLOW + '[0] Todo correcto, continuar')
            Check = input('>> ')
            match Check:
                #Salir SIN CARGAR
                case '2':
                    return

                #Reingreso de datos
                case '1':
                    print(Fore.YELLOW + 'Reiniciando proceso de carga...')
                    esperar(2)
                    input(Fore.YELLOW + 'Presione Enter para seguir')
                    print('\n')
                    Flag = False


                #Todo correcto, carga de datos
                case '0':
                    if 'Dueño' in diccionario_usuario:
                        for i in lista_u:
                            if i['CUIT'] == diccionario_usuario['Dueño']:
                                i['Familia'].append(diccionario_usuario['CUIT'])
                                break
                    lista_u.append(diccionario_usuario)
                    print(Fore.YELLOW + 'Usuario ingresado con exito')
                    esperar()
                    print(Fore.YELLOW + 'Comuniquese con un encargado de la empresa para cancelar su deuda, al nro 11-22334455')
                    esperar()
                    input(Fore.YELLOW + 'Presione Enter para volver al menu anterior')
                    os.system('cls')
                    auth.cargar_archivo(lista_u,RUTA_ARCHIVO)
                    Flag,Reinicio = False,False

                case _:
                    print(Fore.YELLOW + 'Ingrese uno de los valores indicados')
                    esperar()
                    input(Fore.YELLOW + 'Ingrese Enter para reintentar')
                    os.system('cls')

def baja_usuario(cuit):
    """Usuario se da de baja
    Args:
        cuit (int): Cuit del usuario
    """
    if not verificar_decision('Darse de Baja'):
        eliminar_usuario(cuit)
    else:
        print(Fore.YELLOW + 'Volviendo al menu anterior')

def eliminar_usuario(cuit):
    """Cambia el estado del usuario de Activo = True a False

    Args:
        cuit (int): Cuit del usuario a inhabilitar
    """
    lista_u = auth.abrir_archivo(RUTA_ARCHIVO)
    indice, usuario = buscar_usuarios(cuit, True)

    if usuario is None:
        print(Fore.YELLOW + 'El usuario ingresado no existe')
        esperar()
        input(Fore.YELLOW + 'Presione Enter para volver')
        os.system('cls')

    elif usuario['Activo'] is True:
        print(Fore.YELLOW + 'Eliminando usuario...')
        esperar(2)
        lista_u[indice]['Activo'] = False
        print(Fore.YELLOW + 'Usuario Eliminado')
        esperar()
        input(Fore.YELLOW + 'Presione Enter para volver')
        os.system('cls')
        auth.cargar_archivo(lista_u,RUTA_ARCHIVO)

    elif usuario['Activo'] is False:
        print(Fore.YELLOW + 'El usuario ingresado ya esa inhabilitado')
        esperar()
        input(Fore.YELLOW + 'Presione Enter para volver')
        esperar()
        os.system('cls')


def buscar_usuarios(cuit,admin=False):
    """Busqueda de usuario en archivo

    Args:
        cuit (int): Cuit del usuario a buscar
        admin (bool, optional): Verifica si el que busca es admin, para saber si incluir o no los inactivos. Defaults to False.

    Returns:
        tuple: (ubicacion en lista, diccionario del usuario) | (None, None)
    """
    with open(RUTA_ARCHIVO,"r") as Archivo:
        lista_u = json.load(Archivo)
    if admin:
        for indice, usuario in enumerate(lista_u):
            if (usuario['CUIT'] == auth.limpiar_nro(cuit)):
                return indice, usuario
    else:
        for indice, usuario in enumerate(lista_u):
            if (usuario['CUIT'] == auth.limpiar_nro(cuit)) and (usuario['Activo']):
                return indice, usuario
    return None, None

def ver_lista_usuarios():
    """Vista de la lista completa del archivo usuarios
    """
    for i in auth.abrir_archivo(RUTA_ARCHIVO):
        imprimir_usuario(i)

def ver_mi_perfil_user(cuit):
    """Vista de perfil propio del usuario

    Args:
        cuit (int): Cuit del usuario ingresado
    """
    _, usuario_encontrado = buscar_usuarios(cuit)
    if usuario_encontrado is None:
        print(Fore.YELLOW + 'No se encontro un usuario activo con ese CUIT')
        return

    print(Fore.YELLOW + 'Este es tu usuario')
    esperar()
    imprimir_usuario(usuario_encontrado)

def ver_beneficios(cuit):
    """Vista de beneficios del plan elegido por usuario

    Args:
        cuit (int): Cuit del usuario
    """
    esperar()
    print('-+-'*15)
    print(Fore.YELLOW + 'Estos son tus beneficios')
    esperar()
    _, usuario_encontrado = buscar_usuarios(cuit)
    if usuario_encontrado is None:
        print(Fore.YELLOW + 'No se encontraron beneficios porque el usuario no existe o esta inactivo')
        print('-+-'*15)
        return

    beneficios_encontrados = False
    for plan_disponible in PLANES:
        if usuario_encontrado['Plan'].split()[0] == plan_disponible[0]:
            print(plan_disponible[2])
            esperar()
            beneficios_encontrados = True
            break

    if not beneficios_encontrados:
        print(Fore.YELLOW + 'No se encontraron beneficios para el plan asignado')
    print('-+-'*15)

def validar_busqueda_usuario(lista_u):
    """Valida que la lista no este vacia, el cuit sea valido y lo encuentre, devuelve el indice

    Args:
        lista_u (_type_): lista de usuarios del json

    Returns:
        int: indice del usuario buscado
    """
    if lista_u == []:
        print(Fore.YELLOW + 'La lista de usuarios se encuentra vacia')
        esperar()
        input(Fore.YELLOW + 'Presione Enter para volver')
        esperar()
        os.system('cls')
        return None
    Flag = True
    while Flag:
        print(Fore.YELLOW + 'Indique el CUIT del usuario que desee modificar o ingrese 0 para volver')
        cuit = input('>> ')
        if cuit == '0':
            return None
        if not auth.validar_cuit(cuit):
            print(Fore.YELLOW + 'CUIT ingresado es invalido')
        else:
            cuit = auth.limpiar_nro(cuit)
            indice, usuario = buscar_usuarios(cuit,True)
            if usuario == None:
                print(Fore.YELLOW + 'Usuario no encontrado intente nuevamente')
                esperar()
                input(Fore.YELLOW + 'Presione Enter para volver')
                esperar()
                os.system('cls')
            else:
                print(Fore.YELLOW + 'Este es el usuario que desea modificar?')
                esperar()
                imprimir_usuario(usuario)
                esperar()
                if not verificar_decision(cuit):
                    os.system('cls')
                    return indice

def es_plan_familiar(plan_usuario):
    """Indica si el nombre del plan pertenece a una modalidad familiar."""
    return plan_usuario.split()[0] == 'Familiar'

def es_titular_plan_familiar(plan_usuario):
    """Indica si el usuario es titular de un plan familiar."""
    return es_plan_familiar(plan_usuario) and 'Hijo' not in plan_usuario

def quitar_integrante_de_plan_familiar(usuario, lista_u):
    """Desvincula un usuario hijo de su titular familiar."""
    cuit_titular = usuario.get('Dueño')

    if cuit_titular is not None:
        for posible_titular in lista_u:
            if posible_titular['CUIT'] == cuit_titular:
                familia_titular = posible_titular.get('Familia', [])
                if usuario['CUIT'] in familia_titular:
                    familia_titular.remove(usuario['CUIT'])
                break

    usuario.pop('Dueño', None)

def convertir_integrantes_a_plan_individual(usuario, lista_u):
    """Desvincula a los integrantes cuando el titular abandona su plan."""
    integrantes = usuario.get('Familia', [])

    for cuit_integrante in integrantes:
        for posible_integrante in lista_u:
            if posible_integrante['CUIT'] == cuit_integrante:
                posible_integrante['Plan'] = 'Basico'
                posible_integrante.pop('Dueño', None)
                break

    usuario['Familia'] = []

def modificar_plan_usuario(usuario, lista_u):
    """Cambia el plan y actualiza las relaciones familiares involucradas."""
    plan_anterior = usuario['Plan']
    plan_seleccionado = elegir_plan()

    if plan_seleccionado == 'Familiar':
        if es_plan_familiar(plan_anterior):
            print(Fore.YELLOW + 'El usuario ya pertenece a un plan familiar')
            return

        datos_plan_familiar = plan_familiar(usuario['CUIT'], lista_u)
        usuario.update(datos_plan_familiar)

        if 'Dueño' in datos_plan_familiar:
            for posible_titular in lista_u:
                if posible_titular['CUIT'] == datos_plan_familiar['Dueño']:
                    posible_titular.setdefault('Familia', []).append(usuario['CUIT'])
                    break
        return

    if es_titular_plan_familiar(plan_anterior):
        convertir_integrantes_a_plan_individual(usuario, lista_u)
    elif es_plan_familiar(plan_anterior):
        quitar_integrante_de_plan_familiar(usuario, lista_u)

    usuario['Plan'] = plan_seleccionado

def modificar_usuario(admin=False):
    """Eleccion de que usuario y que key modificar

    Args:
        admin (bool, optional): _description_. Defaults to False.
    """
    lista_u = auth.abrir_archivo(RUTA_ARCHIVO)
    indice = validar_busqueda_usuario(lista_u)
    if indice is None:
        return

    Flag = True
    while Flag:
        modificar = lista_u[indice]
        print('^-^'*15)
        esperar()
        imprimir_usuario(modificar)
        print('^-^'*15)
        esperar()
        if admin:
            key = elegir_key(modificar,True)
        else:
            key = elegir_key(modificar)
        match key:
            case 'Nombre':
                modificar[key] = pedido_datos('Ingrese el nombre', auth.validacion_letras, 'Ingrese exclusivamente letras', lista_u)
            case 'Apellido':
                modificar[key] = pedido_datos('Ingrese el apellido', auth.validacion_letras, 'Ingrese exclusivamente letras', lista_u)
            case 'CUIT':
                modificar[key] = pedido_datos('Ingrese el CUIT', auth.validar_cuit, 'Ingrese correctamente el CUIT', lista_u, True, True)
            case 'Telefono':
                modificar[key] = pedido_datos('Ingrese el Telefono (Sin el 15 ni 0)', auth.validar_numero_telefono, 'Ingrese correctamente el Telefono', lista_u,True)
            case 'Email':
                modificar[key] = pedido_datos('Ingrese el E-Mail', auth.validar_email, 'Ingrese un Email Valido', lista_u)
            case 'Password':
                modificar[key] = pedido_datos('Ingrese su contraseña (Debe tener al menos 8 elementos, uno especial y un numero)',auth.validar_contrasenia,'Ingrese un Contraseña adecuada', lista_u)
            case 'Plan':
                modificar_plan_usuario(modificar, lista_u)
            case 'Deudor' | 'Activo':
                print(Fore.YELLOW + f'{key} modificado a estado {not modificar[key]}')
                esperar()
                modificar[key] = not modificar[key]

        if not verificar_decision((Fore.YELLOW + f'la modificacion de {key}. Desea modificar otro dato?')):
            Flag = False

        os.system('cls')

    print(Fore.YELLOW + 'Cargando cambios..')
    esperar(2)
    auth.cargar_archivo(lista_u,RUTA_ARCHIVO)
    esperar(1)
    print(Fore.YELLOW + 'Datos cambiados correctamente')
    input(Fore.YELLOW + 'Ingrese Enter para regresar')
    os.system('cls')


def elegir_key(dic,admin=False):
    """Eleccion de que key del diccionario usuario modificar. Varia si sos admin o no

    Args:
        dic (dict): Diccionario del usuario a modificar
        admin (bool, optional): Verificar si es admin o no. Defaults to False.

    Returns:
        str: key elegida a modificar
    """
    campos_no_modificables = {'Historial', 'Familia', 'Dueño'}
    lista_keys = [key for key in dic.keys() if key not in campos_no_modificables]
    if admin:
        for indice, clave_usuario in enumerate(lista_keys):
            valor_actual = '********' if clave_usuario.lower() in ('password', 'contraseña') else dic[clave_usuario]
            print(Fore.YELLOW + f'[{indice+1}] {clave_usuario} | Valor actual {valor_actual}')
            esperar()
        print(Fore.YELLOW + 'Ingrese la caracteristica a modificar')
        esperar()
        Flag = True
        while Flag:
            try:
                eleccion = int(input('>> '))-1
                if 0 <= eleccion < len(lista_keys):
                    return lista_keys[eleccion]
                else:
                    print(Fore.YELLOW + 'Elija una opcion dentro del rango dado')
                    esperar()
                    input(Fore.YELLOW + 'Presione Enter para reintentar')
                    os.system('cls')
            except Exception as a:
                print(Fore.YELLOW + f'Error {a}, Ingrese nuevamente')
                esperar()
                input(Fore.YELLOW + 'Presione Enter para reintentar')
                os.system('cls')
    else:
        no_admin = {'CUIT', 'Deudor', 'Activo'}
        lista_keys = [key for key in lista_keys if key not in no_admin]
        for indice, clave_usuario in enumerate(lista_keys):
            valor_actual = '********' if clave_usuario.lower() in ('password', 'contraseña') else dic[clave_usuario]
            print(Fore.YELLOW + f'[{indice+1}] {clave_usuario} | Valor actual {valor_actual}')
            esperar()
        print(Fore.YELLOW + 'Ingrese la caracteristica a modificar')
        esperar()
        Flag = True
        while Flag:
            try:
                eleccion = int(input('>> '))-1
                if 0 <= eleccion < len(lista_keys):
                    return lista_keys[eleccion]
                else:
                    print(Fore.YELLOW + 'Elija una opcion dentro del rango dado')
                    esperar()
                    input(Fore.YELLOW + 'Presione Enter para reintentar')
                    os.system('cls')
            except Exception as a:
                print(Fore.YELLOW + f'Error {a}, Ingrese nuevamente')
                esperar()
                input(Fore.YELLOW + 'Presione Enter para reintentar')
                os.system('cls')






def iniciar_sesion_usuario():
    """Inicio de sesion del usuario

    Returns:
        int or None: Si es inicio de sesion valido retorna el cuit, sino None
    """
    print()
    print("===================================")
    consola.print(Panel("   INICIAR SESION", border_style= "green", width=44))
    print("===================================")

    lista_usuarios = auth.abrir_archivo(RUTA_ARCHIVO)

    cuit = input(Fore.YELLOW + "Ingrese su CUIT: ")

    if not auth.validar_cuit(cuit):
        print(Fore.YELLOW + "CUIT invalido")
        esperar()
        os.system('cls')
        return None

    cuit = auth.limpiar_nro(cuit)

    usuario_encontrado = None

    for usuario in lista_usuarios:
        if usuario["CUIT"] == cuit:
            usuario_encontrado = usuario
            break

    if usuario_encontrado == None or usuario_encontrado['Activo']==False:
        print(Fore.YELLOW + "Usuario no encontrado")
        return None

    usuario = check_pasword(usuario_encontrado,3)
    if usuario is not None:
        return(usuario_encontrado['CUIT'])
    else:
        return None



def check_pasword(user,intentos):
    """Funcion recursiva de intentos de ingreso de contrasena

    Args:
        user (dict): Diccionario usuario
        intentos (int): Intentos restantes de ingreso

    Returns:
        Dict or None: Si inicia correctamente devuelve el Diccionario, sino None
    """
    if intentos <= 0:
        print(Fore.YELLOW + "Se agotaron los intentos")
        esperar()
        input(Fore.YELLOW + 'Ingrese Enter para regresar')
        os.system('cls')
        return None

    password = input(Fore.YELLOW + "Ingrese su contraseña: ")
    esperar()

    if password == user["Password"]:

        if user["Deudor"] == True:
            print(Fore.YELLOW + "No puede iniciar sesion porque posee una deuda.")
            esperar()
            print(Fore.YELLOW + "Debe regularizar su situacion.")
            esperar()
            input(Fore.YELLOW + 'Ingrese Enter para regresar')
            os.system('cls')
            return None

        print(Fore.YELLOW + "Inicio de sesion exitoso")
        esperar()
        print(Fore.YELLOW + "Bienvenido/a", user["Apellido"])
        esperar()

        return user

    else:
        intentos -= 1
        print(Fore.YELLOW + "Contraseña incorrecta")
        esperar()
        print(Fore.YELLOW + "Intentos restantes:", intentos)
        esperar()
        os.system('cls')
        return check_pasword(user,intentos)

