import minimalmodbus
import serial

class BHPHSensor:
    def __init__(self, port='COM1', addr=2, baud=9600):
        self.instrument = minimalmodbus.Instrument(port, addr)
        self.instrument.serial.baudrate = baud
        self.instrument.serial.parity = serial.PARITY_NONE
        self.instrument.mode = minimalmodbus.MODE_RTU
    
    def read_data(self):
        """Lee temperatura y pH en una sola llamada"""
        try:
            # Leer 2 registros seguidos (temperatura y pH)
            data = self.instrument.read_registers(0, 2)
            temp = round(data[0] * 0.1, 1)  # Registro 0
            ph = round(data[1] * 0.01, 2)   # Registro 1
            return {'temp': temp, 'ph': ph}
        except:
            return {'temp': None, 'ph': None}

# Uso rápido
sensor = BHPHSensor(port='COM1')  # Ajusta el puerto
datos = sensor.read_data()
print(f"Temperatura: {datos['temp']}°C, pH: {datos['ph']}")