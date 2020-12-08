with open('day7_input.txt') as file:
    luggage_list = file.readlines()
    luggage_list = [ line.strip() for line in luggage_list]

def get_number_of_bags(color):
    lines = [ line for line in luggage_list if color in line and line.index(color)!= 0 ] 
    
    allColors = []
    
    if len(lines) == 0:
        return []
    
    else:
        colors = [ line[:line.index(' bags')] for line in lines ]
        colors = [ color for color in colors if color not in allColors ]
        
        for color in colors:
            allColors.append(color)
            bags = get_number_of_bags(color)
            
            allColors += bags
            
        uniqueColors = []
        for color in allColors:
            if color not in uniqueColors:
                uniqueColors.append(color)
                
        return uniqueColors
            
colors = get_number_of_bags('shiny gold')
print(len(colors))