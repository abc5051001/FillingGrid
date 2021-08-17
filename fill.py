def fill(grid, old_value, new_value, seed):
	if (seed[0]<0 or seed[0]>len(grid)-1 or seed[1]<0 or seed[1]>len(grid[0])-1):
		return 
# where the length exceeds
	else:
		if(grid[seed[0]][seed[1]] == old_value):
# the base case
			grid[seed[0]][seed[1]] = new_value
			fill(grid, old_value, new_value, (seed[0]+1,seed[1]))
# check right
			fill(grid, old_value, new_value, (seed[0]-1,seed[1]))
# check left
			fill(grid, old_value, new_value, (seed[0],seed[1]+1))
# check down
			fill(grid, old_value, new_value, (seed[0],seed[1]-1))
# check up
			fill(grid, old_value, new_value, (seed[0]-1,seed[1]-1))
# up left 
			fill(grid, old_value, new_value, (seed[0]+1,seed[1]-1))
# up right
			fill(grid, old_value, new_value, (seed[0]+1,seed[1]+1))
# down right
			fill(grid, old_value, new_value, (seed[0]-1,seed[1]+1))
# down left
		return
