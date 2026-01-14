import minimalmodbus
import serial
import time

# Colocamos las variables
PUERTO = '/dev/ttyUSB0' 
ID_BOMBA = 1

# Leer los parametros, si no error
try:
    bomba = minimalmodbus.Instrument(PUERTO, ID_BOMBA)
    
    bomba.serial.baudrate = 9600
    bomba.serial.timeout = 1

except Exception as e:
    print(f"Error: {e}")
    exit()

# Definimos la velocidad de la bomba, si no error

def ajustar_velocidad(valor_rpm):
    try:
        bomba.write_register(10, valor_rpm, functioncode = 6)
        print(f"Velocidad del motor ajustado a: {valor_rpm} RPM")

    except Exception as e:
        print(f"Error al escribir la velocidad: {e}")

if __name__ == "__main__":
    while True:
        nueva_vel = int(input("Coloca la velocidad (RPM): "))
        ajustar_velocidad(nueva_vel)


    