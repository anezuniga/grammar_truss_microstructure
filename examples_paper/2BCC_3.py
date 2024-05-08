import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(project_root)

from scripts_generation.initial_vertices import check_custom_initial, format_vertices
from scripts_generation.connections import all_connection, format_edges
from scripts_generation.save_structure import generate_json
from scripts_visualization.visualize_octant import visualize_octant
from scripts_visualization.visualize_unit import visualize_unit
from scripts_visualization.visualize_lattice import visualize_lattice
from scripts_generation.mirror import get_vertices_unit, get_edges_unit
from scripts_generation.translate import get_vertices_lattice, get_edges_lattice

# Directories
filename = '2BCC_3'
folder_json = 'structures/json'

folder_plot_octant = 'structures/plots_octant'
folder_plot_unit = 'structures/plots_unit'
folder_plot_lattice = 'structures/plots_lattice'

filename_json_octant = f"{folder_json}/{filename}_octant.json"
filename_json_unit = f"{folder_json}/{filename}_unit.json"
filename_json_lattice = f"{folder_json}/{filename}_lattice.json"

filename_plot_octant = f"{folder_plot_octant}/{filename}_octant.png"
filename_plot_unit = f"{folder_plot_unit}/{filename}_unit.png"
filename_plot_lattice = f"{folder_plot_unit}/{filename}_lattice.png"

if not os.path.exists(folder_json):
    os.makedirs(folder_json)
if not os.path.exists(folder_plot_octant):
    os.makedirs(folder_plot_octant)
if not os.path.exists(folder_plot_unit):
    os.makedirs(folder_plot_unit)
if not os.path.exists(folder_plot_lattice):
    os.makedirs(folder_plot_lattice)

# {2BCC}3
vertices_octant =  [[0, 0, 0],
                    [1, 1, 1]]
if check_custom_initial(vertices_octant)== True:
    print('Provided vertices are valid')
else:
    assert False, "Custom initial check failed"
edges_octant = all_connection(vertices_octant)

# Expand to unit
vertices_unit = get_vertices_unit(vertices_octant)
edges_unit = get_edges_unit(edges_octant)

# Lattice
vertices_lattice = get_vertices_lattice(vertices_unit)
edges_lattice = get_edges_lattice(edges_unit)

# Save structure
generate_json(format_vertices(vertices_octant), format_edges(edges_octant), filename_json_octant)
generate_json(format_vertices(vertices_unit), format_edges(edges_unit), filename_json_unit)
generate_json(format_vertices(vertices_lattice), format_edges(edges_lattice), filename_json_lattice)

# Visualize
visualize_octant(filename_json_octant, filename_plot_octant)
visualize_unit(filename_json_unit, filename_plot_unit)
visualize_lattice(filename_json_lattice, filename_plot_lattice)
