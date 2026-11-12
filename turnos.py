import os
import csv
import Medicos

def creacion_csv():
    horarios = ["CUIT Médico", "08:00", "09:00", "10:00", "11:00", "12:00"]

    # Obtiene la carpeta donde está ubicado este archivo Python
    carpeta = os.path.dirname(os.path.abspath(__file__))

    # Construye la ruta del CSV dentro de esa carpeta
    ruta_csv = os.path.join(carpeta, "turnos.csv")

    with open(ruta_csv, "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(horarios)

def pedir_turno(cuit):

    pass