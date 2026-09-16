import re
def validador_solo_letras(texto):
    for caracter in texto:
        codigo = ord(caracter)
        # A-Z: 65-90 | a-z: 97-122
        if (codigo < 64) or (90 < codigo < 97) or (codigo > 122):
            return False
    return True

def validador_solo_numeros(numero):
    for caracter in numero:
        codigo = ord(caracter)
        if (codigo < 48 or codigo > 57):
            return False   
    return True

def validar_mail(texto):
    flag_texto = validador_solo_letras(texto)
    flag = None
    for caracter in texto:
        codigo = ord(caracter)
        if codigo == 64:
            flag = True
    if flag == True and flag_texto == True:
        return True
    else:
        return False

def validar_direccion(direccion):

    patron_direccion = re.compile(r"^[a-zA-Z0-9À-ÿñÑ.°]+(?:\s+[a-zA-Z0-9À-ÿñÑ.°]+)*\s+\d+\s*[a-zA-Z]?$", re.IGNORECASE)

    return bool(re.match(patron_direccion, direccion))

def bucle_medico(mensaje, mensaje_error, funcion_validadora):
    dato = input(mensaje)
    flag = funcion_validadora(dato)
    while flag == False:
        dato = input(mensaje_error)
        flag = funcion_validadora(dato)
    return dato