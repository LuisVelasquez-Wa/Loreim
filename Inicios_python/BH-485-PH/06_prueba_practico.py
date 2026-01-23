import minimalmodbus
import serial
import time

# 1. Configuración del Sensor
# En Windows usa 'COM1', 'COM2', etc. En Linux usa '/dev/ttyUSB0'
PUERTO = 'COM1' 
ID_ESCLAVO = 2  # El ID por defecto según el manual

try:
    sensor = minimalmodbus.Instrument(PUERTO, ID_ESCLAVO)
    
    # Ajustes de comunicación según el manual
    sensor.serial.baudrate = 9600
    sensor.serial.bytesize = 8
    sensor.serial.parity = serial.PARITY_NONE
    sensor.serial.stopbits = 1
    sensor.serial.timeout = 1
    sensor.mode = minimalmodbus.MODE_RTU # Modo de transmisión RTU
    
except Exception as e:
    print(f"Error al inicializar puerto: {e}")
    exit()

def leer_datos():
    try:
        # 2. Lectura de Temperatura (Registro 0)
        # Se multiplica por 0.1 como indica el manual
        temp_raw = sensor.read_register(0, 0)
        temperatura = temp_raw * 0.1
        
        # 3. Lectura de pH (Registro 1)
        # Se multiplica por 0.01 como indica el manual
        ph_raw = sensor.read_register(1, 0)
        ph = ph_raw * 0.01
        
        print(f"--- Lectura del Sensor BH-485-PH ---")
        print(f"Temperatura: {temperatura:.1f} °C")
        print(f"Valor de pH: {ph:.2f}")
        
    except Exception as e:
        print(f"Error al leer el sensor: {e}")

# Ejecución
if __name__ == "__main__":
    while True:
        leer_datos()
        time.sleep(2) # Espera 2 segundos entre lecturas