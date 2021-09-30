# Adds bpy module
import bpy

# Adds math module
from math import *

# Variables with cursor's coordinates
my_cursor_location = bpy.context.scene.cursor.location

x_cursor_location = my_cursor_location.x
y_cursor_location = my_cursor_location.y
z_cursor_location = my_cursor_location.z

for obj in range(10):

    # Creation of UV Sphere in the location of the cursor
    bpy.ops.mesh.primitive_uv_sphere_add(segments=32, ring_count=16, radius=1.0, calc_uvs=True, enter_editmode=False, align='WORLD', location=(x_cursor_location, y_cursor_location, z_cursor_location), rotation=(radians(90), 0.0, 0.0))

    # Add modifyers such as subdivision surfaces
    bpy.ops.object.modifier_add(type='SUBSURF')

    # Sets subdivision modifier to 2
    bpy.context.object.modifiers["Subdivision"].levels = 2

    # Shades the UV sphere object smooth
    bpy.ops.object.shade_smooth()

    x_cursor_location += 5
    y_cursor_location += 5
    z_cursor_location += 5