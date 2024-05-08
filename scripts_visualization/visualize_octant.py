import json
import numpy as np
import matplotlib.pyplot as plt
import os

def visualize_octant(filename_json, filename_plot):
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
    for vertex, position in vertices.items():
        ax.scatter(*position)

    # Plot edges
    for edge in edges:
        points = [vertices[vertex] for vertex in edge]
        ax.plot(*zip(*points))

    # Plot
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.savefig(filename_plot)
    plt.show()

def visualize_octant_step(filename_json, filename_plot):
    # Load data
    with open(filename_json, 'r') as file:
        data = json.load(file)

    # Extract vertices and edges
    vertices = {vertex['name']: np.array(vertex['position']) for vertex in data['operations'] if 'position' in vertex}
    edges = [(edge['vertices'], edge['name']) for edge in data['operations'] if 'vertices' in edge]

    # Create 3D plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot vertices
    for vertex, position in vertices.items():
        ax.scatter(*position)

    # Plot edges
    for edge, edge_name in edges:
        points = [vertices[vertex] for vertex in edge]
        linestyle = '-'  # default linestyle
        linewidth = 5
        if edge_name.startswith("nt"):  # if edge is non-terminal
            linestyle = '--'  # dashed linestyle
            linewidth = 3
        ax.plot(*zip(*points), linestyle=linestyle,linewidth=linewidth)

    # Plot
    plt.savefig(filename_plot)
    plt.show()
