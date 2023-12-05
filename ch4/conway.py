import random, time, copy

width = 20
height = 20

initial_array = []

for x in range(width):
    initial_array.append([])
    for y in range(height):
        life = random.randint(0,1)
        if life == 0:
            initial_array[x].append(" ")
        else:
            initial_array[x].append("#")

while True:    
    for y in range(height):
        for x in range(width):
            print(initial_array[y][x], end="|")
        print()
    print("\n\n\n")

    next_array = copy.deepcopy(initial_array)

    for x in range(width):
        for y in range(height):
            left_x_coord = (x-1)
            right_x_coord = (x+1) % width
            upper_y_coord = (y-1)
            lower_y_coord = (y+1) % height
            living_neighbors = 0
            
            if initial_array[left_x_coord][upper_y_coord] == "#":
                living_neighbors +=1 #check upper left neighbor

            if initial_array[x][upper_y_coord] == "#":
                living_neighbors +=1 #check top neighbor

            if initial_array[right_x_coord][upper_y_coord] == "#":
                living_neighbors +=1 #check upper right neighbor

            if initial_array[left_x_coord][y] == "#":
                living_neighbors +=1 #check left neighbor

            if initial_array[right_x_coord][y] == "#":
                living_neighbors +=1 #check right neighbor

            if initial_array[left_x_coord][lower_y_coord] == "#":
                living_neighbors +=1 #check lower left neighbor

            if initial_array[x][lower_y_coord] == "#":
                living_neighbors +=1 #check bottom neighbor

            if initial_array[right_x_coord][lower_y_coord] == "#":
                living_neighbors +=1 #check lower right neighbor

            if initial_array[x][y] == "#":
                if living_neighbors == 2 or living_neighbors == 3:
                    next_array[x][y] = "#"
                else:
                    next_array[x][y] = " "
            else:
                if living_neighbors == 3:
                    next_array[x][y] = "#"

    initial_array = next_array
    time.sleep(1.5)
