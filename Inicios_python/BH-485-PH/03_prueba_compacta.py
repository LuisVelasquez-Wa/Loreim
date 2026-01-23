import minimalmodbus
inst = minimalmodbus.Instrument('COM1', 2)
inst.serial.baudrate = 9600
inst.mode = minimalmodbus.MODE_RTU

ph = round(inst.read_register(1, 2) * 0.01, 2)
temp = round(inst.read_register(0, 1) * 0.1, 1)
print(f"pH={ph}, Temp={temp}°C")