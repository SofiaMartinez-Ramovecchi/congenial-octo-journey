import os
import threading

# Captura de pantalla usando el comando import

window_id = os.popen("xwininfo | grep 'Window id:' | cut -d' ' -f4").read().strip()

screenshot_filename = input("Introduce el nombre del archivo de captura de pantalla: ")

# Ejecutar el comando de captura de pantalla y guardarla con el nombre proporcionado
os.system(f"import -window {window_id} {screenshot_filename}")
print(f"Captura de pantalla guardada como {screenshot_filename}")

