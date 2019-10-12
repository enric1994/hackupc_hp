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

# Remove materials
o.data.materials.clear()

# Create material
mat = bpy.data.materials.new(name="Material")

tex = bpy.data.textures.new("SomeName", 'IMAGE')
img = bpy.data.images.load(filepath="cheetah.jpg")

tex.image = img
# tex.texture_coords = 'WINDOW'

slot = mat.texture_slots.add()
slot.texture = tex
slot.texture_coords = 'OBJECT'


# Apply material
o.data.materials.append(mat)
# Change material color
color_map={
    "red":(1, 0, 0),
    "green":(0, 1, 0),
    "blue":(0, 0, 1)
}
# o.active_material.diffuse_color = (color_map[argv[1]])


bpy.ops.object.text_add(location=(0,0,1), rotation=(math.radians(90),0,0))
bpy.ops.object.editmode_toggle()
bpy.ops.font.delete()
bpy.ops.font.text_insert(text='heyoo')
bpy.ops.object.editmode_toggle()


area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
space = next(space for space in area.spaces if space.type == 'VIEW_3D')
space.viewport_shade = 'RENDERED'  # set the viewport shading