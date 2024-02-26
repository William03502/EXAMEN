import os 

numero_d = 1
numero_f = 1
while numero_d <= 10:
    ruta = "Tarea3/folder" +str(numero_d)
    os.makedirs(ruta, exist_ok=True)
    while numero_f <= 10:
        archivo = "Tarea3/folder" + str(numero_d) + "/fichero" + str(numero_f) + ".txt"
        with open(archivo, "w") as f:
            f.write("Este es el contenido del fichero" + str(numero_f))
        numero_f += 1
    numero_d += 1
    numero_f = 1