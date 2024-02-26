import os
import logging
import shutil

logging.basicConfig(filename='/home/guille/logs/espacio.log', level=logging.INFO)

total, usado, libre = shutil.disk_usage("/")

porcentaje_usado = usado / total * 100

if porcentaje_usado > 80:
    logging.error(f'El espacio ocupado en la partición "/" es mayor que 80%: {porcentaje_usado}%')
elif porcentaje_usado > 60:
    logging.warning(f'El espacio ocupado en la partición "/" es mayor que 60% y menor que 80%: {porcentaje_usado}%')
else:
    logging.info(f'El espacio ocupado en la partición "/" es mayor que 0% y menor que 60%: {porcentaje_usado}%')
