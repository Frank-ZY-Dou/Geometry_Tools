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

def load_ma_file(filepath):
    file = open(filepath, 'r')
    # read first line number of vertices/edges/faces
    first_line = file.readline().rstrip()
    vcount, ecount, fcount = [int(x) for x in first_line.split()]
    # No Medial Vertices
    assert vcount != 0, "No Medial Vertices!"
    # line number
    lineno = 1

    # Medial Mesh Info
    verts, radii, faces, edges = [], [], [], []

    # read vertices
    i = 0
    while i < vcount:
        line = file.readline()
        # skip empty lines or comment lines
        if line.isspace() or line[0] == '#':
            lineno = lineno + 1
            continue
        v = line.split()
        # Handle exception
        assert v[0] == 'v', "vertex line:" + str(
            lineno) + " should start with \'v\'!"
        x = float(v[1])
        y = float(v[2])
        z = float(v[3])
        radii.append(float(v[4]))
        verts.append((x, y, z))
        lineno += 1
        i += 1

    i = 0
    # read edges
    while i < ecount:
        line = file.readline()
        if line.isspace() or line[0] == '#':
            lineno = lineno + 1
            continue
        ef = line.split()
        # Handle exception
        assert ef[0] == 'e', "line:" + str(
            lineno) + " should start with \'e\'!"
        ids = list(map(int, ef[1:3]))
        edges.append(tuple(ids))
        lineno += 1
        i += 1

    i = 0
    # read faces
    while i < fcount:
        line = file.readline()
        if line.isspace() or line[0] == '#':
            lineno = lineno + 1
            continue
        ef = line.split()
        # Handle exception
        assert ef[0] == 'f', "line:" + str(
            lineno) + " should start with \'f\'!"
        f = tuple(list(map(int, ef[1:4])))
        faces.append(f)
        edges.append(f[:2])
        edges.append(f[1:3])
        edges.append((f[0], f[2]))

        lineno += 1
        i += 1

    unique_edges = list(unique_everseen(edges, key=frozenset))
    return vcount, fcount, ecount, verts, radii, faces, unique_edges



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
    filelist = ["01crab_QMAT+.ma",
                "01crab_QMAT.ma",
                "01dog_QMAT+.ma",
                "01dog_QMAT.ma",
                "01fertility_QMAT+.ma",
                "01fertility_QMAT.ma",
                "01hand_QMAT+.ma",
                "01hand_QMAT.ma",
                "01vase_QMAT+.ma",
                "01vase_QMAT.ma",
                "01dog_MATFP.ma",
                "01crab_MATFP.ma",
                "01hand_MATFP.ma",
                "01fertility_MATFP.ma",
                "01vase_MATFP.ma"
                ]
    for filename in filelist:
        filepath = "./data/%s"%filename
        vcount, ecount, fcount, verts, radii, faces, edges = load_ma_file(
            filepath)
        mat_name = filename.split("/")[-1].replace(".ma","")
        generate_medial_mesh("./Medial_Mesh/"+mat_name, verts, radii, faces, edges)