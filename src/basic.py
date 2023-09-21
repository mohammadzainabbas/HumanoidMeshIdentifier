import bpy

# Clear all data from the current scene to start fresh
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import the FBX file
imported_objects = bpy.ops.import_scene.fbx(filepath="fbx/character.fbx")

# List the names of all objects in the scene
object_names = [obj.name for obj in bpy.data.objects]

print(f"{object_names = }")
