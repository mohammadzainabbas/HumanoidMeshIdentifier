import bpy
from icecream import ic

from .skeleton_analysis import check_humanoid_skeleton
from .mesh_analysis import check_humanoid_mesh
from .animation_analysis import check_humanoid_animation


def main():
    # Clear all data from the current scene to start fresh
    bpy.ops.wm.read_factory_settings(use_empty=True)

    # Import the FBX file
    imported_objects = bpy.ops.import_scene.fbx(filepath="fbx/character.fbx")

    ic(imported_objects)

    # List the names of all objects in the scene
    object_names = [obj.name for obj in bpy.data.objects]

    ic(object_names)

    if check_humanoid_skeleton(bpy.data.objects):
        ic("The character has a humanoid skeleton")
    else:
        ic("The character does not have a humanoid skeleton")

    if check_humanoid_mesh(bpy.context.active_object):
        ic("The character has a humanoid mesh")
    else:
        ic("The character does not have a humanoid mesh")
    
    if check_humanoid_animation(bpy.context.active_object): # Get the active object (assuming it's the armature)
        ic("The character has a humanoid animation")
    else:
        ic("The character does not have a humanoid animation")

if __name__ == "__main__":
    ic.configureOutput(prefix="", includeContext=True)
    main()
