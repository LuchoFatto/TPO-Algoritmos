import re
import auth


#Todos los planes disponibles y sus descripciones (Nombre, Precio Mensual, Descripcion)
Planes = (('Basico',5000,"Covertura del 40%"),('Plus',10000,"Covertura del 65%"),('Familiar',12000,"Covertura del 50% y posibilidad de añadir hasta 2 hijos y 1 conyuge"))



#Lista de todos los usuarios
lista_usuarios = []

#funciones auxiliares
def imprimir_usuario(dic):
    for key,valor in dic.items():
        print('-'*30)
        print(f'| {key} : {valor} |')
    print('-'*30)

def limpiar_nro(nro):
    return int(re.sub(r'[\.\-\s]', "", nro))

def verificar_decision(elemento):
    """Modo de verificar si la decision del usuario fue correcta

    Args:
        elemento any: Solo utilizado para mostrar en texto lo que escribio el usuario

    Returns:
        boolean: False si esta de acuerdo con lo escrito, True si no
    """
    Flag = True
    while Flag:
        print('-=-'*10)
        print(f'Usted ha ingresado {elemento}')
        print(f'Si esta bien ingresado ingrese "1"')
        print(f'Si desea reingresar ingrese "2"')
        dec = input('>> ')
        print('-=-'*10)
        if dec == '1':
            return False
        elif dec == '2':
            return True
        else:
            print('Ingrese una opcion adecuada')
            input('Presione Enter para reintentar')
            print('\n\n')


#funciones para modificar o crear elementos de Usuario
def pedir_nombre(pedir):
    """Ingresar, Validar y Verificar un Nombre, Apellido, etc. Ingresado por el Usuario

    Args:
        pedir (str): Que se le pide al usuario que ingrese

    Returns:
        str: Nombre,Apellido, Etc. validado
    """
    Flag = True
    while Flag:
        nombre = input(f'Ingrese el {pedir}\n>> ')
        if not auth.validacion_letras(nombre):
            print('Ingrese exclusivamente letras')
            input('Ingrese Enter para reintentar')
            print('\n\n')
        else:
            Flag = verificar_decision(nombre)
    return nombre

def pedir_cuit():
    """Ingreso, Validacion y verificacion de CUIT de Usuario

    Returns:
        int: CUIT Validado y no repetido ingresado por el Usuario
    """
    Flag = True
    while Flag:
        cuit = input('Ingrese el CUIT\n>> ')
        if not auth.validar_cuit(cuit):
            print('Ingrese correctamente el CUIT')
            input('Ingrese Enter para reintentar')
            print('\n\n')
        else:
            cuit = limpiar_nro(cuit)
            for i in lista_usuarios:
                if i['CUIT'] == cuit:
                    print('El CUIT ingresado ya existe')
                    input('Ingrese Enter para reintentar')
                    cuit = None
                    break
            if cuit != None:
                Flag = verificar_decision(cuit)
    return cuit

def pedir_telefono():
    """Ingreso, Validacion y verificacion de telefono del Usuario

    Returns:
        int: Telefono Validado
    """
    Flag = True
    while Flag:
        telefono = input('Ingrese el Telefono (Sin el 15 ni 0)\n>> ')
        if not auth.validar_numero_telefono(telefono):
            print('Ingrese correctamente el Telefono')
            input('Ingrese Enter para reintentar')
            print('\n\n')
        else:
            telefono = int(limpiar_nro(telefono))
            Flag = verificar_decision(telefono)
    return telefono

def pedir_email():
    """Ingreso, Validacion y verificacion de Email de Usuario

    Returns:
        str: Email validado de Usuario
    """
    Flag = True
    while Flag:
        email = input('Ingrese el Email\n>> ')
        if not auth.validar_email(email):
            print('Ingrese un Email adecuado')
            input('Ingrese Enter para reintentar')
            print('\n\n')
        else:
            Flag = verificar_decision(email)
    return email

