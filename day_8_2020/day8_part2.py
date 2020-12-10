data = 'day8_input.txt'

with open(data) as data:
    data = [{'operation': line[:3], 'parameter': int(line[4:])} for line in data.read().split('\n')]

accumulator = 0
position = 0
previous_position  = set()

def command_acc(position, parameter):
    global accumulator
    
    accumulator += parameter
    return position + 1

def command_jmp(position, parameter):
    return position + parameter

def command_nop(position, parameter):
    return position + 1

command = {
    'acc': command_acc,
    'jmp': command_jmp,
    'nop': command_nop
}

while True:
    if position in previous_position:
        break
    previous_position.add(position)
    position = command[data[position]['operation']](position, data[position]['parameter'])

def run(data):
    global accumulator
    
    accumulator = 0
    address     = 0
    been_there  = set()
    while True:
        if address in been_there:
            break
        been_there.add(address)
        if address == len(data):
            break
        address = command[data[address]['operation']](address, data[address]['parameter'])
    
    return {'address': address, 'accumulator': accumulator}

import copy
import pandas as pd

df = pd.DataFrame(data)
failed_runs = 0
for idx, line in df[df['operation'].isin({'nop', 'jmp'})].iterrows():
    data_patched = copy.deepcopy(data)
    if data_patched[idx]['operation'] == 'jmp':
        data_patched[idx]['operation'] = 'nop'
    elif data_patched[idx]['operation'] == 'nop':
        data_patched[idx]['operation'] = 'jmp'
    result = run(data_patched)
    if result['address'] == len(data_patched):
        break
    failed_runs += 1

print('Value of the accumulator after the program terminates is: %d (failed runs: %d)' % (result['accumulator'], failed_runs))
