import re


def validar_email(email) -> bool:
    patron_email = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    return bool(re.match(patron_email, email))


def validar_cuit(cuit):
    patron_limpiar = re.compile(r"[-\s]")

    cuit_limpio = re.sub(patron_limpiar, "", cuit)

    return len(cuit_limpio) == 11


cuit = input("Ingrese cuit:")
print(validar_cuit(cuit))


def validar_numero_telefono(num_telefono):
    pass


def validar_contrasenia(contrasenia):
    pass
