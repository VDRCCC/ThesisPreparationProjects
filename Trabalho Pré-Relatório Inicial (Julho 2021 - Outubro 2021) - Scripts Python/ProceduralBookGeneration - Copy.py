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
       
        
def create_cube(x_size, y_size, z_size):
    bpy.ops.mesh.primitive_cube_add()
    
    resize(x_size, y_size, z_size)
    align(x_size, y_size, z_size)
    
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
    
    
def align(x, y, z):
    bpy.ops.transform.translate(value = (x, y, z))


def resize(x, y, z):
    bpy.ops.transform.resize(value = (x, y, z))
    
    
def loopcut(number_of_cuts, edge_index, offset):
    
    context_override = get_context_override()
    
    bpy.ops.mesh.loopcut_slide(
    
        context_override, 
        
        MESH_OT_loopcut = {
            "number_cuts": number_of_cuts,
            "smoothness": 0,
            "falloff": "INVERSE_SQUARE",
            "object_index": 0,
            "edge_index": edge_index,
            "mesh_select_mode_init": (False, False, True)
        },
            
        TRANSFORM_OT_edge_slide = {
            "value": offset,
            "single_side": False,
            "use_even": False,
            "flipped": False,
            "use_clamp": True,
            "mirror": True,
            "snap": False,
            "snap_target": 'CLOSEST',
            "snap_point": (0, 0, 0),
            "snap_align": False,
            "snap_normal": (0, 0, 0),
            "correct_uv": True,
            "release_confirm": False,
            "use_accurate": False
        }
    )


def extrude_faces(amount):
    
    bpy.ops.object.mode_set(mode = "EDIT")
    
    bpy.ops.mesh.extrude_region_shrink_fatten(MESH_OT_extrude_region = {
            "use_normal_flip":False,
            "use_dissolve_ortho_edges":False,
            "mirror":False
        },
        TRANSFORM_OT_shrink_fatten = {
            "value":amount,
            "use_even_offset":False,
            "mirror":False,
            "use_proportional_edit":False,
            "proportional_edit_falloff":'SMOOTH',
            "proportional_size":1,
            "use_proportional_connected":False,
            "use_proportional_projected":False,
            "snap":False, "snap_target":'CLOSEST',
            "snap_point":(0, 0, 0),
            "snap_align":False,
            "snap_normal":(0, 0, 0),
            "release_confirm":False,
            "use_accurate":False
        }
    )
    

def model_book():
    context_override = get_context_override()
    
    bpy.ops.object.mode_set(mode = "EDIT")
    loopcut(1, 8, -0.8)
    
    loopcut(1, 15, 0)
    resize(0.85, 1, 1)
    
    loopcut(2, 11, 0)
    resize(2.2, 1, 1)
    
def update_mesh(object):
    bpy.ops.object.mode_set(mode = "OBJECT")
    object.data.update(calc_edges = False)
    
def get_faces(book):
    top_face = None
    bottom_face = None
    front_face = None
    
    update_mesh(book)
    for face in book.data.polygons:
        face_normal = face.normal
        face_area = face.area
        
        if round(face_normal[2]) == 1:
            if top_face == None:
                top_face = face
            else:
                if top_face.area < face.area:
                    top_face = face
                    
        elif round(face_normal[2]) == -1:
            if bottom_face == None:
                bottom_face = face
            else:
                if bottom_face.area < face.area:
                    bottom_face = face
                    
        elif round(face_normal[1]) == -1:
            if front_face == None:
                front_face = face
            else:
                if front_face.area < face.area:
                    front_face = face
                    
    return top_face, bottom_face, front_face


def select_faces(object, face_indexes):
    bpy.ops.object.mode_set(mode = "EDIT")
    bpy.ops.mesh.select_all(action = "DESELECT")
    
    bpy.ops.object.mode_set(mode = "OBJECT")
    for face_index in face_indexes:
        object.data.polygons[face_index].select = True
        
def create_material(name, color):
    material = bpy.data.materials.new(name)
    material.diffuse_color = color
    
    return material


def assign_materials(object):
    cover_material = create_material("cover_material",(
        random.uniform(0, 1),
        random.uniform(0, 1),
        random.uniform(0, 1),
        1
    ))
    # material index 0
    object.data.materials.append(cover_material)
    
    paper_material = create_material("paper_material",(
        random.uniform(0.863, 1),
        random.uniform(0.256, 1),
        random.uniform(0, 1),
        1
    ))
    paper_material.specular_intensity = 0.1
    # material index 1
    object.data.materials.append(paper_material)
    
    bpy.context.object.active_material_index = 1
    bpy.ops.object.material_slot_assign()
    

def create_book(x_size, y_size, z_size):
    book = create_cube(x_size, y_size, z_size)
    
    model_book()
    
    top_face, bottom_face, front_face = get_faces(book)
    
    select_faces(book, [top_face.index, bottom_face.index, front_face.index])
    
    extrude_faces(-0.05)
    assign_materials(book)
    
    bpy.ops.object.mode_set(mode = "OBJECT")
    
def create_book_shelf(number_of_books):
    
    x_position = 0
    
    for i in range(number_of_books):
        x_size = random.uniform(0.15, 0.3)
        y_size = random.uniform(0.7, 0.9)
        z_size = random.uniform(1, 1.2)
            
        create_book(x_size, y_size, z_size)
        
        y_deviation = random.uniform(-0.2, 0.2)
        
        bpy.ops.transform.translate(value = (x_position*2, y_deviation, 0))
        x_gap = random.uniform(0.007, 0.09)
        x_position += x_size + x_gap
        
        

clean_scene()
create_book_shelf(15)