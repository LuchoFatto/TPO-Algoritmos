import os
import csv

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