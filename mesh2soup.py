import trimesh
import numpy as np

def load_mesh(file_path):
    # Load the mesh file
    mesh = trimesh.load(file_path)
    return mesh

def generate_triangular_soup(mesh, noise_scale=0.01):
    # Extract the triangles
    triangles = mesh.triangles

    # Add random perturbation to each vertex
    noise = np.random.normal(scale=noise_scale, size=triangles.shape)
    perturbed_triangles = triangles + noise

    return perturbed_triangles

def save_triangular_soup(triangles, output_file):
    with open(output_file, 'w') as f:
        vertex_count = 1
        for triangle in triangles:
            for vertex in triangle:
                f.write(f"v {vertex[0]} {vertex[1]} {vertex[2]}\n")
            f.write(f"f {vertex_count} {vertex_count + 1} {vertex_count + 2}\n")
            vertex_count += 3

if __name__ == "__main__":
    input_file = "sphere_I.obj"
    output_file = "sphere_I_perturbed_triangular_soup.obj"
    noise_scale = 0.01  # Adjust the scale of noise as needed

    mesh = load_mesh(input_file)
    perturbed_triangles = generate_triangular_soup(mesh, noise_scale)
    save_triangular_soup(perturbed_triangles, output_file)
