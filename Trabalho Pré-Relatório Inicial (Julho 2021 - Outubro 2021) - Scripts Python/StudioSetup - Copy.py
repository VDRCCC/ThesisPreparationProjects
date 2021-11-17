# Adds bpy module
import bpy

# ---------------------------------------------------------------
#     Section Reserved For Plane Creation and Modification
# ---------------------------------------------------------------

# Creates a filled planar mesh with 4 vertices
bpy.ops.mesh.primitive_plane_add(size=15, enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))

# For loop renaming all objects selected
for obj in bpy.context.selected_objects:
    obj.name = "theBackground"
    obj.data.name = "theBackground"
    
# Sets specified object's interaction mode    
bpy.ops.object.mode_set(mode='EDIT')

# Subdivides the plane with 3 cuts
bpy.ops.mesh.subdivide(number_cuts=3)

# Sets the object interaction mode
bpy.ops.object.mode_set(mode='OBJECT')

# List with the vertices than need changing
vertex_list = [15, 14, 13, 2, 3]

# Altering the z values for a list of vertices
for vertex in vertex_list:
    bpy.data.objects["theBackground"].data.vertices[vertex].co.z += 8

# Sets a Subdivision Surface level of 2
bpy.ops.object.subdivision_set(level=2, relative=False)

# Shades the plane smooth
bpy.ops.object.shade_smooth()


# ---------------------------------------------------------------
#     Section Reserved For Camera Creation and Modification
# ---------------------------------------------------------------

bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, -6, 1), rotation=(1.570796, 0, 0), scale=(1, 1, 1))


# ---------------------------------------------------------------
#     Section Reserved For Monkey Creation and Modification
# ---------------------------------------------------------------

# Creates a monkey mesh
bpy.ops.mesh.primitive_monkey_add(size=2, enter_editmode=False, align='WORLD', location=(0, 0, 1), scale=(1, 1, 1))

# Sets a Subdivision Surface level of 2
bpy.ops.object.subdivision_set(level=2, relative=False)

# Shades the plane smooth
bpy.ops.object.shade_smooth()


# ---------------------------------------------------------------
#     Section Reserved For Light Creation and Modification
# ---------------------------------------------------------------

# Adds a light to the scene
bpy.ops.object.light_add(type='AREA', radius=1, align='WORLD', location=(-2.7, -2.5, 3.3), scale=(1, 1, 1), rotation=(1.0472, 0.174533, -0.872665))

# Calibrates the light's power
bpy.context.object.data.energy = 100

# For loop renaming all objects selected
for obj in bpy.context.selected_objects:
    obj.name = "KeyLight"
    obj.data.name = "KeyLight"

# Adds a light to the scene
bpy.ops.object.light_add(type='AREA', radius=1, align='WORLD', location=(3.2, --3.2, 2.4), scale=(1, 1, 1), rotation=(1.309, -0.261799, 0.872665))

# Calibrates the light's power
bpy.context.object.data.energy = 30

# For loop renaming all objects selected
for obj in bpy.context.selected_objects:
    obj.name = "FillLight"
    obj.data.name = "FillLight"