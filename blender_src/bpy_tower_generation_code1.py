import bpy
import json
import os 
import sys
import numpy as np
import random
from mathutils import Matrix
from math import radians
from pathlib import Path
 
############
#####
floor_mat = bpy.data.materials.new(name = "Floor")
floor_mat.use_nodes = True
# let's create a variable to store our list of nodes
floor_mat_nodes = floor_mat.node_tree.nodes

# let's set the metallic to 1.0
#floor_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.319199, 0.66187, 0.66187, 0.8) #blue teal
floor_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.464, 0.278, 0.621, 1) #greyish table in ECCL

#(0.1, 0.2, 0.2, 0.8)
floor_mat_nodes['Principled BSDF'].inputs['Roughness'].default_value=1.0

wall_mat = bpy.data.materials.new(name = "Wall")
wall_mat.use_nodes = True
# let's create a variable to store our list of nodes
wall_mat_nodes = wall_mat.node_tree.nodes
wall_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.459, 0.765, 0.888, 0.8) #green wall in ECCL
    
def make_surface(mat, loc, rotation = (0,0,0,0),scale=(15.0,15.0,0.1)):
    # floor = bpy.ops.mesh.primitive_plane_add(size = 10, location=(0.0, 0.0, -0.05))
    surf = bpy.ops.mesh.primitive_cube_add(size = 1, location=loc, scale = scale)
    bpy.context.object.rotation_mode = 'QUATERNION'
    bpy.context.object.rotation_quaternion=rotation

    # bpy.ops.object.modifier_add(type='BEVEL')
    # bpy.context.object.modifiers["Bevel"].affect = 'VERTICES'
    # bpy.context.object.modifiers["Bevel"].width = 5
    # bpy.context.object.modifiers["Bevel"].segments = 30

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
    
#make_surface(floor_mat,loc = (0.0, 0.0, -0.05), rotation = (0,0,0,0), scale=(25.0,25.0,0.1))
#make_surface(wall_mat,loc = (0.0, -25, 0), rotation = (0.707,-0.707, 0,0))

#bpy.ops.wm.obj_import(filepath="/Users/kristinezheng/lookit-jenga/blender_src/background_wall.obj")

#####
#create material
wood_mat = bpy.data.materials.new(name = "Wood")
wood_mat.use_nodes = True
# let's create a variable to store our list of nodes
wood_mat_nodes = wood_mat.node_tree.nodes

# let's set the metallic to 1.0
# wood_mat_nodes['Principled BSDF'].inputs['Metallic'].default_value=0.5
#wood_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.05, 0.0185, 0.8, 1.0)
bsdf = wood_mat.node_tree.nodes["Principled BSDF"]
texImage = wood_mat.node_tree.nodes.new('ShaderNodeTexImage')
#texture_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', '..', 'images/plywood.png'))
texture_path = '/Users/kristinezheng/lookit-jenga/blender_src/textures_colors/wood_grain1.png'
texImage.image = bpy.data.images.load(texture_path)
wood_mat.node_tree.links.new(bsdf.inputs['Base Color'], texImage.outputs['Color'])

wood_mat_nodes['Principled BSDF'].inputs['Roughness'].default_value=0.167

jenga_mat = bpy.data.materials.new(name = "Jenga")
jenga_mat.use_nodes = True
# let's create a variable to store our list of nodes
jenga_mat_nodes = floor_mat.node_tree.nodes
jenga_mat_nodes['Principled BSDF'].inputs['Base Color'].default_value=(0.057, 0.686, 1, 1) #tan block

########### base tower/block
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

#######
path = '/Users/kristinezheng/lookit-jenga/2_20_towers/7979.json'
with open(path) as file:
    file_contents = file.read()
    
parsed_dict = json.loads(file_contents)
 
 
def make_parsed_tower(obj_dict, mat=None):
    Tower = bpy.context.blend_data.collections.new("Tower")
    bpy.context.collection.children.link(Tower)
    num_obj = len(obj_dict.keys())
    positions = []

    for i in range(1, num_obj+1):
        obj = obj_dict[str(i)]
#        print(obj)
        x_y_z_dim = (obj['x_size'], obj['y_size'], obj['z_size'])
        z_pos = (obj['pos'][0],obj['pos'][1], obj['pos'][2]+10)
        if i == 1:
            z_pos = (obj['pos'][0],obj['pos'][1], obj['pos'][2])
