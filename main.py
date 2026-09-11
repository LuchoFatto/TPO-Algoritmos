import funciones_iniciales 

usuarios = [
    {
        "nombre": "Nicolas",
        "apellido": "Martinez",
        "email": "nicolasmartinez@gmail.com",
        "rol": "afiliado"
    }, 
    {
        "nombre": "Marco",
        "apellido": "Gomez",
        "email": "marco@gmail.com",
        "rol": "medico"
    }
]

funciones_iniciales.alta_usuario(usuarios)

print(usuarios)