import os
import csv
import Medicos
import auth
import usuarios
import time
from colorama import Fore, Style, init
from rich import box
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

# def creacion_csv():
#     horarios = ["CUIT Médico", "08:00", "09:00", "10:00", "11:00", "12:00"]

#     # Obtiene la carpeta donde está ubicado este archivo Python
#     carpeta = os.path.dirname(os.path.abspath(__file__))

#     # Construye la ruta del CSV dentro de esa carpeta
#     ruta_csv = os.path.join(carpeta, "turnos.csv")

#     with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
#         escritor = csv.writer(archivo)
#         escritor.writerow(horarios)


def agregarMedicoTurnos(cuit_medico):

    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(carpeta, "turnos.csv")

    horarios = ["CUIT Médico", "08:00", "09:00",
                "10:00", "11:00", "12:00"]

    with open(ruta_archivo, "a+", newline="", encoding="utf-8") as archivo:

        archivo.seek(0)
        lector = list(csv.reader(archivo))

        # Crear encabezados si el archivo está vacío
        if not lector:
            escritor = csv.writer(archivo)
            escritor.writerow(horarios)

        # Evitar agregar dos veces al mismo médico
        elif any(fila[0] == str(cuit_medico) for fila in lector[1:] if fila):
            return

        # Agregar médico con todos los horarios disponibles
        escritor = csv.writer(archivo)
        escritor.writerow([str(cuit_medico), "", "", "", "", ""])



# Inicializa colorama para compatibilidad de colores en consola de Windows
init(autoreset=True)
console = Console()


def pedir_opcion(mensaje, maximo):
    """Valida que el usuario ingrese un número entero entre 0 y maximo."""
    opcion_valida = False
    resultado = 0

    while not opcion_valida:
        opcion = input(f"{Fore.CYAN}{Style.BRIGHT}{mensaje}{Style.RESET_ALL}").strip()
        if opcion.isdigit() and 0 <= int(opcion) <= maximo:
            resultado = int(opcion)
            opcion_valida = True
        else:
            print(f"{Fore.RED}✖ Opción inválida. Ingrese un número entre 0 y {maximo}.")
            time.sleep(1)

    return resultado


def elegir_especialidad():
    """Muestra el menú de especialidades con tabla Rich y devuelve el nombre elegido."""
    especialidades = ["Cardiologia", "Pediatria", "Traumatologia", "Dermatologia"]
    flag = True
    eleccion = ""

    while flag:
        os.system("cls")
        console.print(
            Panel.fit(
                "[bold cyan]SISTEMA DE RESERVA DE TURNOS[/bold cyan]\n[dim]Paso 1 de 3: Selección de especialidad[/dim]",
                border_style="cyan",
            )
        )

        tabla = Table(box=box.ROUNDED, header_style="bold white on blue", expand=False)
        tabla.add_column("Opción", justify="center", style="bold yellow", width=8)
        tabla.add_column("Especialidad Médica", style="white", width=26)

        for indice in range(len(especialidades)):
            tabla.add_row(f"[{indice + 1}]", especialidades[indice])

        console.print(tabla)

        opcion = pedir_opcion("Seleccione una especialidad >> ", len(especialidades))
        if opcion != 0:
            eleccion = especialidades[opcion - 1]
            flag = False
        else:
            print(f"{Fore.YELLOW}⚠ Debe elegir una opción entre 1 y {len(especialidades)}.")
            time.sleep(1.5)

    return eleccion


def filtrar_medicos_por_especialidad(ruta_m, especialidad):
    """Lee medicos.json y devuelve {CUIT: 'nombre apellido'} para la especialidad dada."""
    medicos = auth.abrir_archivo(ruta_m)
    lista_permitida = {}

    for m in medicos:
        if m["especialidad"] == especialidad:
            lista_permitida[int(m["CUIT"])] = f'{m["nombre"]} {m["apellido"]}'

    return lista_permitida


def medicos_disponibles(ruta_turnos, lista_permitida):
    """Lee turnos.csv y devuelve los médicos permitidos con al menos 1 horario libre."""
    disponibles = []

    with open(ruta_turnos, "r", newline="", encoding="utf-8") as archivo:
        _, *horarios = archivo.readline().rstrip("\r\n").split(",")

        for linea in archivo:
            if linea.strip():
                cuit, *celdas = linea.rstrip("\r\n").split(",")
                cuit = int(cuit.strip())

                if cuit in lista_permitida:
                    libres = []
                    for i in range(len(horarios)):
                        if i >= len(celdas) or celdas[i].strip() == "":
                            libres.append(horarios[i].strip())

                    if libres:
                        disponibles.append({
                            "cuit": cuit,
                            "nombre": lista_permitida[cuit],
                            "libres": libres
                        })

    return disponibles


