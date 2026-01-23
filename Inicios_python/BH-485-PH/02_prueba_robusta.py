import minimalmodbus
import serial
import struct

class BHPHSensor:
    def __init__(self, port, slave_address=2, baudrate=9600):
        """
        Inicializa el sensor BH-485-PH
        
        Args:
            port: Puerto serial (ej: 'COM3' en Windows, '/dev/ttyUSB0' en Linux)
            slave_address: Dirección Modbus del dispositivo (por defecto 2)
            baudrate: Velocidad de comunicación (4800, 9600, 19200)
        """
        try:
            self.instrument = minimalmodbus.Instrument(port, slave_address)
            self.instrument.serial.baudrate = baudrate
            self.instrument.serial.bytesize = 8
            self.instrument.serial.parity = serial.PARITY_NONE
            self.instrument.serial.stopbits = 1
            self.instrument.serial.timeout = 1.0  # segundos
            self.instrument.mode = minimalmodbus.MODE_RTU
            self.instrument.clear_buffers_before_each_transaction = True
            
            print(f"Sensor BH-485-PH inicializado en {port}")
            print(f"Dirección: {slave_address}, Baudrate: {baudrate}")
            
        except Exception as e:
            print(f"Error al inicializar el sensor: {e}")
            raise
    
    def read_temperature(self):
        """
        Lee la temperatura del sensor
        
        Returns:
            Temperatura en °C con 1 decimal
        """
        try:
            # Dirección 0: Temperatura (registro 0000)
            raw_value = self.instrument.read_register(0, 1)
            temperature = raw_value * 0.1  # Multiplicador de 0.1°C
            return round(temperature, 1)
        except Exception as e:
            print(f"Error al leer temperatura: {e}")
            return None
    
    def read_ph(self):
        """
        Lee el valor de pH del sensor
        
        Returns:
            Valor de pH con 2 decimales
        """
        try:
            # Dirección 1: pH (registro 0001)
            raw_value = self.instrument.read_register(1, 2)
            ph_value = raw_value * 0.01  # Multiplicador de 0.01pH
            return round(ph_value, 2)
        except Exception as e:
            print(f"Error al leer pH: {e}")
            return None
    
    def read_mv(self):
        """
        Lee el valor en mV del sensor
        
        Returns:
            Valor en mV con 1 decimal
        """
        try:
            # Dirección 3: mV (registro 0003)
            # Nota: Este valor puede ser negativo, necesitamos manejar números con signo
            raw_value = self.instrument.read_register(3, 1)
            
            # Convertir a entero con signo si es necesario
            if raw_value > 32767:  # Para valores negativos en complemento a 2
                raw_value = raw_value - 65536
            
            mv_value = raw_value * 0.1  # Multiplicador de 0.1mV
            return round(mv_value, 1)
        except Exception as e:
            print(f"Error al leer mV: {e}")
            return None
    
    def read_temperature_status(self):
        """
        Lee el estado del sensor de temperatura
        
        Returns:
            0: normal
            1: temperatura demasiado alta/baja
            2: sin sensor
        """
        try:
            # Dirección 5: Estado de temperatura
            status = self.instrument.read_register(5, 0)
            status_messages = {
                0: "Normal",
                1: "Temperatura demasiado alta/baja",
                2: "Sensor de temperatura no detectado"
            }
            return status, status_messages.get(status, "Estado desconocido")
        except Exception as e:
            print(f"Error al leer estado de temperatura: {e}")
            return None
    
    def read_all_data(self):
        """
        Lee todos los datos principales del sensor
        
        Returns:
            Diccionario con todos los valores
        """
        data = {}
        
        # Leer datos individuales
        data['temperature'] = self.read_temperature()
        data['ph'] = self.read_ph()
        data['mv'] = self.read_mv()
        data['temperature_status'] = self.read_temperature_status()
        
        return data
    
    def set_device_address(self, new_address):
        """
        Cambia la dirección del dispositivo
        
        Args:
            new_address: Nueva dirección (1-254)
        """
        try:
            if 1 <= new_address <= 254:
                self.instrument.write_register(8, new_address, 0)
                print(f"Dirección del dispositivo cambiada a: {new_address}")
            else:
                print("Error: La dirección debe estar entre 1 y 254")
        except Exception as e:
            print(f"Error al cambiar dirección: {e}")
    
    def set_baudrate(self, baudrate):
        """
        Cambia el baudrate del dispositivo
        
        Args:
            baudrate: 4800, 9600 o 19200
        """
        try:
            if baudrate in [4800, 9600, 19200]:
                self.instrument.write_register(9, baudrate, 0)
                print(f"Baudrate cambiado a: {baudrate}")
            else:
                print("Error: Baudrate debe ser 4800, 9600 o 19200")
        except Exception as e:
            print(f"Error al cambiar baudrate: {e}")
    
    def reset_to_default(self):
        """Restablece el dispositivo a valores por defecto"""
        try:
            self.instrument.write_register(10, 1996, 0)
            print("Dispositivo restablecido a valores por defecto")
        except Exception as e:
            print(f"Error al restablecer: {e}")
    
    def device_reset(self):
        """Reinicia el dispositivo"""
        try:
            self.instrument.write_register(11, 1524, 0)
            print("Dispositivo reiniciado")
        except Exception as e:
            print(f"Error al reiniciar: {e}")
    
    def calibrate_zero(self):
        """
        Calibración de punto cero (buffer pH 7.00 o 6.86)
        
        Nota: El electrodo debe estar en la solución buffer antes de ejecutar
        """
        try:
            self.instrument.write_register(13, 1, 0)
            print("Calibración de punto cero iniciada")
            print("Asegúrese de que el electrodo esté en buffer pH 7.00 o 6.86")
        except Exception as e:
            print(f"Error en calibración de punto cero: {e}")
    
    def calibrate_slope(self):
        """
        Calibración de pendiente (buffer pH 4.00 o 10.00)
        
        Nota: El electrodo debe estar en la solución buffer antes de ejecutar
        """
        try:
            self.instrument.write_register(13, 2, 0)
            print("Calibración de pendiente iniciada")
            print("Asegúrese de que el electrodo esté en buffer pH 4.00 o 10.00")
        except Exception as e:
            print(f"Error en calibración de pendiente: {e}")

