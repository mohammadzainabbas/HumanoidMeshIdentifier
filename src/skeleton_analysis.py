import bpy
from typing import List, Tuple, Union, Dict, Any

def check_humanoid_skeleton(objects: Any) -> bool:
    """
    Note: This approach primarily checks for the presence of bones typically associated with humanoid figures. It's not foolproof, but it's a good starting point. Advanced methods might involve more detailed mesh analysis, motion capture data analysis, or even machine learning models trained on a variety of humanoid and non-humanoid figures.
    """
    # Define a list of common humanoid bone names or parts
    humanoid_bones = ['head', 'neck', 'spine', 'arm', 'hand', 'leg', 'foot', 'hip', 'thigh', 'calf']

    # Extract bone names from the scene
    all_armatures = [obj for obj in objects if (obj.type == 'ARMATURE') or (obj.type == 'MESH')]
    object_types = [obj.type for obj in objects]

    print(f"{all_armatures = }")
    print(f"{object_types = }")

    if not len(all_armatures):
        raise Exception("No armatures found in the scene")

    mesh_object = all_armatures[0]

    if mesh_object.type == 'MESH' and mesh_object.modifiers:
        for mod in mesh_object.modifiers:
            if mod.type == 'ARMATURE':
                armature = mod.object
    elif mesh_object.type == 'ARMATURE':
        armature = mesh_object
    else:
        raise Exception("No armature found in the scene")

    bone_names = [bone.name.lower() for bone in armature.pose.bones]

    print(f"{armature = }")
    print(f"{bone_names = }")

    # Check for humanoid structure
    is_humanoid = all(any(bone in name for bone in humanoid_bones) for name in bone_names)

    print(f"{is_humanoid = }")

    # If True, mesh has a recognizable humanoid skeleton.
    # If False, mesh either doesn't have a recognizable humanoid skeleton or lacks one entirely.
    return is_humanoid # we optimise this by returning early if we find a match 