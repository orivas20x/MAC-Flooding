# Laboratorio 5: Ataque de Denegación de Servicio mediante MAC Flooding

## 🎥 Enlace del Video Demostrativo
[Haz clic aquí para ver la demostración del laboratorio en Google Drive]https://drive.google.com/file/d/1M7JqGs5oErSm6h7OfnhShVwWL7lIWkwL/view?usp=sharing

---

## 1. Objetivo del Laboratorio
El propósito de esta práctica es demostrar de forma analítica la vulnerabilidad operativa de los switches de red local (Capa 2) cuando se satura la capacidad de su memoria dinámica de almacenamiento de direcciones de hardware, conocida como Tabla CAM (Content Addressable Memory). Se estudia su degradación hacia el modo de falla abierta (fail-open) y sus contramedidas.

---

## 2. Objetivo del Script
El script desarrollado en Python y Scapy automatiza un bombardeo masivo de tramas Ethernet inválidas por segundo. Utilizando la función constructora `RandMAC()`, genera continuamente direcciones físicas de origen aleatorias destinadas al broadcast de la red (`ff:ff:ff:ff:ff:ff`). Al llenarse la memoria del switch con registros falsos, este pierde la capacidad de conmutar y se degrada operativamente al comportamiento de un Hub, retransmitiendo de forma indiscriminada todo el tráfico legítimo por todos sus puertos físicos activos.

---

## 3. Documentación de la Red
* **Mi Matrícula:** 2024-2421
* **Segmento de Red Local:** `10.24.21.0/24`
* **Herramienta de Inyección:** Scapy / Python 3
* **IP de la Máquina Atacante (Kali Linux):** `10.24.21.2`
* **IP del Router / Gateway (R1):** `10.24.21.1`

---

## 4. Evidencias de Funcionamiento (PoC)
<img width="2481" height="1267" alt="image" src="https://github.com/user-attachments/assets/eb375611-48ad-4a72-b2b6-31c226162cfd" />


---

## 5. Medidas Técnicas de Mitigación (Hardening)
La solución definitiva para evitar que un atacante sature la tabla CAM del switch desde un puerto de acceso es implementar **Port Security** en los equipos de distribución Cisco:

1. Se configuran las interfaces de los usuarios finales estrictamente en modo de acceso.
2. Se habilita la seguridad de puerto para recordar o limitar las direcciones de hardware.
3. Se restringe el número máximo de direcciones MAC permitidas en el puerto físico (máximo 1 o 2).
4. Se define la penalización ante violaciones como `shutdown`, lo que apaga eléctricamente el puerto del switch de forma inmediata si un script intenta falsificar o inundar con nuevas direcciones MAC.

### Comandos de Configuración en Cisco:
```text
Switch(config)# interface FastEthernet 0/5
Switch(config-if)# switchport mode access
Switch(config-if)# switchport port-security
Switch(config-if)# switchport port-security maximum 1
Switch(config-if)# switchport port-security violation shutdown
