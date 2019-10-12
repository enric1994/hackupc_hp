import bpy
import math
import sys
argv = sys.argv
argv = argv[argv.index("--") + 1:]

bpy.ops.import_curve.svg (filepath=argv[0])
objects = bpy.context.scene.objects

for obj in objects:
    obj.select = obj.type == "CURVE"
bpy.context.scene.objects.active = bpy.data.objects["Curve"]
bpy.ops.object.join()



context = bpy.context
scene = context.scene

mball = bpy.data.objects.get("Curve")

if mball:
    me = mball.to_mesh(scene, False, 'PREVIEW')

    # add an object
    o = bpy.data.objects.new("MBallMesh", me)
    scene.objects.link(o)
    o.matrix_world = mball.matrix_world

    # not keep original
    scene.objects.unlink(mball)


bpy.context.scene.objects.active = o
bpy.ops.object.modifier_add(type='SOLIDIFY')
bpy.context.object.modifiers["Solidify"].offset = 0.1
bpy.context.active_object.rotation_mode = 'XYZ'
bpy.context.active_object.rotation_euler = (math.radians(90), 0, 0)
bpy.context.scene.objects.active.scale = (30, 30, 30)
