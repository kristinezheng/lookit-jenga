import bpy
import json
import os 
import sys
import numpy as np
import random
from mathutils import Matrix
from math import radians
from pathlib import Path

for material in bpy.data.materials:
    material.user_clear()
    bpy.data.materials.remove(material)
    
for cam in bpy.data.cameras:
    cam.user_clear()
    bpy.data.cameras.remove(cam)


def deleteAllObjects():
    """
    Deletes all objects in the current scene
    """
    deleteListObjects = ['MESH', 'CURVE', 'SURFACE', 'META', 'FONT', 'HAIR', 'POINTCLOUD', 'VOLUME', 'GPENCIL',
                     'ARMATURE', 'LATTICE', 'EMPTY', 'LIGHT', 'LIGHT_PROBE', 'CAMERA', 'SPEAKER']

    # Select all objects in the scene to be deleted:

    for o in bpy.context.scene.objects:
        for i in deleteListObjects:
            if o.type == i:
                o.select_set(False)
            else:
                o.select_set(True)
    # Deletes all selected objects in the scene:

    bpy.ops.object.delete() 

deleteAllObjects()
    
    
height = 10
json_dir = Path(f'/Users/kristinezheng/jenga-performance-art/json/{height}_tall')
possible_paths = list(json_dir.iterdir())

## relative_path = os.path.join('json', f'{height}_tall', possible_paths[0])
## path = os.path.abspath(os.path.join('..', '..',relative_path))
# k = [1,2,3][0]
#2,4,5 is height 10???
# 7 is similar to another
path = f'/Users/kristinezheng/lookit-jenga/blender_src/block_spec_1.json'
# (f'/Users/kristinezheng/jenga-performance-art/json/{height}_tall/' 
    # + 
    #'0.0125_2_1693092780.1328928.json'
    #'0.251875_4_1693092812.6565719.json'
    #'0.51_6_1693093115.2289646.json'
    #'0.73125_1_1693093162.5186362.json'
    #'0.819375_1_1693093207.721501.json'
    #'0.584375_1_1693092890.8446198.json'
    
    #'0.7585714285714285_6_1693094665.55217.json'
    #'0.5039285714285714_1_1693094729.2312584.json'
    #'0.9785714285714286_7_1693094286.9956653.json'
    #'0.4714285714285714_3_1693094475.5026772.json'
    
    #'0.9833333333333334_4_1693100566.4094222.json'
    #'0.7494444444444444_1_1693100078.7675319.json'
    #'0.5013888888888888_6_1693100678.0054057.json'
    # '0.8277777777777778_8_1693100262.8454077.json'
   
    # )


with open(path) as file:
    file_contents = file.read()
    
parsed_dict = json.loads(file_contents)
 
############
#####
floor_mat = bpy.data.materials.new(name = "Floor")
floor_mat.use_nodes = True
# let's create a variable to store our list of nodes
floor_mat_nodes = floor_mat.node_tree.nodes

# let's set the metallic to 1.0
floor_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.319199, 0.66187, 0.66187, 0.8)

#(0.1, 0.2, 0.2, 0.8)
floor_mat_nodes['Principled BSDF'].inputs['Roughness'].default_value=1.0
    
def make_floor(mat):
    floor = bpy.ops.mesh.primitive_plane_add(size = 10, location=(0.0, 0.0, -0.05))
    bpy.ops.object.modifier_add(type='BEVEL')
    bpy.context.object.modifiers["Bevel"].affect = 'VERTICES'
    bpy.context.object.modifiers["Bevel"].width = 5
    bpy.context.object.modifiers["Bevel"].segments = 30

    # bpy.ops.rigidbody.object_add()
    # bpy.context.object.rigid_body.type = 'PASSIVE'

#    bpy.context.object.rigid_body.friction = 1
#    bpy.context.object.rigid_body.collision_margin = 0
#    bpy.context.object.rigid_body.use_margin = True
#    bpy.context.object.rigid_body.linear_damping = 0.35
#    bpy.context.object.rigid_body.angular_damping = 0.6

    floor = bpy.context.active_object

    if floor.data.materials:
        # assign to 1st material slot
        floor.data.materials[0] = mat
    else:
        # no slots
        floor.data.materials.append(mat)
    
make_floor(floor_mat)

