
# copy IK settings from L bones to R bones

import bpy

bl_info = {
    "name": "Mirror IK Settings",
    "author": "Will Alcorn",
    "version": (1, 0),
    "blender": (2, 78, 0),
    "location": "View3D > Pose Mode > Tools > Mirror IK",
    "description": "Copy bone IK settings from L to R",
    "warning": "",
    "wiki_url": "https://github.com/alcornwill/mirror_ik",
    "category": "Rigging",
    }

class MirrorIKPanel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "posemode"
    bl_category = "Tools"
    bl_label = "Mirror IK"
 
    def draw(self, context) :
        self.layout.operator("pose.mirror_ik", text = "Mirror IK")

        
class MirrorIK(bpy.types.Operator):
    bl_idname = "pose.mirror_ik"
    bl_label = "Mirror IK"
    bl_options = {"REGISTER", "UNDO"}
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"
    bl_context = "posemode"
    
    def execute(self, context):
        mirror_ik(context)
        return {"FINISHED"}
    
def mirror_ik(context):
    obj = context.object
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
        

def add_to_menu(self, context):
    self.layout.operator("pose.mirror_ik", icon = "PLUGIN")
 
def register():
    bpy.utils.register_class(MirrorIK)
    bpy.utils.register_class(MirrorIKPanel)
    bpy.types.VIEW3D_MT_pose.append(add_to_menu)
 
def unregister():
    bpy.utils.unregister_class(MirrorIK)
    bpy.utils.unregister_class(MirrorIKPanel)
    bpy.types.VIEW3D_MT_pose.remove(add_to_menu)
 
if __name__ == "__main__":
    register()
    