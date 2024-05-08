import random
import sys
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.abspath(os.path.join(script_dir, '..'))
sys.path.append(project_root)

from scripts_visualization.visualize_octant import visualize_octant
from scripts_visualization.visualize_unit import visualize_unit
from scripts_visualization.visualize_lattice import visualize_lattice

# Seed
seed = 0

# Directories
filename = f"truss_{seed}"
folder_json = 'structures/json'

folder_plot_octant = 'structures/plots_octant'
folder_plot_unit = 'structures/plots_unit'
folder_plot_lattice = 'structures/plots_lattice'

filename_json_octant = f"{folder_json}/{filename}_octant.json"
filename_json_unit = f"{folder_json}/{filename}_unit.json"
filename_json_lattice = f"{folder_json}/{filename}_lattice.json"

filename_plot_octant = f"{folder_plot_octant}/{filename}_octant.png"
filename_plot_unit = f"{folder_plot_unit}/{filename}_unit.png"
filename_plot_lattice = f"{folder_plot_lattice}/{filename}_lattice.png"

if not os.path.exists(folder_plot_octant):
    os.makedirs(folder_plot_octant)
if not os.path.exists(folder_plot_unit):
    os.makedirs(folder_plot_unit)
if not os.path.exists(folder_plot_lattice):
    os.makedirs(folder_plot_lattice)

# Visualize
visualize_octant(filename_json_octant, filename_plot_octant)
visualize_unit(filename_json_unit, filename_plot_unit)
visualize_lattice(filename_json_lattice, filename_plot_lattice)

