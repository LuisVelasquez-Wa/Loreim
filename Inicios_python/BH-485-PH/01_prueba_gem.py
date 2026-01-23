from pymodbus.client import ModbusSerialClient
from pymodbus.constants import Endian
from pymodbus.payload import BinaryPayloadDecoder
import time

class SensorPHReader:
    """
    Clase simplificada para leer solo el valor de pH del sensor BH-485-PH.
    Versión compatible con Pymodbus 3.x
    """
    def __init__(self, port, baudrate=9600, slave_id=2):
        # Los parámetros se mantienen similares pero es mejor ser explícito
        self.client = ModbusSerialClient(
            port=port,
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1
        )
        self.slave_id = slave_id

    def conectar(self):
        if self.client.connect():
            print("Conexión establecida con el sensor")
            return True
        else:
            print("No se pudo conectar al sensor")
            return False

    def desconectar(self):
        self.client.close()
        print("Conexión cerrada.")

    def leer_ph(self):
        # Nota: 'slave' ahora se recomienda pasar como parámetro 'slave'
        response = self.client.read_holding_registers(
            address=0, 
            count=2,  
            slave=self.slave_id
        )

        if not response.isError():
            # CAMBIO CLAVE: Endian.BIG (en mayúsculas) para v3.x
            decoder = BinaryPayloadDecoder.fromRegisters(
                response.registers, 
                byteorder=Endian.BIG, 
                wordorder=Endian.BIG
            )
            return decoder.decode_32bit_float()
        else:
            print(f"Error de lectura: {response}")
            return None

if __name__ == "__main__":
    # ¡RECUERDA verificar si tu puerto es COM3 o algún otro en el Administrador de Dispositivos!
    PUERTO_SERIAL = 'COM1' 
    ID_ESCLAVO = 2 

    sensor = SensorPHReader(PUERTO_SERIAL, slave_id=ID_ESCLAVO)
    
    if sensor.conectar():
        try:
            while True:
                ph_value = sensor.leer_ph()
                if ph_value is not None:
                    print(f"Valor de pH medido: {ph_value:.2f}")
                time.sleep(2)
        except KeyboardInterrupt:
            print("\nLectura detenida por el usuario.")
        finally:
            sensor.desconectar()