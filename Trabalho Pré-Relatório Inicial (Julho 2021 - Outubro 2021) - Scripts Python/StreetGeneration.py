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

class RoadGeneration:
    
    def __init__(self, name, road_size, material_name, material_color, line_type, line_material_name, line_material_color):
        self.name = name
        self.road_size = road_size
        self.material_name = material_name
        self.material_color = material_color
        self.line_type = line_type
        self.line_material_name = line_material_name
        self.line_material_color = line_material_color
        
    def generate(self):
        bpy.ops.mesh.primitive_cube_add(size=self.road_size)
        
        road = bpy.context.selected_objects[0]
        
        road.name = self.name
        
        road.scale[0] = round(random.uniform(1, 2))
        road.scale[1] = round(random.uniform(10, 20))
        road.scale[2] = 1/self.road_size
        
        road.location = (0, 0, 0)
        
        road_material = bpy.data.materials.new(self.material_name)
        road_material.diffuse_color = self.material_color
        road.data.materials.append(road_material)
        
    def generate_line(self):
        road = bpy.context.selected_objects[0]
        
        print(self.line_type)
        
        if self.line_type == 1:
            bpy.ops.mesh.primitive_cube_add(size=self.road_size)
            
            lines = bpy.context.selected_objects[0]
            
            bpy.ops.transform.resize(value = (0.02, road.scale[1], 0.01))
            
            lines.location = (0, 0, 0.49)
            
            line_material = bpy.data.materials.new(self.line_material_name)
            line_material.diffuse_color = self.line_material_color
            road.data.materials.append(line_material)
    
        elif self.line_type == 2:
            
            number_of_lines = round(self.road_size * road.scale[1] / 3)
            
            y_location_of_line = 0
            
            for line in range(number_of_lines):
                
                bpy.ops.mesh.primitive_cube_add(size=self.road_size)
                
                line = bpy.context.selected_objects[0]
                
                bpy.ops.transform.resize(value = (0.02, 0.1, 0.01))
                
                line.location = (0, -self.road_size * road.scale[1] / 2 + self.road_size * bpy.context.object.scale[1] / 2 + + y_location_of_line, 0.49)
                
                line_material = bpy.data.materials.new(self.line_material_name)
                line_material.diffuse_color = self.line_material_color
                road.data.materials.append(line_material)
            
                line_material = bpy.data.materials.new(self.line_material_name)
                line_material.diffuse_color = self.line_material_color
                road.data.materials.append(line_material)
                
                y_location_of_line += 3
        
        elif self.line_type == 3:
            bpy.ops.mesh.primitive_cube_add(size=self.road_size)
            
            lines1 = bpy.context.selected_objects[0]
            
            bpy.ops.transform.resize(value = (0.02, road.scale[1], 0.01))
            
            lines1.location = (-0.3, 0, 0.49)
            
            line_material = bpy.data.materials.new(self.line_material_name)
            line_material.diffuse_color = self.line_material_color
            road.data.materials.append(line_material)
            
            bpy.ops.mesh.primitive_cube_add(size=self.road_size)
            
            lines2 = bpy.context.selected_objects[0]
            
            bpy.ops.transform.resize(value = (0.02, road.scale[1], 0.01))
            
            lines2.location = (0.3, 0, 0.49)
            
            line_material = bpy.data.materials.new(self.line_material_name)
            line_material.diffuse_color = self.line_material_color
            road.data.materials.append(line_material)
            
        else:
            
            x_location = self.road_size * road.scale[2] / 2
            
            bpy.ops.mesh.primitive_cube_add(size=self.road_size)
            
            lines3 = bpy.context.selected_objects[0]
            
            bpy.ops.transform.resize(value = (0.02, road.scale[1], 0.01))
            
            lines3.location = (- x_location + 0.5, 0, 0.49)
            
            line_material = bpy.data.materials.new(self.line_material_name)
            line_material.diffuse_color = self.line_material_color
            road.data.materials.append(line_material)
            
            bpy.ops.mesh.primitive_cube_add(size=self.road_size)
            
            lines4 = bpy.context.selected_objects[0]
            
            bpy.ops.transform.resize(value = (0.02, road.scale[1], 0.01))
            
            lines4.location = (x_location - 0.5, 0, 0.49)
            
            line_material = bpy.data.materials.new(self.line_material_name)
            line_material.diffuse_color = self.line_material_color
            road.data.materials.append(line_material)
        
        

Road = RoadGeneration("Road", 10, "Asphalt", (0.00901859, 0.00901859, 0.00901859, 1), round(random.uniform(1, 3)), "Lines", (1, 1, 1, 1))
Road.generate()
Road.generate_line()