# Planificación y División de Tareas - Entrega 40%

**Proyecto:** Sistema de Gestión de Obra Social

**Materia:** Algoritmos y Estructura de Datos I

**Ramas de trabajo:** `dylan` | `franco` | `luciano` | `marco`

**Fecha límite:** 17/09/2026

---

## 1. Contrato Común de Datos (Matriz de Usuarios)

Para evitar dependencias entre integrantes, todos los módulos trabajarán sobre una **matriz principal (lista de listas)**.

### Índices de columnas para cada fila en `usuarios` (Revisar):

- `[0]` **CUIT / DNI** (`str`): Identificador único (ej: `"20123456789"`).
- `[1]` **Nombre y Apellido** (`str`): Nombre del usuario.
- `[2]` **Email** (`str`): Correo electrónico.
- `[3]` **Teléfono** (`str`): Número de contacto.
- `[4]` **Rol** (`str`): `"afiliado"` | `"medico"` | `"farmacia"` | `"admin"`.
- `[5]` **Contraseña** (`str`): Clave de acceso.
- `[6]` **Activo** (`bool`): `True` (alta) / `False` (baja lógica).
- `[7]` **Estado de Pago** (`str`): `"al_dia"` | `"deudor"` (aplica a afiliados).
- `[8]` **Plan / Especialidad** (`str`): `"Basico"`, `"Plus"`, `"Familiar"` o especialidad médica.

---

## 2. Asignación de Archivos y Responsabilidades (Flexibles)

### Rama: `integrante`

- **Archivos asignados:** `validaciones.py` | `auth.py`
- **Lógica independiente:** Trabaja con validación de cadenas, expresiones regulares y control de intentos.
- **Tareas específicas:**
    - **`validaciones.py`:**
        - `validar_cuit(cuit)`: Verifica formato numérico y longitud obligatoria.
        - `validar_email(email)`: Valida estructura mediante expresiones regulares.
        - `leer_opcion(mensaje, min_val, max_val)`: Lectura controlada de opciones numéricas por teclado para evitar caídas de la terminal.
    - **`auth.py`:**
        - `iniciar_sesion(matriz_usuarios, rol_esperado)`:
            - Solicita CUIT y contraseña.
            - Valida existencia, coincidencia de rol y que el usuario esté activo (`fila[6] == True`).
            - Maneja un contador de hasta 2 intentos fallidos antes de regresar al menú.
            - Retorna la fila del usuario validado o `None`.

---

### Rama: `integrante`

- **Archivos asignados:** `usuarios.py`
- **Lógica independiente:** CRUD y manipulación de filas de la matriz con listas y funciones lambda/filter.
- **Tareas específicas:**
    - **`usuarios.py`:**
        - `alta_usuario(matriz_usuarios, nuevo_usuario)`: Valida que el CUIT no exista previamente y agrega el nuevo registro a la lista.
        - `baja_usuario(matriz_usuarios, cuit)`: Solicita confirmación y cambia el estado a `False` (`fila[6] = False`).
        - `buscar_usuario_por_cuit(matriz_usuarios, cuit)`: Búsqueda secuencial que retorna la fila correspondiente o `None`.
        - `listar_usuarios_por_rol(matriz_usuarios, rol)`: Retorna la sublista filtrada usando `filter` y `lambda`.
        - `modificar_plan_afiliado(matriz_usuarios, cuit, nuevo_plan)`: Actualiza la columna de plan del afiliado.

---

### Rama: `integrante`

- **Archivos asignados:** `funciones_iniciales.py` | `turnos.py`
- **Lógica independiente:** Define los datos base de prueba y deja la estructura lista para el módulo de turnos.
- **Tareas específicas:**
    - **`funciones_iniciales.py`:**
        - `cargar_datos_semilla()`: Retorna la matriz de usuarios inicial precargada (mínimo 3 afiliados con y sin deuda, 2 médicos con especialidad, 1 farmacia y 1 administrador).
        - `cargar_cartilla_inicial()`: Retorna listas de médicos y farmacias adheridas para consulta.
    - **`turnos.py`:**
        - Implementar stubs informativos para las opciones que quedan fuera del 40%:
            - `reservar_turno()`: Muestra aviso de funcionalidad deshabilitada hasta la entrega final.
            - `consultar_turnos()`: Muestra aviso de funcionalidad deshabilitada.
        - Dejar comentada la estructura que tendrá la matriz de turnos para el 100%.

---

### Rama: `integrante`

- **Archivos asignados:** `menus.py` | `main.py`
- **Lógica independiente:** Control de navegación de consola e interacción con el usuario.
- **Tareas específicas:**
    - **`menus.py`:**
        - `menu_principal()`: Menú inicial con selección de rol y opción de salir.
        - `menu_afiliado(usuario_actual)`:
            - **Bloqueo por deuda:** Si `usuario_actual[7] == "deudor"`, bloquea el acceso a funciones operativas y muestra aviso de regularización.
            - Opciones: ver perfil, consultar cartilla, cambiar plan, darse de baja y turnos (deshabilitados).
        - `menu_admin(matriz_usuarios)`: Opciones de alta, baja lógica y visualización de padrones.
        - `menu_farmacia(matriz_usuarios)`: Búsqueda por CUIT para responder únicamente si el paciente está **ACTIVO** o **INACTIVO**.
        - `menu_medico(usuario_actual)`: Visualización de datos propios, baja del sistema y turnos (deshabilitados).
    - **`main.py`:**
        - Punto de entrada del programa: inicializa la matriz y ejecuta el bucle de navegación principal.

---

## 3. Protocolo de Trabajo en Git

1. Cada integrante trabaja exclusivamente dentro de su rama: `git checkout <tu_nombre>`.
2. Probar cada módulo de forma individual ejecutando directamente el archivo (`python nombre_archivo.py`).
3. Hacer commits claros de cada función terminada y subir los cambios: `git push origin <tu_nombre>`.
4. Una vez verificados los módulos de manera independiente, se integrarán ordenadamente en la rama `main`.