def seleccionar_turno(disponibles, especialidad):
    """Gestiona la elección de médico y horario con interfaz Rich y opción de retroceso."""
    cuit_medico = None
    nombre_medico = None
    hora_elegida = None

    if not disponibles:
        os.system("cls")
        console.print(
            Panel(
                f"[bold yellow]No hay médicos con horarios disponibles para {especialidad}.[/bold yellow]",
                title="Sin disponibilidad",
                border_style="yellow",
            )
        )
        time.sleep(2.5)
    else:
        continuar = True
        while continuar:
            os.system("cls")
            console.print(
                Panel.fit(
                    f"[bold cyan]ESPECIALIDAD: {especialidad.upper()}[/bold cyan]\n[dim]Paso 2 de 3: Elija un profesional disponible[/dim]",
                    border_style="cyan",
                )
            )

            tabla_medicos = Table(box=box.ROUNDED, header_style="bold white on blue")
            tabla_medicos.add_column("Opción", justify="center", style="bold yellow", width=8)
            tabla_medicos.add_column("Profesional", style="bold white", width=26)
            tabla_medicos.add_column("CUIT", justify="center", style="cyan", width=15)
            tabla_medicos.add_column("Turnos Libres", justify="center", style="green", width=15)

            for i in range(len(disponibles)):
                med = disponibles[i]
                tabla_medicos.add_row(
                    f"[{i + 1}]",
                    med["nombre"],
                    str(med["cuit"]),
                    f"{len(med['libres'])} disp."
                )

            tabla_medicos.add_row("[0]", "[red]Cancelar operación[/red]", "-", "-")
            console.print(tabla_medicos)

            opcion_med = pedir_opcion("Seleccione un médico >> ", len(disponibles))

            if opcion_med == 0:
                os.system("cls")
                print(f"{Fore.YELLOW}Operación cancelada por el usuario.")
                time.sleep(1.5)
                continuar = False
            else:
                medico_actual = disponibles[opcion_med - 1]

                os.system("cls")
                console.print(
                    Panel.fit(
                        f"[bold cyan]DR/A. {medico_actual['nombre'].upper()}[/bold cyan]\n[dim]Paso 3 de 3: Seleccione un horario disponible[/dim]",
                        border_style="green",
                    )
                )

                tabla_horarios = Table(box=box.ROUNDED, header_style="bold white on green")
                tabla_horarios.add_column("Opción", justify="center", style="bold yellow", width=8)
                tabla_horarios.add_column("Horario Disponible", justify="center", style="bold white", width=22)

                for idx in range(len(medico_actual["libres"])):
                    tabla_horarios.add_row(f"[{idx + 1}]", medico_actual["libres"][idx])

                tabla_horarios.add_row("[0]", "[yellow]Volver a elegir médico[/yellow]")
                console.print(tabla_horarios)

                opcion_hora = pedir_opcion("Seleccione un horario >> ", len(medico_actual["libres"]))

                if opcion_hora != 0:
                    cuit_medico = medico_actual["cuit"]
                    nombre_medico = medico_actual["nombre"]
                    hora_elegida = medico_actual["libres"][opcion_hora - 1]
                    continuar = False
                else:
                    print(f"{Fore.CYAN}↺ Volviendo al listado de médicos...")
                    time.sleep(0.8)

    return cuit_medico, nombre_medico, hora_elegida


def guardar_turno_csv(ruta_turnos, cuit_medico, hora_elegida, cuit_paciente):
    """Graba el CUIT del paciente en la celda correspondiente manteniendo intactos todos los demás médicos."""
    nuevas_lineas = []

    with open(ruta_turnos, "r", encoding="utf-8") as archivo:
        primera_linea = archivo.readline().rstrip("\r\n")

        if primera_linea:
            nuevas_lineas.append(primera_linea + "\n")
            encabezado = primera_linea.split(",")

            indice_hora = -1
            for i in range(len(encabezado)):
                if encabezado[i].strip() == hora_elegida:
                    indice_hora = i

            for linea in archivo:
                if linea.strip():
                    columnas = linea.rstrip("\r\n").split(",")
                    while len(columnas) < len(encabezado):
                        columnas.append("")

                    # Solo se modifica la columna si la fila pertenece al médico elegido
                    if indice_hora != -1 and int(columnas[0].strip()) == int(cuit_medico):
                        columnas[indice_hora] = str(cuit_paciente)

                    # Este append va fuera del if anterior para conservar a TODOS los médicos
                    nuevas_lineas.append(",".join(columnas) + "\n")

    if nuevas_lineas:
        with open(ruta_turnos, "w", encoding="utf-8") as archivo:
            archivo.writelines(nuevas_lineas)


def guardar_historial_usuario(ruta_u, cuit_paciente, nombre_medico, hora_elegida):
    """Agrega la tupla (nombre_medico, hora_elegida) en la key 'Historial' del paciente."""
    lista_usuarios = auth.abrir_archivo(ruta_u)

    for usuario in lista_usuarios:
        if int(usuario["CUIT"]) == int(cuit_paciente):
            if "Historial" not in usuario:
                usuario["Historial"] = []
            usuario["Historial"].append((nombre_medico, hora_elegida))

    auth.cargar_archivo(lista_usuarios,ruta_u)


