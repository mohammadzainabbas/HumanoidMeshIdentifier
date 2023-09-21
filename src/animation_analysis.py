import bpy
from typing import List, Tuple, Union, Dict, Any

def check_humanoid_animation(object: Any) -> bool:
    """
    Note: This script checks each animation action for keyframes that move bones typically associated with humanoid figures. If it finds such keyframes, it assumes that the animation is humanoid.
    """
    # Check if the object has animation data
    if object.animation_data:

        # List of common humanoid bone names or parts (you may want to customize this)
        humanoid_bones = ['head', 'neck', 'spine', 'arm', 'hand', 'leg', 'foot', 'hip', 'thigh', 'calf']
        
        # Iterate through all the actions (animations)
        for action in bpy.data.actions:
            
            # Assign the action to the object's animation data
            object.animation_data.action = action

            # Analyze keyframes for humanoid features
            # is_humanoid_animation = False
            for fcurve in action.fcurves:

                # Try to find the bone name from the data path
                bone_name = fcurve.data_path.split('"')[1] if '"' in fcurve.data_path else ''
                bone_name = bone_name.lower()

                # Check if the bone name resembles any humanoid bone names
                if any(human_bone in bone_name for human_bone in humanoid_bones):
                    return True
                    # is_humanoid_animation = True
                    # break

            # if is_humanoid_animation:
            #     print(f"The action '{action.name}' seems to be a humanoid animation.")
            # else:
            #     print(f"The action '{action.name}' does not seem to be a humanoid animation.")

    else:
        print("The object does not have animation data.")
        return False