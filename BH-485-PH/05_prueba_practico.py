import minimalmodbus
import serial
import time

# 1. Configuración del Sensor
# Reemplaza '/dev/ttyUSB0' por el puerto donde esté tu adaptador RS485

sensor = minimalmodbus.Instrument('COM1', 2) # El '2' es el ID por defecto 

# Ajustes de comunicación según el manual 
sensor.serial.baudrate = 9600
sensor.serial.bytesize = 8
sensor.serial.parity   = serial.PARITY_NONE
sensor.serial.stopbits = 1
sensor.serial.timeout  = 1

def leer_datos():
    try:
        # 2. Lectura de Temperatura (Registro 0) 
        # Se multiplica por 0.1 como indica el manual [cite: 95, 110]
        temp_raw = sensor.read_register(0, 0) 
        temperatura = temp_raw * 0.1

        # 3. Lectura de pH (Registro 1) 
        # Se multiplica por 0.01 como indica el manual [cite: 95, 121]
        ph_raw = sensor.read_register(1, 0)
        ph = ph_raw * 0.01

        print(f"--- Lectura del Sensor BH-485-PH ---")
        print(f"Temperatura: {temperatura:.1f} °C")
        print(f"Valor de pH: {ph:.2f}")
        
    except Exception as e:
        print(f"Error al leer el sensor: {e}")

# Ejecutar la lectura
if __name__ == "__main__":
    while True:
        leer_datos()
        time.sleep(5) # Espera 5 segundos antes de la siguiente lectura