#####
#create material
wood_mat = bpy.data.materials.new(name = "Wood")
wood_mat.use_nodes = True
# let's create a variable to store our list of nodes
wood_mat_nodes = wood_mat.node_tree.nodes

# let's set the metallic to 1.0
wood_mat_nodes['Principled BSDF'].inputs['Metallic'].default_value=0.5
#wood_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.05, 0.0185, 0.8, 1.0)
bsdf = wood_mat.node_tree.nodes["Principled BSDF"]
texImage = wood_mat.node_tree.nodes.new('ShaderNodeTexImage')
#texture_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'images/plywood.png'))
texture_path = '/Users/kristinezheng/jenga-performance-art/images/wood_grain1.png'
#'/Users/isabellayu/jenga-performance-art/images/wood_grain.png'
texImage.image = bpy.data.images.load(texture_path)
wood_mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

wood_mat_nodes['Principled BSDF'].inputs['Roughness'].default_value=0.167
obj_dict = {
    "pos": [
      0,
      0,
      0.15
    ],
    "ori": [
      0,
      0,
      0,
      1
    ],
    "linVel": [
      0,
      0,
      0
    ],
    "angVel": [
      0,
      0,
      0
    ],
    "x_size": 1.5,
    "y_size": 0.5,
    "z_size": 0.3,
    "mass": 0.225,
    "friction": 0.5
  }

def make_tower(obj_dict, num_obj = 20, mat=None, x_shift = 0):
    Tower = bpy.context.blend_data.collections.new("Tower")
    bpy.context.collection.children.link(Tower)
    positions = []
    z_stack = obj_dict['pos'][2]*2
    x_y_z_dim = (obj_dict['x_size'], obj_dict['y_size'], obj_dict['z_size'])
    current_pos = (obj_dict['pos'][0], obj_dict['pos'][1], obj_dict['pos'][2])
    rotation = obj_dict['ori']
    for i in range(0, num_obj):
#        print(i, obj['pos'])

        bpy.ops.mesh.primitive_cube_add(size=1, location = current_pos, scale = x_y_z_dim)
        bpy.context.object.rotation_mode='QUATERNION'
        bpy.context.object.rotation_quaternion=rotation
        
        # bpy.ops.rigidbody.object_add()
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].width = 0.02
        bpy.ops.object.shade_smooth()

        # bpy.context.object.rigid_body.mass = obj_dict['mass']
        # bpy.context.object.rigid_body.friction = obj['friction']
        # bpy.context.object.rigid_body.collision_margin = 0
        # bpy.context.object.rigid_body.use_margin = True
        # bpy.context.object.rigid_body.linear_damping = 0.35
        # bpy.context.object.rigid_body.angular_damping = 0.6
            
        # bpy.context.active_object.rotation_mode = 'QUATERNION'
        # #xyzw to wxyz
        # bpy.context.active_object.rotation_quaternion = (obj['ori'][3], obj['ori'][0], obj['ori'][1], obj['ori'][2])

        # cube = bpy.context.active_object
        # print("LOCATION", cube.location)
        # positions.append(cube.location)
        positions.append(bpy.context.object.location)

        Tower.objects.link(bpy.context.object)
        if i == 0:
            current_pos = (current_pos[0] + x_shift*(i+1), current_pos[1], current_pos[2] +10+ z_stack)
        else:
            current_pos = (current_pos[0] + x_shift, current_pos[1], current_pos[2]+ z_stack)# + z_stack*i)
        
    #set cubes to material 
    if mat:
        for ob in Tower.all_objects:
            if ob.data.materials:
            # assign to 1st material slot
                ob.data.materials[0] = mat
            else:
            # no slots
                ob.data.materials.append(mat)    
    return Tower, positions

#BlockTower, BlockPositions = make_tower(parsed_dict, wood_mat)
block_tower, positions = make_tower(obj_dict, 20, wood_mat, x_shift = 0.15) #0.15, 0, 0.3
#0,0.3,0.15

### make grease pencil
bpy.ops.object.gpencil_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1), type='LRT_OBJECT')
gp = bpy.context.active_object
gp.grease_pencil_modifiers["Line Art"].thickness = 10
gp.grease_pencil_modifiers["Line Art"].opacity = 0.5
gp.grease_pencil_modifiers["Line Art"].source_type = 'COLLECTION'
gp.grease_pencil_modifiers["Line Art"].source_collection = bpy.data.collections["Tower"]

