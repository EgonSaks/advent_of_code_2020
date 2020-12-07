from typing import List
from math import floor

def row_and_column_finder(seat: str, rows: int = 128, cols: int = 8, row_lower: str = 'F', row_upper: str = 'B', col_lower: str = 'L', col_upper: str = 'R') -> List[int]:

    row_lower_bound = 0
    row_upper_bound = rows # Takes parameter from type hints, 128
    row_number = floor(row_lower_bound + (row_upper_bound - row_lower_bound)/2) # (0 + (128 - 0)/2)

    row_lower_half = [row_lower_bound, row_number] 	# [0, 64]
    row_upper_half = [row_number, row_upper_bound]	# [64, 128]

    col_lower_bound = 0
    col_upper_bound = cols # Takes parameter from type hints, 8
    col_number = floor(col_lower_bound + (col_upper_bound - col_lower_bound)/2) # (0 + (8 - 0)/2)

    col_lower_half = [col_lower_bound, col_number] 	# [0, 4]
    col_upper_half = [col_number, col_upper_bound]	# [4, 8]

    for code in seat:

        if code == row_lower: # Takes row_lower parameter from type hints

            row_lower_bound = row_lower_half[0]  # 0
            row_upper_bound = row_lower_half[1]  # 64

            # This is the middle point
            row_number = floor(row_lower_bound + (row_upper_bound - row_lower_bound)/2) # (0+ ( 64-0)/2) = 32

            row_lower_half = [row_lower_bound, row_number] # [0, 32]
            row_upper_half = [row_number, row_upper_bound] # [32, 64]

        elif code == row_upper: # Takes row_upper parameter from type hints

            row_lower_bound = row_upper_half[0] # 64
            row_upper_bound = row_upper_half[1] # 128

            # This is the middle point
            row_number = floor(row_lower_bound + (row_upper_bound - row_lower_bound)/2) # (64 + (128-64)/2) = 96

            row_lower_half = [row_lower_bound, row_number] # [64, 96]
            row_upper_half = [row_number, row_upper_bound] # [96, 128]

        elif code == col_lower: # Takes col_lower parameter from type hints

            col_lower_bound = col_lower_half[0] # [0]
            col_upper_bound = col_lower_half[1] # [4]

            # This is the middle point
            col_number = floor(col_lower_bound + (col_upper_bound - col_lower_bound)/2) # (0 + (4-0)/2) = 2

            col_lower_half = [col_lower_bound, col_number] # [0, 2]
            col_upper_half = [col_number, col_upper_bound] # [2, 4]

        elif code == col_upper: # Takes col_lower parameter from type hints

            col_lower_bound = col_upper_half[0] # [4]
            col_upper_bound = col_upper_half[1] # [8]

            # This is the middle point
            col_number = floor(col_lower_bound + (col_upper_bound - col_lower_bound)/2) # (4 + (8-4)/2) = 6

            col_lower_half = [col_lower_bound, col_number] # [4, 6]
            col_upper_half = [col_number, col_upper_bound] # [6, 8]

        # print(row_number, col_number) 

    return [row_number, col_number]

# Unique seat ID: multiply the row by 8, then add the column
def get_seat_id(row_col: List[int]) -> int:

    row = row_col[0]
    col = row_col[1]

    seat_id = (row * 8) + col

    return seat_id

# Input --------------------------------------------

seat_map = open('day5_input.txt', 'r').readlines()
seat_map = [x.strip() for x in seat_map]

# List of seat_id's
seat_ids = []


for seat in seat_map:
    result = row_and_column_finder(seat)
    seat_id = get_seat_id(result)
    seat_ids.append(seat_id)

#print(f"Seat ID-s: {seat_ids}")

smallest_seat_ID = min(seat_ids)
highest_seat_ID = max(seat_ids)

print(f"Smallest seat ID: {smallest_seat_ID}")
print(f"Highest seat ID: {highest_seat_ID}")

my_seat_ID = [seat for seat in range(min(seat_ids), max(seat_ids)) if seat not in seat_ids][0] 

print(f"My seat ID is: {my_seat_ID}")