def pedir_password():
    """Ingreso, Validacion y Verificacion de Contraseña

    Returns:
        str: Contraseña Validad de Usuario
    """
    Flag = True
    while Flag:
        password = input('Ingrese su contraseña (Debe tener al menos 8 elementos, uno especial y un numero)\n>> ')
        if not auth.validar_contrasenia(password):
            print('Ingrese un Contraseña adecuada')
            input('Ingrese Enter para reintentar')
            print('\n\n')
        else:
            Flag = verificar_decision(password)
    return password

def pedir_plan():
    """Eleccion de Plan en base a la tupla 'Planes'

    Returns:
        tuple: Con cualquier plan Retorna (Plan elegido, None, None); si eligio familiar dueño (Familiar Dueño, [], None); si elijo
            familiar hijo (Familiar Hijo, None, Cuit de Dueño)
    """
    print('Elija un Plan de Pago')
    Flag = True
    while Flag:

        #Muestra los Planes en pantalla
        Contador = 0
        for i in Planes:
            Contador += 1
            print(f'{Contador}- {i[0]} >> {i[2]} << ${i[1]} x Mes')
        eleccion = int(input('\n--Ingrese el numero de la opcion acorde--\n>> ')) #Falta verificar que sea numero
        if (eleccion > Contador) or (eleccion < 1):
            print('Numero Invalido')
            input('Presione Enter Para reintentar')
            print('\n\n')
        else:
            Flag = False

    plan = Planes[eleccion-1][0]
    familia,CUIT_principal = None,None

    if plan == 'Familiar':
        Flag = True
        while Flag:
            print('Usted ha seleccionado el plan familiar')
            print('Quiere incluirse a un plan existente (No puede haber mas de 3 afiliados + titular en el mismo plan familiar)(Ingrese 1),\nSi desea ser dueño (Ingrese 2)')
            Check = input('>> ')
            if Check == '2':
                plan = 'Familiar Dueño'
                familia = []
                print('Se ha guardado como dueño del plan familiar')
                input('Presione Enter para continuar')
                print('\n')
                CUIT_principal = None
                return plan, familia , CUIT_principal
            elif Check == '1':
                if not (lista_usuarios == []):
                    Valido, Find = True,False
                    while Valido:
                        print('Ingrese el CUIT de la persona a la cual se va a incluir, si quiere volver ingrese 0')
                        CUIT_principal = input('>> ')
                        if CUIT_principal != '0':
                            if auth.validar_cuit(CUIT_principal):
                                CUIT_principal = limpiar_nro(CUIT_principal)
                                for i in lista_usuarios:
                                    if i['CUIT'] == CUIT_principal and (i['Plan'] == 'Familiar Dueño'):
                                        Find = True
                                        if len(i['Familia']) < 3:
                                            plan = 'Familiar Hijo'
                                            return plan, familia , CUIT_principal
                                        else:
                                            print('Se ha encontrado el CUIT indicado pero se encuentra en el maximo de afiliados')
                                            break
                                if not Find:
                                    print('No se ha encontrado ningun afiliado con el plan familiar dueño con ese CUIT')
                            else:
                                print('Ingrese un CUIT valido')
                                print('\n')
                        else:
                            Valido = False
                    input('Presione Enter para volver')
                    print('\n')
                else:
                    print('No hay usuarios afiliados aun, elija ser dueño')

            else:
                print('Ingrese uno de los valores indicados')
                print('Revise los datos, si esta todo correcto ingrese 1, sino ingrese 0 y vuelva a intentar')
                print('\n')
    else:
        return plan, familia, CUIT_principal




