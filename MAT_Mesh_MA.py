import trimesh

def read_vertex_data_ma(filename):
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
            if line.startswith("e "):
                edge_data = line[2:].split()
                if len(edge_data) == 2:
                    e1, e2 = map(int, edge_data)
                    edges.append((e1, e2 ))
            if line.startswith('f '):
                face_data = line[2:].split()
                if len(face_data) == 3:
                    f1, f2, f3 = map(int, face_data)
                    faces.append((f1, f2, f3))

    return vertices, edges, faces



unit_sphere = trimesh.load_mesh('./data/sphere_I.obj')
vertices, edges, faces = read_vertex_data_ma("./data/chair_0002.ma")
spheres = []


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

convex_hull_mesh.export('./data/chair111_ma_mesh.obj')
