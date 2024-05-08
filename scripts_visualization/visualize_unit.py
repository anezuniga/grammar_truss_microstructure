import json
import numpy as np
import matplotlib.pyplot as plt
import os

def visualize_unit(filename_json, filename_plot):
    # Load data
    with open(filename_json, 'r') as file:
        data = json.load(file)

    # Extract vertices and edges
    vertices = {vertex['name']: np.array(vertex['position']) for vertex in data['operations'] if 'position' in vertex}
    edges = [edge['vertices'] for edge in data['operations'] if 'vertices' in edge]

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot vertices
    i = 0
    for vertex, position in vertices.items():
        i+=1
        total = 8 # Total number of octants in the unit cell (or units in the lattice)
        if (i > 2*len(vertices)/total) & (i < 3*len(vertices)/total+1):
            paint = "r"
        else:
            paint = "b"
        ax.scatter(*position, color=paint)

    # Plot edges
    i = 0
    for edge in edges:
        i+=1
        if (i > 2*len(edges)/total) & (i < 3*len(edges)/total+1):
            paint = "r"
        else:
            paint = "b"
        points = [vertices[vertex] for vertex in edge]
        ax.plot(*zip(*points), color=paint)

    # Plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig(filename_plot)
    plt.show()
