from collections import deque

def find_largest_connected_vertices(connection_matrix):
    n = len(connection_matrix)
    visited = [False] * n
    largest_component_size = 0
    
    def bfs(start):
        queue = deque([start])
        size = 0
        while queue:
            node = queue.popleft()
            for neighbor in range(n):
                if connection_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
            size += 1
        return size
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            component_size = bfs(i)
            largest_component_size = max(largest_component_size, component_size)
            
    return largest_component_size

def get_connection_indexes(connection_matrix, vertex_index):
    connection_indexes = []
    for i, value in enumerate(connection_matrix[vertex_index]):
        if value == 1:
            connection_indexes.append(i)
    return connection_indexes

def fulfill_vertex(vertices, vertex_index, connection_matrix):
    connected_indexes = get_connection_indexes(connection_matrix, vertex_index)
    connected_vertices = [vertices[i] for i in connected_indexes]
    
    vertex = vertices[vertex_index]
    on_face = any(coord == 0 or coord == 1 for coord in vertex)

    if on_face:
        # Check if it has at least 2 connected vertices in the same face
        same_face_count = sum(any(coord == 0 or coord == 1 for coord in connected_vertex) for connected_vertex in connected_vertices)
        if same_face_count >= 2:
            return True
        # Check if it has 1 connected vertex somewhere else that is not on the same face
        other_face_count = sum(1 for connected_vertex in connected_vertices if not any(coord == 0 or coord == 1 for coord in connected_vertex))
        if other_face_count >= 1:
            return True
    else:
        # Check if it has 2 any connections
        if len(connected_vertices) >= 2:
            return True
    return False
