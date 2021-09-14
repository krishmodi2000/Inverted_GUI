import json
import os
import serial
import serial.tools.list_ports

commands = ['D', 'V', 'S', 'T', 'A']

ser_ports = serial.tools.list_ports.comports()
ports = [port.name for port in ser_ports]

ser = serial.Serial(ports[0], baudrate = 9600, timeout=20)

def json_create(commands=commands):
    if os.path.exists('data.json'):
        data = json_read()

    else:
        data = {
            commands[0]: 
            {
                'chemistry': 'NMC',
                'no of cells': 16,
                'design capacity': 40,
                'minimum voltage': 48,
                'nominal voltage': 57.6,
                'maximum voltage': 67.2,
            },

            commands[1]: 
            {
                'cell voltages': ['xxxx']*16,
            },

            commands[2]: 
            {
                'battery voltage': 'xx',
                'total current': 'xx',
                'soc': 98,
                'status': 'Charging',
                'mosfet status': [1, 0]
            },

            commands[3]: 
            {
                'temperature': ['xxx']*4,
                'mosfet temperature': 'xxx'
            },

            commands[4]: 
            {
                'alarms': [0, 0, 0, 0, 0]
            },
        }
    
        with open('data.json', 'w') as outfile:
                json.dump(data, outfile)

    return data

def json_read():
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)

    return data

def json_write(signal, ser):
    data = json_read()

    if signal == commands[0]:
        ser.wirte(commands[0])
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]


    elif signal == commands[1]:
        ser.wirte(commands[1])
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

    elif signal == commands[2]:
        ser.wirte(commands[2])
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

    elif signal == commands[3]:
        ser.wirte(commands[3])
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

    elif signal == commands[4]:
        ser.wirte(commands[4])
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]






