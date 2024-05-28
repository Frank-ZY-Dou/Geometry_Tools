import trimesh
from itertools import filterfalse

################
# Code credit to https://github.com/songshibo/blender-mat-addon/tree/main
# -> https://songshibo.github.io/
# -> https://ningnawang.github.io/
################
def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element


def read_vertex_data(filename):
    vertices = []
    edges = []
    faces = []
    radius = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith('v '):
                vertex_data = line[2:].split()
                if len(vertex_data) == 4:
                    x, y, z, r = map(float, vertex_data)
                    vertices.append((x, y, z))
                    radius.append(r)
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

    return radius, vertices, edges, faces



def generate_medial_mesh(name, verts, radii, faces, edges, *args):
    if len(args) == 0:  # stndard MAT
        # Simply assemble Medial Mesh
        with open(name + '.obj', 'w') as file:
            for v in verts:
                file.write(f'v {v[0]} {v[1]} {v[2]}\n')
            for e in edges:
                file.write(f'l {e[0] + 1} {e[1] + 1}\n')  # OBJ索引从1开始
            for f in faces:
                file.write(f'f {f[0] + 1} {f[1] + 1} {f[2] + 1}\n')  # OBJ索引从1开始

        with open(name + '_l.obj', 'w') as file:
            for v in verts:
                file.write(f'v {v[0]} {v[1]} {v[2]}\n')
            for e in edges:
                file.write(f'l {e[0] + 1} {e[1] + 1}\n')  # OBJ索引从1开始

        with open(name + '_f.obj', 'w') as file:
            for v in verts:
                file.write(f'v {v[0]} {v[1]} {v[2]}\n')
            for f in faces:
                file.write(f'f {f[0] + 1} {f[1] + 1} {f[2] + 1}\n')  # OBJ索引从1开始




if __name__ == '__main__':
#     filelist = ["01snake_op_36_NeuralSkeleton.obj",
# "01ant_op_54_NeuralSkeleton.obj",
# "01bottle_op_13_NeuralSkeleton.obj",
# "01chair-2_op_134_NeuralSkeleton.obj",
# "01dog_op_42_NeuralSkeleton.obj",
# "01dolphin_op_36_NeuralSkeleton.obj",
# "01fertility_op_76_NeuralSkeleton.obj",
# "01guitar_op_65_NeuralSkeleton.obj",
# "01hand_op_39_NeuralSkeleton.obj",
# "01kitten_op_41_NeuralSkeleton.obj"
#                 ]

    filelist = ["01crab_4/01crab_4_MA-0-0.obj",
                "01crab_4/01crab_4_MA-1-0.obj",
                "01crab_4/01crab_4_MA-1-1.obj",
                "01human-2/01human-2_MA-0-0.obj",
                "01human-2/01human-2_MA-1-0.obj",
                "01human-2/01human-2_MA-1-1.obj",
                ]
    for filename in filelist:
        filepath = "./data/%s"%filename
        radii,verts, edges, faces = read_vertex_data(
            filepath)
        mat_name = filename.split("/")[-1].replace(".obj","")
        generate_medial_mesh("./Medial_Mesh/_"+mat_name, verts, radii, faces, edges)