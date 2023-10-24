def extract_vertices_edges(input_file, output_vertices_edges_file):
    vertices = []
    edges = []

    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertex = line.strip().split()[1:]
                vertices.append(vertex)
            elif line.startswith('l '):
                edge = line.strip().split()[1:]
                edges.append(edge)

    with open(output_vertices_edges_file, 'w') as file:
        for vertex in vertices:
            file.write('v ' + ' '.join(vertex) + '\n')

        for edge in edges:
            file.write('l ' + ' '.join(edge) + '\n')

def extract_vertices_faces(input_file, output_vertices_faces_file):
    vertices = []
    faces = []

    with open(input_file, 'r') as file:
        for line in file:
            if line.startswith('v '):
                vertex = line.strip().split()[1:]
                vertices.append(vertex)
            elif line.startswith('f '):
                face = line.strip().split()[1:]
                faces.append(face)

    with open(output_vertices_faces_file, 'w') as file:
        for vertex in vertices:
            file.write('v ' + ' '.join(vertex) + '\n')

        for face in faces:
            file.write('f ' + ' '.join(face) + '\n')

# 使用示例
input_file = './data/01armadillo_MA (1).obj'
output_vertices_edges_file ='./data/01armadillo_MA_l.obj'
output_vertices_faces_file = './data/01armadillo_MA_f.obj'

extract_vertices_edges(input_file, output_vertices_edges_file)
extract_vertices_faces(input_file, output_vertices_faces_file)