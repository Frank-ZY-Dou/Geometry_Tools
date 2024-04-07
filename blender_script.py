import bpy
import time

# from the github:
# https://github.com/songshibo/blender-mat-addon

import bpy
import time
import os


def get_ma_files(folder_path):
    ma_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".ma"):
                ma_files.append(os.path.join(root, file))
    return ma_files

folder_path = r"/Users/Frank/Desktop/MATFP_rendering_only"
ma_files = get_ma_files(folder_path)

for idid, file_path in enumerate(ma_files):
    print("::::", file_path)

    print(bpy.app.version_string)
    bpy.ops.import_mesh.mat(filepath=file_path, mat_type='std')
    objects = []

    for obj in bpy.context.scene.objects:
        obj.select_set(obj.type == "MESH")
        objects.append(obj)

    c = {}
    c["object"] = c["active_object"] = bpy.context.object
    c["selected_objects"] = c["selected_editable_objects"] = objects
    bpy.ops.object.join()

    start_time = time.time()
    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers['Remesh'].mode='VOXEL'
    bpy.context.object.modifiers['Remesh'].voxel_size=0.09
    bpy.ops.object.modifier_apply(modifier='Remesh')
    print("--- VOXEL REMESH:  %.2f seconds ---" % (time.time() - start_time))

    #bpy.ops.export_mesh.ply(filepath="./remeshed.ply", use_selection=True)
    bpy.ops.export_mesh.stl(filepath=file_path.replace(".ma","_recon.stl"), use_selection=True)
    bpy.ops.object.delete()