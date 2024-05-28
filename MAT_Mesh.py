import trimesh

# input_mesh = trimesh.load_mesh('../project/hand/01hand_MA_scp.obj')
unit_sphere = trimesh.load_mesh('./data/sphere_I.obj')
spheres = []


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
# 01human-2_MA-1-1.obj
# 01crab_4_MA-1-1.obj
vertices, edges, faces = read_vertex_data("./data/01crab_4/01crab_4_MA-1-1.obj")
vertices, edges, faces = read_vertex_data("./data/01human-2/01human-2_MA-1-1.obj")
for vertex in vertices:
    center = vertex[:3]
    radius = vertex[3]
    transformed_sphere = unit_sphere.copy()
    transformed_sphere.vertices *= radius
    transformed_sphere.vertices += center
    spheres.append(transformed_sphere)

convex_hull_mesh = trimesh.Trimesh()

for edge in edges:
    sphere1 = spheres[edge[0]]
    sphere2 = spheres[edge[1]]
    edge_mesh = trimesh.util.concatenate([sphere1, sphere2]).convex_hull
    convex_hull_mesh = trimesh.util.concatenate([convex_hull_mesh, edge_mesh])
for face in faces:
    sphere1 = spheres[face[0]]
    sphere2 = spheres[face[1]]
    sphere3 = spheres[face[2]]
    face_mesh = trimesh.util.concatenate([sphere1, sphere2, sphere3]).convex_hull
    convex_hull_mesh = trimesh.util.concatenate([convex_hull_mesh, face_mesh])

convex_hull_mesh.export('./01human-2_model-1-1.obj')