def alta_usuario():
    """
        Creacion de Usuario, Verificacion de Datos Ingresados y posibilidad de reincio de ingreso
    """

    Reinicio = True

    while Reinicio:
        print('-'*50)
        #Ingreso de Nombre de Usuario
        Nombre = pedir_nombre('Nombre')
        print('-'*50)

        #Ingreso de Apellido de Usuario
        Apellido = pedir_nombre('Apellido')
        print('-'*50)

        #Ingreso de CUIT de Usuario
        CUIT = pedir_cuit()
        print('-'*50)

        #Ingreso de Telefono de Usuario
        Telefono = pedir_telefono()
        print('-'*50)

        #Ingreso de Email de Usuario
        Email = pedir_email()
        print('-'*50)

        #Ingreso Plan de Usuario
        Plan, familia, cuit_principal = pedir_plan()
        print('-'*50)

        #Ingreso de Contraseña de Usuario
        Password = pedir_password()
        print('-'*50)


        diccionario_usuario = {
            'Nombre': Nombre,
            'Apellido': Apellido,
            'CUIT': CUIT,
            'Telefono': Telefono,
            'Email': Email,
            'Plan': Plan,
            'Password': Password,
            'Historial': [],
            'Deudor' : True
        }

        if familia != None:
            diccionario_usuario['Familia'] = familia
        elif cuit_principal != None:
            diccionario_usuario['Dueño'] = cuit_principal

        print('\n\n')
        imprimir_usuario(diccionario_usuario)
        print('\n')
        print('Revise los datos, si desea salir sin cargar ingrese 2\nSi desea volver a intentar ingrese 1\nSi esta todo correcto ingrese 0') #Posible recursividad en el futuro
        Check,Flag = True,True
        while Flag:
            Check = input('>> ')
            if Check == '2':
                return
            if Check == '0':
                if cuit_principal != None:
                    for i in lista_usuarios:
                        if i['CUIT'] == cuit_principal:
                            i['Familia'].append(diccionario_usuario['CUIT'])
                            break
                lista_usuarios.append(diccionario_usuario)
                print('Usuario ingresado con exito')
                print('Comuniquese con un encargado de la empresa para cancelar su deuda, al nro 11-22334455')
                input('Presione Enter para volver al menu anterior')
                print('\n')
                Flag,Reinicio = False,False
            elif Check == '1':
                print('Reiniciando proceso de carga')
                input('Presione Enter para seguir')
                print('\n')
                Flag = False
            else:
                print('Ingrese uno de los valores indicados')
                print('Revise los datos, si esta todo correcto ingrese 1, sino ingrese 0 y vuelva a intentar')
                print('\n')




def buscar_usuarios(cuit):
    for indice, usuario in enumerate(lista_usuarios):
        if usuario['CUIT'] == cuit:
            return indice, usuario
    return None, None

def ver_lista_usuarios():
    for i in lista_usuarios:
        imprimir_usuario(i)


def modificar_usuario_admin():
    if lista_usuarios == []:
        print('La lista de usuarios se encuentra vacia')
        return
    Flag = True
    while Flag:
        print('Indique el CUIT del usuario que desee modificar o ingrese 0 para volver')
        cuit = input('>> ')
        if cuit == '0':
            return
        if auth.validar_cuit(cuit):
            cuit = limpiar_nro(cuit)
            print('Este es el usuario que desea modificar?')
            indice, usuario = buscar_usuarios(cuit)
            if usuario:
                imprimir_usuario(usuario)
            else:
                print('Usuario no encontrado intente nuevamente')
            if not verificar_decision(cuit):
                Flag = False
    modificar = lista_usuarios.pop(indice)
    #incompleto, se continua para el 100%


def modificar_user(dic):
    print('Que desea modificar?')
    contador = 0
    for key,item in dic.items():
        contador += 1
        print(f'[{contador}] {key} : {item}')
    #incompleto, se continua para el 100%

def ver_mi_perfil_user(cuit): #asumo que el cuit existe
    _, user = buscar_usuarios(cuit)
    print('Este es tu usuario')
    imprimir_usuario(user)

def baja_usuario(cuit):
    if not verificar_decision('Darse de Baja'):
        eliminar_usuario(cuit)
    else:
        print('Volviendo al menu anterior')

def eliminar_usuario(cuit):
    indice, usuario = buscar_usuarios(cuit)
    if usuario:
        lista_usuarios.pop(indice)
        print('Usuario Eliminado')
        input('Presione Enter para volver')
    else:
        print('El usuario ingresado no existe')
        input('Presione Enter para volver')
