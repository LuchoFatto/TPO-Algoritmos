




#NO SE USA SOLO A MODO DE FUTURO USO PARA ARCHIVOS
"""
- `[0]` **CUIT / DNI** (`str`): Identificador único (ej: `"20123456789"`).
- `[1]` **Nombre y Apellido** (`str`): Nombre del usuario.
- `[2]` **Email** (`str`): Correo electrónico.
- `[3]` **Teléfono** (`str`): Número de contacto.
- `[4]` **Rol** (`str`): `"afiliado"` | `"medico"` | `"farmacia"` | `"admin"`.
- `[5]` **Contraseña** (`str`): Clave de acceso.
- `[6]` **Activo** (`bool`): `True` (alta) / `False` (baja lógica).
- `[7]` **Estado de Pago** (`str`): `"al_dia"` | `"deudor"` (aplica a afiliados).
- `[8]` **Plan / Especialidad** (`str`): `"Basico"`, `"Plus"`, `"Familiar"` o especialidad médica.
"""

#Lista de todos los usuarios
lista_usuarios = [
    {
        "Nombre": "Juan",
        "Apellido": "Pérez",
        "CUIT": 20123456789,
        "Telefono": 1122334455,
        "Email": "juan@gmail.com",
        "Plan": "Basico",
        "Password": "Juan123!",
        "Historial": [],
        "Deudor": False
    },
    {
        "Nombre": "María",
        "Apellido": "Gómez",
        "CUIT": 20987654321,
        "Telefono": 1144556677,
        "Email": "maria@gmail.com",
        "Plan": "Plus",
        "Password": "Maria123!",
        "Historial": [],
        "Deudor": True
    },
    {
        "Nombre": "Carlos",
        "Apellido": "López",
        "CUIT": 20333444555,
        "Telefono": 1166778899,
        "Email": "carlos@gmail.com",
        "Plan": "Familiar Dueño",
        "Password": "Carlos123!",
        "Historial": [],
        "Deudor": False,
        "Familia": [20444555666]
    },
    {
        "Nombre": "Lucía",
        "Apellido": "López",
        "CUIT": 20444555666,
        "Telefono": 1177889900,
        "Email": "lucia@gmail.com",
        "Plan": "Familiar Hijo",
        "Password": "Lucia123!",
        "Historial": [],
        "Deudor": False,
        "Dueño": 20333444555
    }
]

#lista de todos los medicos
Medicos = [
    {
        "nombre": "Nicolas", 
        "apellido": "Martinez", 
        "email": "nicolasmartinez@gmail.com", 
        "rol": "medico",
        "matricula": "213123",
        #"contraseña": "tateti",
        #"telefono": "1162453589"
    },
    {
        "nombre": "Tomas", 
        "apellido": "Gonzales", 
        "email": "ngonza@gmail.com", 
        "rol": "medico",
        "matricula": "123456",
        #"contraseña": "asfalto",
        #"telefono": "1162452078"
    }
]

#lista de todos las farmacias
Farmacias = [
    {
        "id": "farmacity", 
        "direccion": "alvear 1234", 
        "beneficiaria": "1"
    },
    {
        "id": "farmaplus", 
        "direccion": "mitre 4213", 
        "beneficiaria": "0"
    }
]

#adminisitrador
Admin = {
    'Usuario' : 'adminadmin',
    'Contraseña' : 'admin123'
}