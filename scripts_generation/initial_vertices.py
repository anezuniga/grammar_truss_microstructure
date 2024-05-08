import random

def generate_essential_vertices(precision):
    vertices = [[0, round(random.random(), precision), round(random.random(), precision)],
                [1, round(random.random(), precision), round(random.random(), precision)],
                [round(random.random(), precision), 0, round(random.random(), precision)],
                [round(random.random(), precision), 1, round(random.random(), precision)],
                [round(random.random(), precision), round(random.random(), precision), 0],
                [round(random.random(), precision), round(random.random(), precision), 1]]
    return vertices

def generate_extra_face_vertices(num_vertices, precision):
    extra_vertices = []
    for _ in range(num_vertices):
        face = random.randint(0, 5)
        if face == 0:
            vertex = [0, round(random.random(), precision), round(random.random(), precision)]
        elif face == 1:
            vertex = [1, round(random.random(), precision), round(random.random(), precision)]
        elif face == 2:
            vertex = [round(random.random(), precision), 0, round(random.random(), precision)]
        elif face == 3:
            vertex = [round(random.random(), precision), 1, round(random.random(), precision)]
        elif face == 4:
            vertex = [round(random.random(), precision), round(random.random(), precision), 0]
        else:
            vertex = [round(random.random(), precision), round(random.random(), precision), 1]
        extra_vertices.append(vertex)
    return extra_vertices

def generate_extra_body_vertices(num_vertices, precision):
    extra_vertices = []
    for _ in range(num_vertices):
        vertex = [round(random.uniform(1/10**precision, 1- 1/10**precision), precision), round(random.uniform(1/10**precision, 1- 1/10**precision), precision), round(random.uniform(0.1, 0.9), precision)]
        extra_vertices.append(vertex)
    return extra_vertices

def generate_initial_vertices(v_extra_face, v_extra_body, precision):
    vertices_octant_essential = generate_essential_vertices(precision)
    vertices_octant_extra_face = generate_extra_face_vertices(v_extra_face, precision)
    vertices_octant_extra_body = generate_extra_body_vertices(v_extra_body, precision)
    vertices_octant_all = []
    vertices_octant_all.extend(vertices_octant_essential)
    vertices_octant_all.extend(vertices_octant_extra_face)
    vertices_octant_all.extend(vertices_octant_extra_body)
    vertices_octant = filter_repeated_vertices(vertices_octant_all)
    return vertices_octant

def filter_repeated_vertices(vertices):
    vertices_filtered = []
    for vertex in vertices:
        if vertex not in vertices_filtered:
            vertices_filtered.append(vertex)
    return vertices_filtered

def check_custom_initial(vertices):
    x_coords = set()
    y_coords = set()
    z_coords = set()

    for vertex in vertices:
        x_coords.add(vertex[0])
        y_coords.add(vertex[1])
        z_coords.add(vertex[2])

    meet_condition = (0 in x_coords and 1 in x_coords and
            0 in y_coords and 1 in y_coords and
            0 in z_coords and 1 in z_coords)

    return meet_condition

def format_vertices(vertices):
    formatted_vertices = {}
    for i, vertex in enumerate(vertices):
        key = "v" + str(i)
        formatted_vertices[key] = vertex
    return formatted_vertices
