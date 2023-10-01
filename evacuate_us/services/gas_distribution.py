import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
room_size = (40, 40)
diffusion_rate = 1
gas_release_rate = 1000000
time_steps = 10

# Initialize room, gas concentration, and walls
room = np.zeros(room_size)
gas_concentration = np.zeros(room_size)
walls = np.zeros((40, 40))
for i in range(40):
    for j in range(40):
        if (i == 6 or j == 6) and i + j > 6 and not i > 10 and not j > 10:
            walls[i][j] = 1
start_point = (10, 10)
gas_concentration[start_point] = 10

# Create a figure for visualization
fig, ax = plt.subplots()

# Define a colormap with white for walls
cmap = plt.get_cmap('hot')
cmap.set_bad('white', 1.0)


# Define a function to update the animation at each time step
def update(frame):
    global gas_concentration
    new_gas_concentration = np.zeros(room_size)
    for i in range(room_size[0]):
        for j in range(room_size[1]):
            if not walls[i, j]:  # Check if the cell is not a wall
                neighbors = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
                neighbor_average = np.mean([gas_concentration[x, y] for x, y in neighbors if 0 <= x < room_size[0] and 0 <= y < room_size[1] and not walls[x, y]])
                new_gas_concentration[i, j] = gas_concentration[i, j] + diffusion_rate * (neighbor_average - gas_concentration[i, j])
    gas_concentration = new_gas_concentration
    gas_concentration[start_point] += gas_release_rate

    ax.clear()
    ax.imshow(gas_concentration, cmap=cmap, interpolation='nearest')
    ax.set_title(f"Gas Distribution (Step {frame})")

def animate():
    ani = animation.FuncAnimation(fig, update, frames=time_steps, interval=10)
    # Display the animation
    plt.show()