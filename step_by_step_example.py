import os
import numpy as np
from scripts_generation.initial_vertices import check_custom_initial, format_vertices
from scripts_generation.connections import format_edges_step
from scripts_generation.save_structure import generate_json
from scripts_visualization.visualize_octant import visualize_octant_step

# Directories
folder_json = 'structures_step/json'
folder_plot_octant = 'structures_step/plots_octant'

if not os.path.exists(folder_json):
    os.makedirs(folder_json)
if not os.path.exists(folder_plot_octant):
    os.makedirs(folder_plot_octant)

# Define vertices_octant and edges_octant for each iteration
for i in range(7):  # Loop from 0 to 6
    filename = f'2FCC_3_step_{i}'  # Adjust filename accordingly
    filename_json_octant = f"{folder_json}/{filename}.json"
    filename_plot_octant = f"{folder_plot_octant}/{filename}.png"

    vertices_octant =  [[0, 0, 1],
                        [0, 1, 0],
                        [1, 0, 0],
                        [1, 1, 1]]

    # Define edges_octant based on iteration
    if i == 0:
        edges_octant = [[1, -1, -1, -1],
                        [-1, 1, -1, -1],
                        [-1, -1, 1, -1],
                        [-1, -1, -1, 1]]
    elif i == 1:
        edges_octant = [[1, 1, -1, -1],
                        [1, 1, -1, -1],
                        [-1, -1, 1, -1],
                        [-1, -1, -1, 1]]
    elif i == 2:
        edges_octant = [[1, 1, 1, -1],
                        [1, 1, -1, -1],
                        [1, -1, 1, -1],
                        [-1, -1, -1, 1]]
    elif i == 3:
        edges_octant = [[1, 1, 1, -1],
                        [1, 1, 1, -1],
                        [1, 1, 1, -1],
                        [-1, -1, -1, 1]]
    elif i == 4:
        edges_octant = [[1, 1, 1, -1],
                        [1, 1, 1, 1],
                        [1, 1, 1, -1],
                        [-1, 1, -1, 1]]
    elif i == 5:
        edges_octant = [[1, 1, 1, -1],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [-1, 1, 1, 1]]
    elif i == 6:
        edges_octant = [[1, 1, 1, 0],
                        [1, 1, 1, 1],
                        [1, 1, 1, 1],
                        [0, 1, 1, 1]]

    # Save structure
    generate_json(format_vertices(vertices_octant), format_edges_step(edges_octant), filename_json_octant)

    # Visualize
    visualize_octant_step(filename_json_octant, filename_plot_octant)
