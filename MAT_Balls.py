import trimesh

unit_sphere = trimesh.load_mesh('./data/sphere_I.obj')
spheres = []


def read_vertex_data(filename):
    vertices = []
    edges = []
    faces = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('v '):
                vertex_data = line[2:].split()
                if len(vertex_data) == 4:
                    x, y, z, r = map(float, vertex_data)
                    vertices.append((x, y, z, r))
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


vertices, edges, faces = read_vertex_data("./01guitar_selected_inner_points_new.obj")
print(len(vertices))
for vertex in vertices:
    center = vertex[:3]
    radius = vertex[3]
    transformed_sphere = unit_sphere.copy()
    transformed_sphere.vertices *= radius
    transformed_sphere.vertices += center
    spheres.append(transformed_sphere)

convex_hull_mesh = trimesh.Trimesh()

for sp in spheres:
    convex_hull_mesh = trimesh.util.concatenate([convex_hull_mesh, sp])

convex_hull_mesh.export('./01hand_output_sphere.obj')
