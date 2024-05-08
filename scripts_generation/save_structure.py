import json
import numpy as np

def generate_json(vertices, edges, file_name):

    operations = []

    # Add vertices
    for vertex, position in vertices.items():
        operations.append({
            "name": vertex,
            "position": position
        })

    # Add edges
    for edge, vertices in edges.items():
        operations.append({
            "name": edge,
            "smooth": False,
            "vertices": vertices
        })

    # Final structure
    truss_structure = {
        "operations": operations
    }

    # Save file
    with open(file_name, 'w') as file:
        json.dump(truss_structure, file, indent=4)

    print(f'Truss structure saved to {file_name}')

