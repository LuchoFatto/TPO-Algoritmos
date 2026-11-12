import csv
import os
from colorama import Fore

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

def ver_turnos_medico(cuit_medico):

    carpeta = os.path.dirname(os.path.abspath(__file__))
    ruta_archivo = os.path.join(carpeta, "turnos.csv")

    if not os.path.exists(ruta_archivo):
        print(Fore.RED + "\nNo existe el archivo de turnos.")
        return

    with open(ruta_archivo, "r", newline="", encoding="utf-8") as archivo:

        lector = csv.DictReader(archivo)

        encontrado = False

        for fila in lector:

            if not fila or not fila["CUIT Médico"]:
                continue

            if fila["CUIT Médico"] == str(cuit_medico):

                encontrado = True

                print(Fore.YELLOW + "\n--- MIS TURNOS ---")
                print(Fore.CYAN + f"\nMédico: {cuit_medico}\n")

                for horario, paciente in fila.items():

                    if horario == "CUIT Médico":
                        continue

                    if paciente.strip() == "":
                        print(Fore.GREEN + f"{horario} - LIBRE")
                    else:
                        print(Fore.RED + f"{horario} - OCUPADO (Paciente: {paciente})")

                break

        if not encontrado:
            print(Fore.RED + "\nNo se encontró ningún médico con ese CUIT.")