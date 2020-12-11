with open("day9_input.txt", "r") as fp:
    lines = [int(line.rstrip()) for line in fp.readlines()]
# lines

def challenge1(codes, premable):
    previous_stack = []
    i = 0
    start = 0
    end = start+premable
    curr_index = premable
    while curr_index < len(codes)-1:
        stack = codes[start:end]
        if curr_index > len(stack)-1:
            start+=1
            end+=1
            valid = False
            for i in stack[:-1]:
                for j in stack[1:]:
                    #print(codes[curr_index], i, j)
                    if i+j == codes[curr_index]:
                        valid = True
                        break
                    else:
                        valid == False
                if valid:
                    break
            if valid == False:
                return codes[curr_index]

        curr_index+=1
#         print(stack)
#         break

challenge1(lines, 25)

import numpy as np
def challenge2(codes, invalid_num):
    contigous_list = []

    for i in range(0, len(codes)-1):
        for j in range(1, len(codes)-1):
            stack = np.array(codes[i:j])
            if np.sum(stack) == invalid_num:
                print(stack, stack.min()+stack.max())

challenge2(lines, challenge1(lines, 25))