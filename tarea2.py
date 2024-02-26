import os

salida = os.popen('df -h /dev/sda2').readlines()
for linea in salida[1:]:
    partes = linea.split()
    if len(partes) >= 6:
        ubicacion = partes[0]
        porcentaje = partes[4]
        print(f'{ubicacion} {porcentaje}')

salida = os.popen('df -h /dev/sdb1').readlines()
for linea in salida[1:]:
    partes = linea.split()
    if len(partes) >= 6:
        ubicacion = partes[0]
        porcentaje = partes[4]
        print(f'{ubicacion} {porcentaje}')

