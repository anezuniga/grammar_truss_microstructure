def all_connection(vertices):
    num_vertices = len(vertices)
    edges = [[1] * num_vertices for _ in range(num_vertices)]
    return edges

def format_edges(edges_matrix):
    formatted_edges = {}
    for i in range(len(edges_matrix)):
        for j in range(i+1, len(edges_matrix[i])):
            if edges_matrix[i][j] == 1:
                key = "e" + str(len(formatted_edges))
                vertex1 = "v" + str(i)
                vertex2 = "v" + str(j)
                formatted_edges[key] = [vertex1, vertex2]
    return formatted_edges

def format_edges_step(edges_matrix):
    formatted_edges = {}
    for i in range(len(edges_matrix)):
        for j in range(i+1, len(edges_matrix[i])):
            if edges_matrix[i][j] == 1:
                key = "e" + str(len(formatted_edges))
                vertex1 = "v" + str(i)
                vertex2 = "v" + str(j)
                formatted_edges[key] = [vertex1, vertex2]
            elif edges_matrix[i][j] == -1:
                key = "nt" + str(len(formatted_edges))
                vertex1 = "v" + str(i)
                vertex2 = "v" + str(j)
                formatted_edges[key] = [vertex1, vertex2]
    return formatted_edges

def initial_connection(vertices):
    num_vertices = len(vertices)
    edges = [[-1] * num_vertices for _ in range(num_vertices)]
    for i in range(num_vertices):
        edges[i][i] = 1  # Set diagonal elements to 1
    return edges

def add_connection(connection_matrix, v1, v2):
    connection_matrix[v1][v2] = 1
    connection_matrix[v2][v1] = 1
    return connection_matrix

def remove_connection(connection_matrix, v1, v2):
    connection_matrix[v1][v2] = 0
    connection_matrix[v2][v1] = 0
    return connection_matrix

def get_intermediate_indexes(matrix):
    indexes = []
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):  # Only iterate over upper triangular part (excluding diagonal)
            if matrix[i][j] == -1:
                indexes.append((i, j))
    return indexes