## Ideas on how to check for animated humanoid mesh in Blender

To determine if an animated mesh is humanoid, we can examine its structure and look for features that are typically associated with humanoids. A general approach might include:

1. **Skeleton Structure**: Check if the mesh has a skeleton, and if so, whether the skeleton has joints or bones that match typical humanoid naming conventions or structures (e.g., head, arms, legs).
1. **Mesh Topology**: Look for humanoid features in the mesh itself, such as a head, torso, two arms, and two legs.
1. **Animation**: If the mesh is animated, see if the animations are typical of humanoid movements.
To accomplish this, we'll utilize the bpy module, which is Blender's Python API. This will allow us to import the FBX file into Blender, inspect its contents, and determine if it has humanoid characteristics.

Here's a high-level overview of the steps we'll take:

- [x] Import the FBX file into Blender.
- [x] Check the skeleton structure for humanoid bones.
- [x] If the skeleton is humanoid, confirm by checking the mesh topology.
- [x] Optionally, check the animations if present.

### Check Skeleton Structure

A humanoid typically has a head, torso, two arms, two legs, etc. If the skeleton or armature inside the mesh follows this structure, you might infer that the mesh is humanoid.

Check if the mesh has a skeleton, and if so, whether the skeleton has joints or bones that match typical humanoid naming conventions or structures (e.g., head, arms, legs).

This approach primarily checks for the presence of bones typically associated with humanoid figures. It's not foolproof, but it's a good starting point. Advanced methods might involve more detailed mesh analysis, motion capture data analysis, or even machine learning models trained on a variety of humanoid and non-humanoid figures.

### Check Mesh Topology

If the skeleton appears humanoid, you can further verify by checking the mesh topology for humanoid features. This would be a bit more involved and might require analyzing the mesh's vertices and faces.

Checking mesh topology to determine if a mesh is humanoid can be a bit complex due to the sheer variety of humanoid models available. However, we can make some general assumptions and checks to help us make an educated guess.

Here are a few properties we can check for:

- [x] **Symmetry**: Humanoids are generally symmetrical along the vertical axis.
- [x] **Connected Components**: A humanoid mesh should ideally be one connected component.
- [x] **Proportions**: We can compare the bounding box of the mesh to expected human proportions.

### Check Animations

Analyzing animations to determine if a mesh is humanoid can be a bit subjective. However, we can try to look for some common characteristics of humanoid animation, such as `bipedal walking`, `standing`, or `hand movements`. We can do this by examining the keyframe data for each bone to see if it performs recognizable humanoid actions.

If the mesh has animations, you can check if the animations match typical humanoid movements. This would be even more subjective and might require visual inspection.

#

> Humanoids can vary greatly, and a more complex solution could involve machine learning or deep analysis of mesh vertices and their movements. However, the approach outlined here should be taken as a starting-point, and thus is not intended to be exhaustive/definitive/bulletproof.

