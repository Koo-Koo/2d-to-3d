import bpy
import sys




# bpy.ops.render.render(animation=True, use_viewport=True)
# alt + o // alt + p
# blender --background --enable-autoexec --python render.py -- [file_name] [frame_num] [people_num] [option]

def render(file_name,frame_num,people_num):
    scn = bpy.context.scene  # get the current scene
    scn.frame_end = frame_num
    
    for i in range(people_num):
        bpy.ops.import_scene.makehuman_mhx2(filepath="sample_model/model.mhx2",rigType='MHX',useOverride=True)
        if i == 0:
            model = bpy.data.objects['Model2']
        else:
            model = bpy.data.objects['Model2.{:03d}'.format(i)]
        model.scale = (0.1,0.1,0.1)
        model.location[2] = 0.7
        
        if people_num==1:
            bpy.ops.mcp.load_and_retarget(filepath="{}.bvh".format(file_name,i))
        else:
            bpy.ops.mcp.load_and_retarget(filepath="{}_{:02d}.bvh".format(file_name,i))

    bpy.ops.wm.save_as_mainfile(filepath="{}.blend".format(file_name))
    print("{}.blend created".format(file_name))


def without_render(file_name,frame_num,people_num):
    scn = bpy.context.scene  # get the current scene
    scn.frame_end = frame_num
    
    if people_num==1:
        bpy.ops.import_anim.bvh(filepath="{}.bvh".format(file_name))
    else:
        for i in range(people_num):
            bpy.ops.import_anim.bvh(filepath="{}_{:02d}.bvh".format(file_name,i))
            
    bpy.ops.wm.save_as_mainfile(filepath="{}.blend".format(file_name))
    print("{}.blend created".format(file_name))


def preprocess():
    candidate_list = [item.name for item in bpy.data.objects if item.type == "MESH"]
    for object_name in candidate_list:
        bpy.data.objects[object_name].select = True
    bpy.ops.object.delete()
    for items in bpy.data.meshes:
        bpy.data.meshes.remove(items)

def main():
    argv = sys.argv
    argv = argv[argv.index("--")+1:]
    if len(argv)!=4 :
        print("argument error")
        return
    file_name = str(argv[0])
    frame_num = int(argv[1])
    people_num = int(argv[2])
    option = int(argv[3]) # rendering option
    print(file_name,frame_num,people_num,option)
    preprocess()
    if option==1:
        render(file_name,frame_num,people_num)
    elif option==2:
        without_render(file_name,frame_num,people_num)

if __name__ == "__main__":
    main()

