import bpy
import random



def clean_scene():
    for object in bpy.data.objects:
        bpy.data.objects.remove(object)
        
    for material in bpy.data.materials:
        bpy.data.materials.remove(material)
        
    for texture in bpy.data.textures:
        bpy.data.textures.remove(texture)
        
    for mesh in bpy.data.meshes:
        bpy.data.meshes.remove(mesh)



clean_scene()



def resize(x, y, z):
    bpy.ops.transform.resize(value = (x, y, z))
    


def create_cube(size_value):
    bpy.ops.mesh.primitive_cube_add(size=size_value)
    
    return bpy.context.selected_objects[0]



def get_context_override():
    window = bpy.context.window
    screen = window.screen
    area = next(area for area in screen.areas if area.type == "VIEW_3D")
    region = next(region for region in area.regions if region.type == "WINDOW")
    
    return {
        "window": window,
        "screen": screen,
        "area": area,
        "region": region,
        "scene": bpy.context.scene
    }
    


def create_material(name, color): 
    
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    
    return material



def assign_material(object, name, color):
    road_material = create_material(name, color)
    object.data.materials.append(road_material)
    
    
    
def create_road_lines(type, road_size, road_length, road_width):
    
    context_override = get_context_override()
    
    if type == 1:
        lines = create_cube(road_size)
        
        resize(0.02, road_length, 0.01)
    
#        lines.scale[0] =  0.02
#        lines.scale[1] = road_length
#        lines.scale[2] = 0.01
        
        lines.location = (0, 0, 0.49)
        
        assign_material(lines, "road_lines_material", (1, 1, 1, 1))
    
    elif type == 2:
        
        number_of_lines = round(road_size * road_length / 3)
        
        y_location_of_line = 0
        
        for line in range(number_of_lines):
            
            line = create_cube(road_size)
            
            resize(0.02, 0.1, 0.01)
        
#            line.scale[0] =  0.02
#            line.scale[1] = 0.1
#            line.scale[2] = 0.01
            
            line.location = (0, -road_size * road_length / 2 + road_size * bpy.context.object.scale[1] / 2 + y_location_of_line, 0.49)
        
            assign_material(line, "road_lines_material", (1, 1, 1, 1))
            
            y_location_of_line += 3
    
    elif type == 3:
        lines1 = create_cube(road_size)
        
        resize(0.02, road_length, 0.01)
    
#        lines1.scale[0] = 0.02
#        lines1.scale[1] = road_length
#        lines1.scale[2] = 0.01
        
        lines1.location = (-0.3, 0, 0.49)
        
        assign_material(lines1, "road_lines_material1", (1, 1, 1, 1))
        
        lines2 = create_cube(road_size)
        
        resize(0.02, road_length, 0.01)
    
#        lines2.scale[0] = 0.02
#        lines2.scale[1] = road_length
#        lines2.scale[2] = 0.01
        
        lines2.location = (0.3, 0, 0.49)
        
        assign_material(lines2, "road_lines_material2", (1, 1, 1, 1))
        
    else:
        
        x_location = road_size * road_width / 2
        
        lines3 = create_cube(road_size)

        resize(0.02, road_length, 0.01)

#        lines3.scale[0] = 0.02
#        lines3.scale[1] = road_length
#        lines3.scale[2] = 0.01
        
        lines3.location = (- x_location + 0.5, 0, 0.49)
        
        assign_material(lines3, "road_lines_material3", (1, 1, 1, 1))
        
        lines4 = create_cube(road_size)
        
        resize(0.02, road_length, 0.01)
    
#        lines4.scale[0] = 0.02
#        lines4.scale[1] = road_length
#        lines4.scale[2] = 0.01
        
        lines4.location = (x_location - 0.5, 0, 0.49)
        
        assign_material(lines4, "road_lines_material4", (1, 1, 1, 1))
            
            

def create_road(road_size):
    road = create_cube(road_size)
    
    bpy.context.object.scale[0] = round(random.uniform(1, 2))
    bpy.context.object.scale[1] = round(random.uniform(10, 20))
    bpy.context.object.scale[2] = 1/road_size
    
    assign_material(road, "road_material", (0.00901859, 0.00901859, 0.00901859, 1))
    
    road.location = (0, 0, 0)
    
    #create_road_lines(4, road_size, bpy.context.object.scale[1], bpy.context.object.scale[0])
    
    if bpy.context.object.scale[0] == 2:
        create_road_lines(round(random.uniform(1, 3)), road_size, bpy.context.object.scale[1], bpy.context.object.scale[0])
    
    
create_road(10)