def main():
    """
    Ejemplo de uso del sensor BH-485-PH
    """
    # Configuración - ¡AJUSTA ESTOS VALORES!
    PORT = 'COM1'  # Puerto serial en Windows
    # PORT = '/dev/ttyUSB0'  # Puerto serial en Linux
    SLAVE_ADDRESS = 2
    BAUDRATE = 9600
    
    try:
        # Crear instancia del sensor
        sensor = BHPHSensor(
            port=PORT,
            slave_address=SLAVE_ADDRESS,
            baudrate=BAUDRATE
        )
        
        # Leer todos los datos
        print("\n=== Leyendo datos del sensor ===")
        data = sensor.read_all_data()
        
        # Mostrar resultados
        if data['temperature'] is not None:
            print(f"Temperatura: {data['temperature']} °C")
        
        if data['ph'] is not None:
            print(f"pH: {data['ph']}")
        
        if data['mv'] is not None:
            print(f"mV: {data['mv']} mV")
        
        if data['temperature_status'] is not None:
            status_code, status_msg = data['temperature_status']
            print(f"Estado temperatura: {status_code} - {status_msg}")
        
        print("\n=== Fin de lectura ===")
        
    except Exception as e:
        print(f"Error: {e}")
        print("\nPosibles soluciones:")
        print("1. Verifica que el puerto serial sea correcto")
        print("2. Verifica la conexión del cable RS485")
        print("3. Verifica la alimentación del sensor (9-36V DC)")
        print("4. Verifica que la dirección Modbus sea correcta")
        print("5. Verifica los parámetros de comunicación (baudrate, paridad, etc.)")

if __name__ == "__main__":
    main()