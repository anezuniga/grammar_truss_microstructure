import random
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(project_root)

from scripts_generation.initial_vertices import generate_initial_vertices, format_vertices
from scripts_generation.connections import initial_connection, format_edges, get_intermediate_indexes, add_connection, remove_connection
from scripts_generation.save_structure import generate_json
from scripts_generation.mirror import get_vertices_unit, get_edges_unit
from scripts_generation.translate import get_vertices_lattice, get_edges_lattice
from scripts_generation.feasibility import fulfill_vertex, find_largest_connected_vertices

prob_connection = 0.1
precision = 1 # 1 referrs to 0.1
n_dataset = 10000
v_max_extra_face = 5
v_max_extra_body = 5

# Seed
for seed in range(n_dataset):
    random.seed(seed)
    v_extra_face = random.randint(0, v_max_extra_face)
    v_extra_body = random.randint(0, v_max_extra_body)

    # Octant
    vertices_octant = generate_initial_vertices(v_extra_face, v_extra_body, precision)
    num_total_vertices = len(vertices_octant)

    # Edge connections
    edges_octant = initial_connection(vertices_octant)
    tot_edges = len(get_intermediate_indexes(edges_octant))
    for _ in range (tot_edges):
        intermediate_idx = get_intermediate_indexes(edges_octant)
        selected_idx = random.choice(intermediate_idx)
        v1 = selected_idx[0]
        v2 = selected_idx[1]
        v1_fulfill = fulfill_vertex(vertices_octant, v1, edges_octant)
        v2_fulfill = fulfill_vertex(vertices_octant, v2, edges_octant)

        num_connected = find_largest_connected_vertices(edges_octant)
        all_connected = num_connected == num_total_vertices

        if v1_fulfill == True and v2_fulfill == True and all_connected == True:
            if random.random() < prob_connection:
                # Terminal connection
                edges_octant = add_connection(edges_octant, v1, v2)
            else:
                # Terminal disconnection
                edges_octant = remove_connection(edges_octant, v1, v2)
        else:
            # Terminal connection
            edges_octant = add_connection(edges_octant, v1, v2)

    # Unit cell
    vertices_unit = get_vertices_unit(vertices_octant)
    edges_unit = get_edges_unit(edges_octant)

    # Lattice
    vertices_lattice = get_vertices_lattice(vertices_unit)
    edges_lattice = get_edges_lattice(edges_unit)

    # Save structure
    folder_json = 'dataset'
    if not os.path.exists(folder_json):
        os.makedirs(folder_json)
    filename_octant = f'{folder_json}/truss_{seed}_octant.json' 
    filename_unit = f'{folder_json}/truss_{seed}_unit.json' 
    generate_json(format_vertices(vertices_octant), format_edges(edges_octant), filename_octant)
    generate_json(format_vertices(vertices_unit), format_edges(edges_unit), filename_unit)
