import validaciones

from colorama import Fore, Style, init
from tabulate import tabulate
from rich.console import Console
from rich.panel import Panel

init(autoreset=True)

consola = Console()


# Afiliados / médicos
def alta_medico(usuarios):

    medico_nombre = validaciones.bucle_medico(Fore.YELLOW + "Ingrese su nombre: ", "SOLO LETRAS - Ingrese su nombre: ", validaciones.validador_solo_letras) #verifica solo letras sin limite de caracteres

    medico_apellido = validaciones.bucle_medico(Fore.YELLOW + "ingrse su apellido: ", "SOLO LETRAS - Ingrese su apellido: ", validaciones.validador_solo_letras)

    medico_cuit = input(Fore.YELLOW + "Ingrese su NRO de CUIT: ")
    flag_cuit = validaciones.validador_solo_numeros(medico_cuit)
    while flag_cuit == False:
        medico_cuit = input(Fore.YELLOW + "SOLO NUMEROS SIN GUIONES - CUIT: ")
        flag_cuit = validaciones.validador_solo_numeros(medico_cuit)

    medico_matricula = input(Fore.YELLOW + "Ingrese su NRO de matricula: ")
    flag_matricula = validaciones.validador_solo_numeros(medico_matricula)
    while flag_matricula == False:
        medico_matricula = input(Fore.YELLOW + "SOLO NUMEROS SIN GUIONES - Ingrese su NRO de matricula: ")
        flag_matricula = validaciones.validador_solo_numeros(medico_matricula)

    medico_email = input(Fore.YELLOW + "Ingrese su email: ")
    flag_email = validaciones.validar_email(medico_email)
    while flag_email == False:
        medico_email = input(Fore.YELLOW + "ERROR - Ingrese su email correctamente: ")
        flag_email = validaciones.validar_email(medico_email)

    medico_contraseña = input(Fore.YELLOW + "Contraseña: ")
    flag_contraseña = validaciones.validador_solo_numeros(medico_contraseña)
    while flag_contraseña == False:
        medico_contraseña = input(Fore.YELLOW + "ERROR: ingrese una contraseña de solo numero: ")
        flag_contraseña = validaciones.validador_solo_numeros(medico_contraseña)

    usuarios.append({"nombre":medico_nombre, "apellido":medico_apellido, "cuit":medico_cuit, "email":medico_email,"matricula":medico_matricula, "contraseña":medico_contraseña})

    #imprimir_lista_medicos(usuarios)

def modificar_medico(usuarios):
    matricula_medico_eliminar = input(Fore.YELLOW + "Para modificar un medico ingrese el numero de matricula: ")
    flag = None
    for user in usuarios:
        if user["rol"] == "medico" and user["matricula"] == str(matricula_medico_eliminar):
            opcion = input(Fore.YELLOW + "que desea modificar: 1) mail - 2) contraseña")
            if opcion == "1":
                user["email"] = input(Fore.YELLOW + "Ingrese el nuevo Email del Medico/a: ")#agregar validacion de email y letras
                flag_email = validaciones.validar_email(user["email"])
                while flag_email == False:
                    user["email"] = input(Fore.YELLOW + "Ingrese su mail correctamente: ")
                    flag_email = validaciones.validar_email(user["email"])


def eliminar_medico(usuarios):
    print(usuarios)
    cuit_medico_eliminar = input(Fore.YELLOW + "Para darse de baja ingrese su NUMERO de CUIT: ")
    for user in usuarios:
        if user["cuit"] == int(cuit_medico_eliminar):
            confirmacion = input(Fore.YELLOW + "Confirmacion, desea eliminar? SI/NO:  ") #hay que agregar que preguntar para confirmar
            if confirmacion == "SI":
                user["estado_socio"] = 0
                #usuarios.remove(user) Cambiamos el estado de 1 a 0 para no perder el dato del cliente
            else:
                pass #se vuelve al menu donde se eligio eliminar medico
            

def imprimir_lista_medicos(usuarios):
    for user in usuarios:        
        print(Fore.YELLOW + "\nNombre: {0}".format(user["nombre"],))
        print(Fore.YELLOW + "Apellido: {0}".format(user["apellido"]))
        print(Fore.YELLOW + "CUIT: {0}".format(user["cuit"]))
        print(Fore.YELLOW + "Email: {0}".format(user["email"]))
        print(Fore.YELLOW + "Matricula: {0}".format(user["matricula"]))
        print(Fore.YELLOW + "Contraseña: {0}".format(user["contraseña"]))
        print(Fore.YELLOW + "Estado del Socio: {0}".format(user["estado_socio"]))