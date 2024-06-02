import numpy as np
import trimesh

def read_obj(file_path):
    mesh = trimesh.load(file_path)
    return mesh

def compute_distances(vertices, surface_mesh):
    distances = []
    for v in vertices:
        distance = np.min(np.linalg.norm(surface_mesh.vertices - v, axis=1))
        distances.append(distance)
    return distances


def read_vertex_data(filename):
    vertices = []
    edges = []
    faces = []
    with open(filename, 'r') as file:
        for line in file:
            print(line)
            line = line.strip()
            if line.startswith('v '):
                vertex_data = line[2:].split()
                if len(vertex_data) == 3:
                    x, y, z = map(float, vertex_data)
                    vertices.append((x, y, z))
            if line.startswith("l "):
                edge_data = line[2:].split()
                if len(edge_data) == 2:
                    e1, e2 = map(int, edge_data)
                    edges.append((e1 - 1, e2 - 1))
            if line.startswith('f '):
                face_data = line[2:].split()
                if len(face_data) == 3:
                    f1, f2, f3 = map(int, face_data)
                    faces.append((f1 - 1, f2 - 1, f3 - 1))
    return vertices, edges, faces

def write_obj_with_distances( vertices, edges, faces, distances, output_file):
    with open(output_file, 'w') as file:
        for i, vertex in enumerate(vertices):
            file.write(f"v {vertex[0]} {vertex[1]} {vertex[2]} {distances[i]}\n")
        for i, edge in enumerate(edges):
            file.write(f"l {edge[0]+1} {edge[1]+1}\n")
        for i, face in enumerate(faces):
            file.write(f"f {face[0]+1} {face[1]+1} {face[2]+1}\n")


def main():
    skel_path = './data/01Hand_MA.obj'
    surface_path = './data/01Hand.obj'
    output_path = './data/01Hand_MA_with_r.obj'

    vertices, edges, faces = read_vertex_data(skel_path)
    print(vertices)
    surface_mesh = read_obj(surface_path)

    distances = compute_distances( vertices,  surface_mesh)
    write_obj_with_distances( vertices, edges, faces, distances, output_path)

if __name__ == "__main__":
    main()