bpy.context.scene.view_layers["ViewLayer"].use_pass_z = True

block_dim = (1.5/1.2,0.5/1.2,0.3/1.2)
num_blocks = len(list(parsed_dict.keys()))
#add light
light_data = bpy.data.lights.new("light", type ="AREA")
light = bpy.data.objects.new("light", light_data)
bpy.context.collection.objects.link(light)
light.location = (block_dim[0]*1.5,block_dim[0]*1.5,block_dim[0]*(num_blocks+3))#(1.5,1.5,5)
#light.data.shape = 'DISK'
#light.data.energy = 1500
#light.data.diffuse_factor = 5
#light.data.size = 50
light.data.energy = 15000
light.data.diffuse_factor = 200
light.data.size = 1000
light.data.use_contact_shadow = True
prev_block = positions[0]
prev_block_height = 10 * 0.3
print("PREV HEIGHT", prev_block, prev_block_height)

light.data.use_shadow = False
        
        
light_data2 = bpy.data.lights.new("light2", type ="AREA")
light_data2.energy = 5000
light2 = bpy.data.objects.new("light2", light_data2)
bpy.context.collection.objects.link(light2)
light2.location = (-5,-5,10)

light2.data.diffuse_factor = 600
light2.data.specular_factor = 30 
light2.data.size = 1000
light2.data.use_contact_shadow = True 

#rotate camera
# empty_cube = bpy.ops.object.empty_add(type='CUBE', align='WORLD', 
#         location=(0, 0, prev_block_height / 2), scale=(1,1,1))

#bpy.ops.transform.resize(value=(1.5,1.5,1.5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#bpy.ops.transform.resize(value=(block_dim[0]*2,block_dim[0]*2,prev_block_height), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

#create camera
cam_data = bpy.data.cameras.new('camera')
cam = bpy.data.objects.new('camera', cam_data)
bpy.context.collection.objects.link(cam)
cam.location = (2,12,3)#(4,10,3)


cam.rotation_mode = "XYZ"
cam.rotation_euler=(84 * np.pi/180, 0, 175 * np.pi/180)
#(84 * np.pi/180, 0, 158 * np.pi/180)
# cam.rotation_euler.to_quaternion()

#connect camera to empty cube 
# e = bpy.data.objects['Empty']
# print(e)
# c = bpy.data.objects['camera']
# c.parent = e 
# c.data.clip_end = 500

# rotate 
#e.keyframe_insert("rotation_euler", frame=1) # assuming rotation_mode being euler by default
#e.matrix_world = Matrix.Translation(e.location) * Matrix.Rotation(radians(45), 4, 'Z')
#e.keyframe_insert("rotation_euler", frame=50)


t = bpy.data.collections['Tower']
c_coll = t.objects
# for c in range(1)):
c_coll[1].keyframe_insert("location", frame = 0)

z_stack = obj_dict['pos'][2]*2
# assume 400 frames, every 20 things  
for i in range(1, len(c_coll)-1): 
    obj = c_coll[i]
    # print(obj)
    old_loc = obj.location
    # print('c_coll[i-1].locatio', c_coll[i-1].location)
    obj.location = (old_loc[0],old_loc[1], c_coll[i-1].location[2]+z_stack)
    # print(f'frame{i}',old_loc, obj.location)
# for i in range(0,390, 30):
    # r = int(i/30) * 30
#     e.rotation_euler = [0, 0, radians(r)]
    obj.keyframe_insert("location", frame = i*20)
    
    if i <len(c_coll):
        next_obj = c_coll[i+1]
        next_obj.keyframe_insert("location", frame = i*20)

bpy.context.scene.frame_end = len(c_coll)*20
bpy.context.scene.render.image_settings.file_format = 'FFMPEG'
bpy.context.scene.render.ffmpeg.codec = 'H264'
bpy.context.scene.render.ffmpeg.format = 'MPEG4'

bpy.context.scene.eevee.use_soft_shadows = False

# for fc in e.animation_data.action.fcurves:
    # fc.extrapolation = 'LINEAR'
    
    
# print(path)