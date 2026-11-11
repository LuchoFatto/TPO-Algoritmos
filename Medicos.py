import validaciones
import usuarios
import json
import re
import auth
import base_datos

# Afiliados / médicos
def alta_medico():

    medico_nombre = validaciones.bucle_medico("Ingrese su nombre: ", "SOLO LETRAS - Ingrese su nombre: ", validaciones.validador_solo_letras) #verifica solo letras sin limite de caracteres

    medico_apellido = validaciones.bucle_medico("ingrse su apellido: ", "SOLO LETRAS - Ingrese su apellido: ", validaciones.validador_solo_letras)

    medico_cuit = validar_cuit_medicos()

    medico_matricula = input("Ingrese su NRO de matricula: ")
    flag_matricula = validaciones.validador_solo_numeros(medico_matricula)
    while flag_matricula == False:
        medico_matricula = input("SOLO NUMEROS SIN GUIONES - Ingrese su NRO de matricula: ")
        flag_matricula = validaciones.validador_solo_numeros(medico_matricula)

    medico_email = input("Ingrese su email: ")
    flag_email = validaciones.validar_email(medico_email)
    while flag_email == False:
        medico_email = input("ERROR - Ingrese su email correctamente: ")
        flag_email = validaciones.validar_email(medico_email)

    medico_contraseña = input("Contraseña: ")
    flag_contraseña = validaciones.validador_solo_numeros(medico_contraseña)
    while flag_contraseña == False:
        medico_contraseña = input("ERROR: ingrese una contraseña de solo numero: ")
        flag_contraseña = validaciones.validador_solo_numeros(medico_contraseña)

    medico = {
        "nombre":medico_nombre,
        "apellido":medico_apellido,
        "CUIT":medico_cuit, 
        "email":medico_email,
        "matricula":medico_matricula,
        "contraseña":medico_contraseña,
        "estado_socio": 1
        }
    
    print(medico)
    return(medico)

    #usuarios.append({"nombre":medico_nombre, "apellido":medico_apellido, "cuit":medico_cuit, "email":medico_email,"matricula":medico_matricula, "contraseña":medico_contraseña})
    #imprimir_lista_medicos(usuarios)

def generarArchivo(medico, ruta_archivo):
    print("""Agregar un médico al archivo JSON""")

    try:
        # Intentar leer los médicos existentes
        try:
            with open(ruta_archivo, "r", encoding="utf-8") as archivo:
                medicos = json.load(archivo)

        except FileNotFoundError:
            medicos = []

        # Agregar el nuevo diccionario a la lista
        medicos.append(medico)

        # Guardar la lista actualizada
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            json.dump(medicos, archivo, indent=4, ensure_ascii=False)

        print("Médico agregado con éxito")

    except Exception as e:
        print(e)


def validar_cuit_medicos():
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
            cuit = usuarios.limpiar_nro(cuit)
            for i in base_datos.lista_usuarios:
                if i['CUIT'] == cuit:
                    print('El CUIT ingresado ya existe')
                    input('Ingrese Enter para reintentar')
                    cuit = None
                    break
            if cuit != None:
                Flag = usuarios.verificar_decision(cuit)
    return cuit

def modificar_medico(usuarios):
    matricula_medico_eliminar = input("Para modificar un medico ingrese el numero de matricula: ")
    flag = None
    for user in usuarios:
        if user["rol"] == "medico" and user["matricula"] == str(matricula_medico_eliminar):
            opcion = input("que desea modificar: 1) mail - 2) contraseña")
            if opcion == "1":
                user["email"] = input("Ingrese el nuevo Email del Medico/a: ")#agregar validacion de email y letras
                flag_email = validaciones.validar_email(user["email"])
                while flag_email == False:
                    user["email"] = input("Ingrese su mail correctamente: ")
                    flag_email = validaciones.validar_email(user["email"])


def eliminar_medico(usuarios):
    print(usuarios)
    cuit_medico_eliminar = input("Para darse de baja ingrese su NUMERO de CUIT: ")
    for user in usuarios:
        if user["cuit"] == int(cuit_medico_eliminar):
            confirmacion = input("Confirmacion, desea eliminar? SI/NO:  ") #hay que agregar que preguntar para confirmar
            if confirmacion == "SI":
                user["estado_socio"] = 0
                #usuarios.remove(user) Cambiamos el estado de 1 a 0 para no perder el dato del cliente
            else:
                pass #se vuelve al menu donde se eligio eliminar medico
            

def imprimir_lista_medicos(usuarios):
    for user in usuarios:        
        print("\nNombre: {0}".format(user["nombre"],))
        print("Apellido: {0}".format(user["apellido"]))
        print("CUIT: {0}".format(user["cuit"]))
        print("Email: {0}".format(user["email"]))
        print("Matricula: {0}".format(user["matricula"]))
        print("Contraseña: {0}".format(user["contraseña"]))
        print("Estado del Socio: {0}".format(user["estado_socio"]))