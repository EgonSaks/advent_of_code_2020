data ='day10_input.txt'

with open(data, "r") as data:
    lines = [int(line.rstrip()) for line in data.readlines()]

one_jolt = 0
two_jolt = 0
three_jolt = 0 
outlet_rating = 0
lines.append(max(lines)+3) #max jolt is added


while True:
    #print(1 in lines)
    if (outlet_rating + 1) in lines:
        one_jolt+= 1
        outlet_rating += 1
    elif outlet_rating + 2 in lines:
        two_jolt += 1
    elif (outlet_rating + 3) in lines:
        three_jolt += 1
        outlet_rating += 3
    else:
        break

print("The number of 1-jolt differences multiplied by the number of 3-jolt differences is", one_jolt*three_jolt)

sol = {0:1}
for line in sorted(lines):
    sol[line] = 0
    if line - 1 in sol:
        sol[line] += sol[line-1]
    if line - 2 in sol:
        sol[line] += sol[line-2]
    if line - 3 in sol:
        sol[line] += sol[line-3]

print("The total number of distinct ways you can arrange the adapters to connect the charging outlet to your device is:",sol[max(lines)])