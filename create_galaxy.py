import numpy as np
import os
import bpy

filepath = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../hippa_pos.txt'))
pos = np.loadtxt(filepath)

mesh = bpy.data.meshes.new('Galaxy_mesh')
obj = bpy.data.objects.new('Galaxy', mesh)
bpy.context.scene.objects.link(obj)

faces = []
for i in range(len(pos)-2):
    faces.append([i, i+1, i+2])

mesh.from_pydata(pos, [], faces)
mesh.update()
