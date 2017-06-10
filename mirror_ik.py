
# copy IK settings from L bones to R bones

import bpy

obj = bpy.context.object
bones = obj.pose.bones

for lbone in bones:
    if not lbone.name.endswith('L'): continue
    rbone = bones[lbone.name[:-1] + 'R']
    
    rbone.lock_ik_x = lbone.lock_ik_x
    rbone.lock_ik_y = lbone.lock_ik_y
    rbone.lock_ik_z = lbone.lock_ik_z
    
    rbone.use_ik_limit_x = lbone.use_ik_limit_x
    rbone.use_ik_limit_y = lbone.use_ik_limit_y
    rbone.use_ik_limit_z = lbone.use_ik_limit_z
    
    rbone.ik_min_x = lbone.ik_min_x
    rbone.ik_max_x = lbone.ik_max_x
    
    rbone.ik_min_y = -lbone.ik_max_y
    rbone.ik_max_y = -lbone.ik_min_y
    
    rbone.ik_min_z = -lbone.ik_max_z
    rbone.ik_max_z = -lbone.ik_min_z