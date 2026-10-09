from auth import validar_email
from auth import validar_contrasenia
from usuarios import limpiar_nro

def test_mail():
    assert validar_email("fra@hotmail.com") == True
    assert validar_email("fra@hotmail") == False
    assert validar_email("fra@") == False

def test_contrasenia():
    assert validar_contrasenia("Franco28#") == True
    assert validar_contrasenia("Jorge") == False
    assert validar_contrasenia("jorgito_28") == False

def test_limpiarnro():
    assert limpiar_nro('44.338.568') == 44338568
    assert limpiar_nro("22 33 44 11") == 22334411
    assert limpiar_nro("234_111") == 234111