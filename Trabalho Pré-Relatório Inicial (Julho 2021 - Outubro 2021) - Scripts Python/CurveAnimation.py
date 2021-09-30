# Adds bpy module
import bpy

# ---------------------------------------------------------------
#        Section Reserved For Coordenate List Creation
# ---------------------------------------------------------------

# A list of coordenates for a set of points in a curve
coordsList = [[12, 2, 5], [9, 6, 4], [8, 1, 3], [0, 4, 2], [-7, -16, 1]]

curveList = []

# Lists with RGB values for colors to be used in the curve objects
colorList1 = [0.8, 0.0, 0.004, 1.0]
colorList2 = [0.004, 0.0, 0.8, 1.0]
colorList3 = [0.076, 0.883, 0.906, 1.0]
colorList4 = [0.017, 0.8, 0.0, 1.0]

# List containing camera location coordenates
camCoordsList = [[12, 2, 5], [11, 2, 4], [8, 0, 3], [0.7, -6, 2], [-7, -16, 1]]

# List containing camera location coordenates
camRotationList = [[1.570800, 0, -0.561918], [1.570800, 0, -0.450954], [1.570800, 0, 0.481517], [1.434536, 0.086752, 0.829282], [1.293639, 0.085921, 0.676657]]
# ---------------------------------------------------------------
#   Section Reserved For Curve Object Creation and Modification
# ---------------------------------------------------------------

for eachObject in range(0, 4):

    # Add a new curve to the main database
    theCurveObject = bpy.data.curves.new('CurveObject', 'CURVE')

    # Determines the number of dimensions of the curve as 3
    theCurveObject.dimensions = '3D'

    # Adds a new sline to the curve
    splineObject = theCurveObject.splines.new(type = 'NURBS')

    # Add a number of points to this spline
    splineObject.points.add(len(coordsList)-1)

    # Applies the coordenates within coordList to the splineObject's points
    for vertex in range(len(coordsList)):
        x, y, z = coordsList[vertex]
        splineObject.points[vertex].co = (x, y, z, 1)
        
    # Generate a new object with the curve
    curveObject = bpy.data.objects.new('crv_line', theCurveObject)

    # Link the curve object to the scene collection
    bpy.context.scene.collection.objects.link(curveObject)

    # Activate the object
    bpy.context.view_layer.objects.active = curveObject

    # Append any curve created so they can be iterated over at a later moment
    curveList.append(curveObject)

    # Iterates over curveList moving each curve object 0.05 meters on the x axis
    for object in curveList:
        object.location.x += 0.05
        
    # Defines curve thickness at 0.02 meters
    bpy.context.object.data.bevel_depth = 0.02


    # ---------------------------------------------------------------
    #    Section Reserved For Animation Creation and Modification
    # ---------------------------------------------------------------

    # Sets timeline to 1
    bpy.context.scene.frame_set(1)

    # Set factor to 1
    bpy.context.object.data.bevel_factor_start = 1

    # Access active object's data and place key frame on it's bevel start value
    bpy.context.object.data.keyframe_insert(data_path = 'bevel_factor_start')

    # Sets timeline to 50
    bpy.context.scene.frame_set(50)

    # Set factor to 0
    bpy.context.object.data.bevel_factor_start = 0

    # Access active object's data and place key frame on it's bevel start value
    bpy.context.object.data.keyframe_insert(data_path = 'bevel_factor_start')

    # Sets the animation frame range of the timeline to 50
    bpy.context.scene.frame_end = 50
    
    
# ------------------------------------------------------------------------
#   Section Reserved For Curve Object Material Creation and Modification
# ------------------------------------------------------------------------

# Create a new variable and assign it to a new material
curveMaterial = bpy.data.materials.get('M_curve_line')
if curveMaterial is None:
    curveMaterial = bpy.data.materials.new(name = 'M_curve_line')
    
print(curveMaterial)
    