#        print(i, obj['pos'])

        bpy.ops.mesh.primitive_cube_add(size=1, location = z_pos, scale = x_y_z_dim)
        bpy.context.object.rotation_mode='QUATERNION'
        bpy.context.object.rotation_quaternion=obj['ori'][-1], obj['ori'][0], obj['ori'][1], obj['ori'][2]
        
        # bpy.ops.rigidbody.object_add()
        bpy.ops.object.modifier_add(type='BEVEL')
        bpy.context.object.modifiers["Bevel"].width = 0.02
        bpy.ops.object.shade_smooth()
        
        cube = bpy.context.active_object
        print("LOCATION", cube.location)
        positions.append(cube.location)

        Tower.objects.link(bpy.context.object)
        
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
BlockTower, BlockPositions = make_parsed_tower(parsed_dict, wood_mat)

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

#num_blocks = 10
#block_tower, positions = make_tower(obj_dict, num_blocks, jenga_mat, x_shift = 0) #0.15, 0, 0.3
#0,0.3,0.15

#### make grease pencil
#bpy.ops.object.gpencil_add(align='WORLD', location=(0, 0, 0), scale=(1, 1, 1), type='LRT_OBJECT')
#gp = bpy.context.active_object
#gp.grease_pencil_modifiers["Line Art"].thickness = 10
#gp.grease_pencil_modifiers["Line Art"].opacity = 0.5
#gp.grease_pencil_modifiers["Line Art"].source_type = 'COLLECTION'
#gp.grease_pencil_modifiers["Line Art"].source_collection = bpy.data.collections["Tower"]

#bpy.context.scene.view_layers["ViewLayer"].use_pass_z = True

#block_dim = (1.5/1.2,0.5/1.2,0.3/1.2)
## num_blocks = #len(list(parsed_dict.keys()))
##add light
#light_data = bpy.data.lights.new("light", type ="SPOT")
#light = bpy.data.objects.new("light", light_data)
#bpy.context.collection.objects.link(light)
#light.location = (0.62, 5.52, 1.78)
#light.rotation_quaternion[0] = 0.714# , -0.7, -0.002, 0.002)
#light.data.energy = 70
#light.data.diffuse_factor = 10
#light.data.shadow_soft_size = 2
#light.data.use_contact_shadow = True 

# light_data = bpy.data.lights.new("light", type ="AREA")
# light = bpy.data.objects.new("light", light_data)
# light.location = (block_dim[0]*1.5,block_dim[0]*1.5,block_dim[0]*(num_blocks+3))#(1.5,1.5,5)
# #light.data.shape = 'DISK'
# #light.data.energy = 1500
# #light.data.diffuse_factor = 5
# #light.data.size = 50
# light.data.energy = 15000
# light.data.diffuse_factor = 200
# light.data.size = 1000
# light.data.use_contact_shadow = True
# prev_block = positions[0]
# prev_block_height = 10 * 0.3
# print("PREV HEIGHT", prev_block, prev_block_height)

# light.data.use_shadow = False
        
        
# light_data2 = bpy.data.lights.new("light2", type ="AREA")
# light_data2.energy = 5000
# light2 = bpy.data.objects.new("light2", light_data2)
# bpy.context.collection.objects.link(light2)
# light2.location = (-5,-5,10)

# light2.data.diffuse_factor = 600
# light2.data.specular_factor = 30 
# light2.data.size = 1000
# light2.data.use_contact_shadow = True 

#rotate camera
# empty_cube = bpy.ops.object.empty_add(type='CUBE', align='WORLD', 
#         location=(0, 0, prev_block_height / 2), scale=(1,1,1))

#bpy.ops.transform.resize(value=(1.5,1.5,1.5), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)
#bpy.ops.transform.resize(value=(block_dim[0]*2,block_dim[0]*2,prev_block_height), orient_type='GLOBAL', orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL', mirror=False, use_proportional_edit=False, proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False, use_proportional_projected=False)

##create camera
#cam_data = bpy.data.cameras.new('camera')
#cam = bpy.data.objects.new('camera', cam_data)
#bpy.context.collection.objects.link(cam)
#cam.location = (2,12,3)#(4,10,3)


#cam.rotation_mode = "XYZ"
#cam.rotation_euler=(84 * np.pi/180, 0, 175 * np.pi/180)


t = bpy.data.collections['Tower']
c_coll = t.objects
# for c in range(1)):
c_coll[1].keyframe_insert("location", frame = 0)

z_stack = obj_dict['pos'][2]*2
# assume 400 frames, every 20 things  
for i in range(1, len(c_coll)): 
    obj = c_coll[i]
    old_loc = obj.location
    obj.location = (old_loc[0],old_loc[1], old_loc[2]-10)
    #c_coll[i-1].location[2]+z_stack)
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