import numpy as np
from scipy.spatial import cKDTree
import trimesh

def chamfer_distance(input_mesh_file, reference_mesh_file):
    input_mesh = trimesh.load_mesh(input_mesh_file)
    reference_mesh = trimesh.load_mesh(reference_mesh_file)
    input_vertices = input_mesh.vertices[:, :3]
    reference_vertices = reference_mesh.vertices[:, :3]
    input_kdtree = cKDTree(input_vertices)
    reference_kdtree = cKDTree(reference_vertices)
    input_to_reference_distances, _ = reference_kdtree.query(input_vertices)
    chamfer_input_to_reference = np.mean(input_to_reference_distances)
    reference_to_input_distances, _ = input_kdtree.query(reference_vertices)
    chamfer_reference_to_input = np.mean(reference_to_input_distances)
    chamfer_distance = chamfer_input_to_reference + chamfer_reference_to_input
    return chamfer_distance


def unidirectional_hausdorff_distance(input_mesh_file, reference_mesh_file):
    input_mesh = trimesh.load_mesh(input_mesh_file)
    reference_mesh = trimesh.load_mesh(reference_mesh_file)
    distance_input_to_reference = input_mesh.hausdorff_distance(reference_mesh)
    return distance_input_to_reference


def unidirectional_hausdorff_distance_reverse(input_mesh_file, reference_mesh_file):
    input_mesh = trimesh.load_mesh(input_mesh_file)
    reference_mesh = trimesh.load_mesh(reference_mesh_file)
    distance_reference_to_input = reference_mesh.hausdorff_distance(input_mesh)
    return distance_reference_to_input


def bidirectional_hausdorff_distance(input_mesh_file, reference_mesh_file):
    distance_input_to_reference = unidirectional_hausdorff_distance(input_mesh_file, reference_mesh_file)
    distance_reference_to_input = unidirectional_hausdorff_distance_reverse(reference_mesh_file, input_mesh_file)
    bidirectional_distance = max(distance_input_to_reference, distance_reference_to_input)
    return bidirectional_distance

if __name__ == '__main__':
    input_mesh_file = "input_mesh.obj"
    reference_mesh_file = "reference_mesh.obj"

    # Compute chamfer distance
    chamfer_dist = chamfer_distance(input_mesh_file, reference_mesh_file)
    print("Chamfer Distance:", chamfer_dist)

    # Compute unidirectional Hausdorff distance: input mesh to reference mesh
    unidirectional_dist_input_to_ref = unidirectional_hausdorff_distance(input_mesh_file, reference_mesh_file)
    print("Unidirectional Hausdorff Distance (Input to Reference):", unidirectional_dist_input_to_ref)

    # Compute unidirectional Hausdorff distance: reference mesh to input mesh
    unidirectional_dist_ref_to_input = unidirectional_hausdorff_distance_reverse(input_mesh_file, reference_mesh_file)
    print("Unidirectional Hausdorff Distance (Reference to Input):", unidirectional_dist_ref_to_input)

    # Compute bidirectional Hausdorff distance
    bidirectional_dist = max(unidirectional_dist_input_to_ref, unidirectional_dist_ref_to_input)
    print("Bidirectional Hausdorff Distance:", bidirectional_dist)