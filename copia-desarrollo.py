# import shutil
from os import path
import distutils

folder  = "Desarrollo 22"
source  =    path.join("c:/", folder)
target  =    path.join("f:/", folder)

try:
    distutils.dir_util.copy_tree(source, target)
    # shutil.copy(origen, destino)
    print('Directorio copiado con éxito')
except FileNotFoundError:
    print('El directorio de origen no se encontró')
except PermissionError:
    print('Permiso denegado')