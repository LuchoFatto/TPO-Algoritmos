import csv

def creacion_csv():
    horarios = ["CUIT Médico", "08:00", "09:00", "10:00", "11:00", "12:00"]

    with open("turnos.csv", "w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(horarios)
