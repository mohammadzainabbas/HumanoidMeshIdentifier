import bpy
import bmesh
from typing import List, Tuple, Union, Dict, Any

def check_humanoid_mesh(object: Any) -> bool:
    """
    Note: This script makes a series of checks on the mesh's topology and then combines those checks to make an educated guess about whether or not the mesh is humanoid. It's worth noting that these checks are heuristics and might not work for all humanoid models, especially non-standard or stylized ones.
    """

    bpy.ops.preferences.addon_enable(module="bmesh")
    # Get the active object (assuming it's the character mesh)
    mesh = object.data

    # Create a new BMesh instance to analyze mesh topology
    bm = bmesh.new()
    bm.from_mesh(mesh)

    # 1. Check for Symmetry
    # Count vertices on the left and right of the X-axis
    left_vertices = [v for v in bm.verts if v.co.x < 0]
    right_vertices = [v for v in bm.verts if v.co.x > 0]
    if len(left_vertices) != len(right_vertices): return False

    # 2. Check Connected Components
    # Using the island select mode in bmesh
    bm.faces.ensure_lookup_table()
    bm.faces.active = bm.faces[0]
    bpy.ops.mesh.select_linked()
    connected_components = len([f for f in bm.faces if f.select])
    bm.free()
    if connected_components != len(bm.faces): return False

    # 3. Check Proportions (simplified)
    bbox_dimensions = object.dimensions
    height_to_width_ratio = bbox_dimensions.z / bbox_dimensions.x
    # Humanoids generally have a height-to-width ratio greater than 2
    if height_to_width_ratio <= 2: return False

    # If everything goes well i.e: all checks for "is_humanoid_topology" are successful
    return True
