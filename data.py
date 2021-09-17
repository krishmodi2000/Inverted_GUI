import json
import os
import serial
import serial.tools.list_ports

commands = ['D', 'V', 'S', 'T', 'A']

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
                'maximum voltage': 67.2
            },

            commands[1]:
            {
                'cell voltages': ['xxxx']*16
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

def json_write(signal, port, baudrate = 9600, commands = commands):
    data = json_read()

    ser = serial.Serial(port, baudrate = baudrate, timeout=5)

    if not ser.is_open:
        ser.open()

    if signal == commands[0]:
        ser.write(b'D')
        line = ser.readline().decode("ascii")
        print(line)
        print('1')
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

            data[commands[0]] = {
                'chemistry': line[0],
                'no of cells': line[1],
                'design capacity': line[2],
                'minimum voltage': line[3],
                'nominal voltage': line[4],
                'maximum voltage': line[5]
            } 



    elif signal == commands[1]:
        ser.write(bytes(commands[1]))
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

            data[commands[1]] = {
                'cell voltages': line,
                'max voltage': max(line),
                'min voltage': min(line),
                'avg voltage': sum(line)/len(line),
                'difference': abs(max(line)-min(line))
            }



    elif signal == commands[2]:
        ser.write(bytes(commands[2]))
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

            if line[3] == 1:
                status = 'Charging'
            elif line[4] == 1:
                status = 'Discharging'
            else:
                status = 'Idle'


            data[commands[2]] = {
                'battery voltage': line[0],
                'total current': line[1],
                'soc': line[2],
                'status': status,
                'mosfet status': [line[3], line[4]]
            }

    elif signal == commands[3]:
        ser.write(bytes(commands[3]))
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]

            data[commands[3]] = {
                'temperature': line[:4],
                'mosfet temperature': line[-1]
            },

    elif signal == commands[4]:
        ser.write(bytes(commands[4]))
        line = ser.readline().decode("ascii")
        if line[0] == '#':
            line = line.lstrip('#')
            line = line.rstrip()
            line = line.split(',')
            line = [int(l) if l.isnumeric() == True else l for l in line]
            
            data[commands[4]] = {
                'alarms': line
            }


    with open('data.json', 'w') as outfile:
                json.dump(data, outfile)

    ser.close()

    return data

ser_ports = serial.tools.list_ports.comports()
ports = [port.name for port in ser_ports]

print(ports)

json_create()

data = json_read()
print(data)

data = json_write('D', ports[0])
print(data)

data = json_write('T', ports[0])
print(data)






