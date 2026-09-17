




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
        "rol": "admin"
    }
]