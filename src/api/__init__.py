import os
import sys

# Obtener la ruta del directorio actual del script
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# Añadir la ruta del directorio padre al sys.path
parent_dir = os.path.dirname(current_script_dir)
sys.path.append(parent_dir)