def pedir_turno(cuit):
    """Orquesta el flujo completo de reserva para el paciente identificado por 'cuit'."""
    ruta_m = os.path.join(os.path.dirname(os.path.abspath(__file__)), "medicos.json")
    ruta_turnos = os.path.join(os.path.dirname(os.path.abspath(__file__)), "turnos.csv")
    ruta_u = usuarios.RUTA_ARCHIVO

    especialidad = elegir_especialidad()

    os.system("cls")
    print(f"{Fore.CYAN}Buscando profesionales disponibles en {especialidad}...")
    time.sleep(0.8)

    lista_permitida = filtrar_medicos_por_especialidad(ruta_m, especialidad)
    disponibles = medicos_disponibles(ruta_turnos, lista_permitida)

    cuit_medico, nombre_medico, hora_elegida = seleccionar_turno(disponibles, especialidad)

    if hora_elegida is not None:
        os.system("cls")
        print(f"{Fore.CYAN}Registrando su reserva en el sistema...")
        time.sleep(0.8)

        guardar_turno_csv(ruta_turnos, cuit_medico, hora_elegida, cuit)
        guardar_historial_usuario(ruta_u, cuit, nombre_medico, hora_elegida)

        os.system("cls")
        comprobante = (
            f"[bold green]✔ TURNO CONFIRMADO EXITOSAMENTE[/bold green]\n\n"
            f"[bold white]Especialidad:[/bold white] {especialidad}\n"
            f"[bold white]Profesional:[/bold white]  {nombre_medico} (CUIT: {cuit_medico})\n"
            f"[bold white]Horario:[/bold white]      [bold yellow]{hora_elegida} hs[/bold yellow]\n"
            f"[bold white]Paciente:[/bold white]     CUIT {cuit}"
        )
        console.print(Panel.fit(comprobante, title="Comprobante de Reserva", border_style="green"))
        time.sleep(3)


def obtener_historial_usuario(ruta_u, cuit_paciente):
    """Busca al paciente por CUIT en el JSON y devuelve su lista 'Historial'."""
    lista_usuarios = auth.abrir_archivo(ruta_u)
    historial = []

    for usuario in lista_usuarios:
        if int(usuario["CUIT"]) == int(cuit_paciente):
            historial = usuario.get("Historial", [])

    return historial


def ver_historial(cuit):
    """Muestra en una tabla Rich los turnos guardados en la key 'Historial' del paciente."""
    ruta_u = usuarios.RUTA_ARCHIVO
    historial = obtener_historial_usuario(ruta_u, cuit)

    os.system("cls")
    console.print(
        Panel.fit(
            f"[bold cyan]HISTORIAL DE TURNOS RESERVADOS[/bold cyan]\n[dim]Paciente CUIT: {cuit}[/dim]",
            border_style="cyan",
        )
    )

    if not historial:
        console.print(
            Panel(
                "[yellow]Aún no tienes turnos registrados en tu historial.[/yellow]",
                border_style="yellow",
                expand=False,
            )
        )
    else:
        tabla_historial = Table(box=box.ROUNDED, header_style="bold white on blue")
        tabla_historial.add_column("N°", justify="center", style="bold yellow", width=6)
        tabla_historial.add_column("Profesional", style="bold white", width=28)
        tabla_historial.add_column("Horario Reservado", justify="center", style="bold green", width=20)

        for i in range(len(historial)):
            registro = historial[i]
            nombre_medico = registro[0]
            hora_turno = registro[1]
            tabla_historial.add_row(f"[{i + 1}]", nombre_medico, f"{hora_turno} hs")

        console.print(tabla_historial)

    input(f"\n{Fore.CYAN}{Style.BRIGHT}Presione Enter para volver al menú...{Style.RESET_ALL}")


def menu_turnos(cuit):
    """Menú principal para elegir entre reservar un turno o consultar el historial."""
    continuar = True

    while continuar:
        os.system("cls")
        console.print(
            Panel.fit(
                f"[bold cyan]GESTIÓN DE TURNOS MÉDICOS[/bold cyan]\n[dim]Bienvenido | CUIT: {cuit}[/dim]",
                border_style="cyan",
            )
        )

        tabla_menu = Table(box=box.ROUNDED, header_style="bold white on blue", expand=False)
        tabla_menu.add_column("Opción", justify="center", style="bold yellow", width=8)
        tabla_menu.add_column("Acción", style="white", width=32)

        tabla_menu.add_row("[1]", "Reservar un nuevo turno")
        tabla_menu.add_row("[2]", "Ver mis turnos (Historial)")
        tabla_menu.add_row("[0]", "[red]Salir[/red]")

        console.print(tabla_menu)

        opcion = pedir_opcion("Seleccione una opción >> ", 2)

        if opcion == 1:
            pedir_turno(cuit)
        elif opcion == 2:
            ver_historial(cuit)
        else:
            os.system("cls")
            print(f"{Fore.CYAN}Saliendo del módulo de turnos...")
            time.sleep(1)
            continuar = False