import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random

num_points = 1000
x_coords = np.random.randint(0, 1000, num_points)
y_coords = np.random.randint(0, 1000, num_points)

df = pd.DataFrame({'x': x_coords, 'y': y_coords})
df.to_excel('coordinates.xlsx', index=False)

grid_size = 200
x_grid = np.floor_divide(x_coords, grid_size)
y_grid = np.floor_divide(y_coords, grid_size)

unique_grids = set(zip(x_grid, y_grid))
grid_to_color = {grid: [random.random(), random.random(), random.random()] for grid in unique_grids}

plt.figure(figsize=(10, 10))
for grid, color in grid_to_color.items():
    grid_points = (x_grid == grid[0]) & (y_grid == grid[1])
    plt.scatter(x_coords[grid_points], y_coords[grid_points], color=color, label=f'Grid {grid}')

plt.title('Random Points with Grid Coloring')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.grid(True)
plt.legend()
plt.savefig('points_grid_visualization.jpeg')  # Burada dosya yolu düzeltildi
plt.show()
