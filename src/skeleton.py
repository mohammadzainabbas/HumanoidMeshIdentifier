import bpy

# Clear all data from the current scene to start fresh
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import the FBX file
imported_objects = bpy.ops.import_scene.fbx(filepath="fbx/character.fbx")

# Define a list of common humanoid bone names or parts
humanoid_bones = ['head', 'neck', 'spine', 'arm', 'hand', 'leg', 'foot', 'hip', 'thigh', 'calf']

objects = bpy.data.objects

print(f"{objects = }")

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