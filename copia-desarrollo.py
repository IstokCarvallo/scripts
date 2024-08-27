# import shutil
from os import path
from datetime import datetime
import distutils

folder  = "Desarrollo 22"
source  =    path.join("c:/", folder)
target  =    path.join("f:/", folder)

print(f'Inicio proceso de respaldo :{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')

try:
    distutils.dir_util.copy_tree(source, target)
    # shutil.copy(origen, destino)
    print('Directorio copiado con éxito')
except FileNotFoundError:
    print('El directorio de origen no se encontró')
except PermissionError:
    print('Permiso denegado')

print(f'Fin proceso de respaldo :{datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')