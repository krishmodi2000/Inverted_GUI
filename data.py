import json
import os

def json_create():
    if os.path.exists('data.json'):
        data = json_read()

    else:
        data = {
            'D': {

                'chemistry': 'NMC',
                'no of cells': 16,
                'design capacity': 40,
                'minimum voltage': 48,
                'nominal voltage': 57.6,
                'maximum voltage': 67.2,
            },

            'V': {
                'cell voltages': ['xxxx']*16,
            },

            'S': {
                'battery voltage': 'xx',
                'total current': 'xx',
                'soc': 98,
                'status': 'Charging',
                'mosfet status': [1, 0]
            },

            'T': {
                'temperature': ['xxx']*4,
                'mosfet temperature': 'xxx'
            },

            'A': {
                'alarms': [0, 0, 0, 0, 0]
            },
        }
    
        with open('data.json', 'w') as outfile:
                json.dump(data, outfile)

    return data

def json_write(signal, string):
    data = json_read()

    keys = data.keys()

    for key, val in data[signal].items():
        pass

    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)

def json_read():
    with open('data.json', 'r') as outfile:
        data = json.load(outfile)

    return data

