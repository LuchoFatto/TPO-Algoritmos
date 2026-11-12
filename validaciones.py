import auth

def validador_solo_letras(texto):
    """Reutiliza la validacion de letras definida en auth.py."""
    return auth.validacion_letras(texto)

def validador_solo_numeros(numero):
    """Valida que el dato tenga solamente numeros y no este vacio."""
    return bool(numero) and numero.isdigit()

def validar_email(email):
    """Reutiliza la validacion de email definida en auth.py."""
    return auth.validar_email(email)

def validar_direccion(direccion):
    """Reutiliza la validacion de direccion definida en auth.py."""
    return auth.validar_direccion(direccion)

def bucle_medico(mensaje, mensaje_error, funcion_validadora):
    dato = input(mensaje)
    flag = funcion_validadora(dato)
    while flag == False:
        dato = input(mensaje_error)
        flag = funcion_validadora(dato)
    return dato

def validador_especialidad(especialidad):
    if especialidad in ["Cardiologia", "Dermatologia", "Pediatria", "Traumatologia"]:
        return True
    else:
        return False