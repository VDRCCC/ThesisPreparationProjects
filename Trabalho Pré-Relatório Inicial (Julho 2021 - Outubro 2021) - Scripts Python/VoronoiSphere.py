import bpy
import math

def clean_scene():
    for object in bpy.data.objects:
        bpy.data.objects.remove(object)
        
def create_cube():
    
    bpy.ops.mesh.primitive_cube_add(size = 1)
    
    return bpy.context.object
        
def create_sphere():
    
    # Create a cube
    cube = create_cube()
    
    # Subdivide it
    subdiv_modifier = cube.modifiers.new(type = 'SUBSURF', name = 'subdiv_cube')
    
    
    # Increase resolution
    subdiv_modifier.levels = 5
    
    bpy.ops.object.modifier_apply(modifier = 'subdiv_cube')
    
    # Spherify it (apply cast)
    cast_modifier = cube.modifiers.new(type = 'CAST', name = 'cast_cube')
    
    bpy.ops.object.modifier_apply(modifier = 'cast_cube')
    
    # Decimate it (planar surfaces)
    decimate_modifier = cube.modifiers.new(type = 'DECIMATE', name = 'decimate_cube')
    decimate_modifier.decimate_type = 'DISSOLVE'
    decimate_modifier.angle_limit = math.radians(20)
    decimate_modifier.use_dissolve_boundaries = True
    
    bpy.ops.object.modifier_apply(modifier = 'decimate_cube')
        
clean_scene()
create_sphere()