import bpy
import random

def clean_scene():
    for object in bpy.data.objects:
        bpy.data.objects.remove(object)
        
    for texture in bpy.data.textures:
        bpy.data.textures.remove(texture)
        
def create_cube():
    bpy.ops.mesh.primitive_cube_add()
    return bpy.context.object

def subdivide(object, name, levels):
    modifier = object.modifiers.new(type = "SUBSURF", name = name)
    modifier.levels = levels
    
def create_voronoi_texture(intensity, scale):
    texture = bpy.data.textures.new("voronoi", type = "VORONOI")
    texture.distance_metric = "DISTANCE_SQUARED"
    texture.noise_intensity = intensity
    texture.noise_scale = scale
    
    return texture
    
def displace(object, name, intensity, scale):
    modifier = object.modifiers.new(type = "DISPLACE", name = name)
    texture = create_voronoi_texture(intensity, scale)
    modifier.texture = texture
    
    
def decimate(object, name, ratio):
    modifier = object.modifiers.new(type = "DECIMATE", name = name)
    modifier.ratio = ratio
    
def get_vertex_offset(vertex, scale):
    direction = vertex.normal
    direction[0] += random.uniform(-0.5, 0.5)
    direction[1] += random.uniform(-0.5, 0.5)
    direction[2] += random.uniform(-0.5, 0.5)
    
    return direction * scale
    
def offset_vertices(object):
    for vertex in object.data.vertices:
        vertex.co = get_vertex_offset(vertex, 3)
        
def collapse_modifiers(object):
    for modifier in object.modifiers:
        bpy.ops.object.modifier_apply(modifier = modifier.name)
        
def create_rock():
    cube = create_cube()
    
    subdivide(cube, "subdivide", 5)
    displace(cube, "displace", random.uniform(0.4, 0.8), random.uniform(1.5, 2))
    decimate(cube, "decimate", 0.25)
    
    offset_vertices(cube)
    collapse_modifiers(cube)

clean_scene()
create_rock()