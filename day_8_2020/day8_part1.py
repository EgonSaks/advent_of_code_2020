data = 'day8_input.txt'

# Get data and clean it
with open(data) as data:
    data = [{'operation': line[:3], 'parameter': int(line[4:])} for line in data.read().split('\n')]


accumulator = 0
# Current position
position = 0
# Previous position
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
    
previous_position, position, accumulator

print(f'Value in the accumulator is: {accumulator}')