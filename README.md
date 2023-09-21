# Humanoid Mesh Identifier

This project aims to assess if an animated mesh is humanoid by examining its structure, mesh topology, and animation features using Blender's Python API (`bpy`).

## Ideas

Humanoids can vary greatly, and a more complex solution could involve machine learning or deep analysis of mesh vertices and their movements. This project aims to provide a simple solution that can be used as a starting point for more complex solutions.

Check the ideas document for more details: [docs/IDEA.md](https://github.com/mohammadzainabbas/HumanoidMeshIdentifier/blob/main/docs/IDEA.md).

## Requirements

- [x] Blender with Python API support
- [x] FBX file of the animated mesh

## Steps

### 1. Import the FBX File

```python
import bpy

# Clear all data from the current scene to start fresh
bpy.ops.wm.read_factory_settings(use_empty=True)

# Import the FBX file
bpy.ops.import_scene.fbx(filepath="path_to_your_character.fbx")
```

### 1. Check the Skeleton Structure

Refer to the provided Python script for Blender to check the skeleton structure.

### 1. Check the Mesh Topology

Refer to the provided Python script for Blender to perform various checks on mesh topology.

### 1. Check the Animations

Refer to the provided Python script for Blender to analyze the animation of the mesh.

### 1. Test the Script

```bash
blender -b -P src/main.py
```

> Assuming you have `blender` installed and added to your `PATH`; and you have clone this repo as well.

## Limitations

This is a basic assessment and may produce false positives or negatives. For a more thorough analysis, consider using advanced methods such as machine learning models trained on a variety of humanoid and non-humanoid figures.

