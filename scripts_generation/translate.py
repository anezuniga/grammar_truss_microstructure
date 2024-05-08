
def translate_vertices(vertices, vector):
        translated = []
        for v in vertices:
            new_vertex = v.copy()
            for i in range(3):
                new_vertex[i] += vector[i]
            translated.append(new_vertex)
        return translated

def get_vertices_lattice(vertices): # vertices are stacked in the order that gives them the right priority for visualization (back first, front last)
    translated_vertices = translate_vertices(vertices, [0,2,0]) # bottom back
    vertices_lattice = translated_vertices
    vertices_lattice.extend(vertices[:])                        # bottom left
    translated_vertices = translate_vertices(vertices, [2,2,0]) # bottom right
    vertices_lattice.extend(translated_vertices)
    translated_vertices = translate_vertices(vertices, [2,0,0]) # bottom front
    vertices_lattice.extend(translated_vertices)
    translated_vertices = translate_vertices(vertices, [0,2,2]) # top back
    vertices_lattice.extend(translated_vertices)
    translated_vertices = translate_vertices(vertices, [0,0,2]) # top left
    vertices_lattice.extend(translated_vertices)
    translated_vertices = translate_vertices(vertices, [2,2,2]) # top right
    vertices_lattice.extend(translated_vertices)
    translated_vertices = translate_vertices(vertices, [2,0,2]) # top front
    vertices_lattice.extend(translated_vertices)
    return vertices_lattice

def get_edges_lattice(edges):
    total = 8 # Total number of units in the lattice
    edges_lattice = [[0] * (total * len(edges)) for _ in range(total * len(edges))]
    for i in range(total):
        for j in range(len(edges)):
            for k in range(len(edges)):
                edges_lattice[i*len(edges)+j][i*len(edges)+k] = edges[j][k]
    return edges_lattice