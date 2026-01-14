from pymodbus.client import ModbusSerialClient
from pymodbus.payload import BinaryPayloadDecoder
from pymodbus.constants import Endian
import time

class SensorPHReader:
    def __init__(self, port, baudrate=9600, slave_id=2):
        self.client = ModbusSerialClient(
            port=port,
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1
        )
        self.slave_id = slave_id

    def conectar(self):                 #Intenta establecer la conexión serial

        if self.client.connect():
            print("Conexión establecida al sensor")
            return True
        else:
            print("No se pudo conectar al sensor")
            return False

    def desconectar(self):
        """Cierra la conexión."""
        self.client.close()
        print("Conexión cerrada.")

    def leer_ph(self):
        """Lee el valor float de 32 bits desde la dirección de pH (dirección 0)."""
        # La dirección 0 requiere 2 registros (count=2) para un float de 32 bits.
        response = self.client.read_holding_registers(
            address=0, 
            count=2,  
            slave=self.slave_id
        )

        if not response.isError():
            decoder = BinaryPayloadDecoder.fromRegisters(
                response.registers, 
                byteorder=Endian.Big, 
                wordorder=Endian.Big
            )
            # Retorna el valor decodificado
            return decoder.decode_32bit_float()
        else:
            raise Exception(f"Error de lectura en la dirección 0: {response}")

# --- Parte principal del programa ---
if __name__ == "__main__":
    # IMPORTANTE: Reemplaza 'COM3' con el nombre de tu puerto serial real.
    PUERTO_SERIAL = 'COM1' 
    ID_ESCLAVO = 2 

    sensor = SensorPHReader(PUERTO_SERIAL, slave_id=ID_ESCLAVO)
    
    if sensor.conectar():
        try:
            while True:
                ph_value = sensor.leer_ph()
                if ph_value is not None:
                    print(f"Valor de pH: {ph_value:.2f}")
                time.sleep(2) # Espera 2 segundos antes de la siguiente lectura
        except KeyboardInterrupt:
            print("Lectura de pH detenida por el usuario.")
        finally:
            sensor.desconectar()