# Set use nodes to True
curveMaterial.use_nodes = True

# For loop to check for and delete existing nodes
curveNodes = curveMaterial.node_tree.nodes
for node in curveNodes:
    curveNodes.remove(node)
    
# Adds back a material output node
mattOutput = curveNodes.new(type = 'ShaderNodeOutputMaterial')

# Assign new material node to a variable
emissionType = curveMaterial.node_tree.nodes.new('ShaderNodeEmission')

# Set color of new material
emissionType.inputs[0].default_value = (colorList4)

# Sets emission strenght
emissionType.inputs[1].default_value = 20

# Link emission shader to material
curveMaterial.node_tree.links.new(mattOutput.inputs[0], emissionType.outputs[0])

# Copy material settings to every curve in the scene
mat = curveMaterial.copy()
mat.name = 'M_crv_line.001'
emissionType.inputs[0].default_value = (colorList1)
bpy.data.objects['crv_line.001'].active_material = mat

mat2 = curveMaterial.copy()
mat2.name = 'M_crv_line.002'
emissionType.inputs[0].default_value = (colorList2)
bpy.data.objects['crv_line.002'].active_material = mat2

mat3 = curveMaterial.copy()
mat3.name = 'M_crv_line.003'
emissionType.inputs[0].default_value = (colorList3)
bpy.data.objects['crv_line.003'].active_material = mat3

mat4 = curveMaterial.copy()
mat4.name = 'M_crv_line'
emissionType.inputs[0].default_value = (colorList4)
bpy.data.objects['crv_line'].active_material = mat4

# Change background color to black
bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0, 0, 0, 1)

# Activate bloom and maximise it's threshold
bpy.context.scene.eevee.use_bloom = True
bpy.context.scene.eevee.bloom_threshold = 10


# ---------------------------------------------------------------
#   Section Reserved For Camera Creation and Modification
# ---------------------------------------------------------------

# Add camera to the scene
bpy.ops.object.camera_add(enter_editmode=False, align='VIEW', location=(0, 0, 0), rotation=(0, 0, 0), scale=(1, 1, 1))

camObject = bpy.context.object

# Sets camera location from list
camObject.location = camCoordsList[4]
camObject.rotation_euler = camRotationList[0]

# Set keyframe for camera location at frame 1
camObject.keyframe_insert(data_path = 'location', frame = 1)

# Set keyframe for camera rotation at frame 1
camObject.keyframe_insert(data_path = 'rotation_euler', frame = 1)

# Sets camera location from list
camObject.location = camCoordsList[3]
camObject.rotation_euler = camRotationList[1]

# Set keyframe for camera location at frame 15
camObject.keyframe_insert(data_path = 'location', frame = 15)

# Set keyframe for camera rotation at frame 15
camObject.keyframe_insert(data_path = 'rotation_euler', frame = 15)

# Sets camera location from list
camObject.location = camCoordsList[2]
camObject.rotation_euler = camRotationList[2]

# Set keyframe for camera location at frame 25
camObject.keyframe_insert(data_path = 'location', frame = 25)

# Set keyframe for camera rotation at frame 25
camObject.keyframe_insert(data_path = 'rotation_euler', frame = 25)

# Sets camera location from list
camObject.location = camCoordsList[1]
camObject.rotation_euler = camRotationList[3]

# Set keyframe for camera location at frame 37
camObject.keyframe_insert(data_path = 'location', frame = 37)

# Set keyframe for camera rotation at frame 37
camObject.keyframe_insert(data_path = 'rotation_euler', frame = 37)

# Sets camera location from list
camObject.location = camCoordsList[0]
camObject.rotation_euler = camRotationList[4]

# Set keyframe for camera location at frame 50
camObject.keyframe_insert(data_path = 'location', frame = 50)

# Set keyframe for camera rotation at frame 50
camObject.keyframe_insert(data_path = 'rotation_euler', frame = 50)