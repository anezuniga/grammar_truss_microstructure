from scripts_generation.initial_vertices import generate_essential_vertices, format_vertices, filter_repeated_vertices


def mirror_vertices(vertices, axis):
        mirrored = []
        for v in vertices:
            new_vertex = v.copy()
            new_vertex[axis] *= -1
            mirrored.append(new_vertex)
        return mirrored

def get_vertices_unit(vertices):
    vertices_unit = vertices[:]
    mirrored_vertices = mirror_vertices(vertices_unit, 0)
    vertices_unit.extend(mirrored_vertices)
    mirrored_vertices = mirror_vertices(vertices_unit, 1)
    vertices_unit.extend(mirrored_vertices)
    mirrored_vertices = mirror_vertices(vertices_unit, 2)
    vertices_unit.extend(mirrored_vertices)
    return vertices_unit

def get_edges_unit(edges):
    edges_unit = [[0] * (8 * len(edges)) for _ in range(8 * len(edges))]
    for i in range(8):
        for j in range(len(edges)):
            for k in range(len(edges)):
                edges_unit[i*len(edges)+j][i*len(edges)+k] = edges[j][k]
    return edges_unit
