def create_scad_file(vertices, connection_matrix, thick_end, thick_mid, filename):
    script_content = '''
// Function to draw a line with varying thickness
module line(start, end, thick_end, thick_mid) {
    // Calculate mid point
    mid = (start + end) / 2;
    
    // Create two gradient cylinders between start, mid, and end
    hull() {
        $fn = 20;
        translate(start) sphere(thick_end);
        translate(mid) sphere(thick_mid);
    }
    hull() {
        $fn = 20;
        translate(mid) sphere(thick_mid);
        translate(end) sphere(thick_end);
    }
}

// Draw lines between connected vertices with varying thickness
module drawConnections(vertices, connection_matrix, thick_end, thick_mid) {
    for (i = [0 : len(vertices) - 1]) {
        for (j = [0 : len(vertices) - 1]) {
            if (connection_matrix[i][j] == 1) {
                line(vertices[i], vertices[j], thick_end, thick_mid);
            }
        }
    }
}
'''
    vertices_str = str(vertices).replace('],', '],\n    ').replace('[[', '[\n    [').replace(']]', ']\n]')
    connection_matrix_str = str(connection_matrix).replace('],', '],\n    ').replace('[[', '[\n    [').replace(']]', ']\n]')
    
    script_content += f'''
// Define the vertices
vertices = {vertices_str};

// Define the connection matrix
connection_matrix = {connection_matrix_str};

// Parameters for end and mid thicknesses
thick_end = {thick_end}; // Thickness at the vertices
thick_mid = {thick_mid}; // Thickness at the mid-point

// MAIN
drawConnections(vertices, connection_matrix, thick_end, thick_mid);
'''
    with open(filename, 'w') as file:
        file.write(script_content)