from plyfile import PlyData, PlyElement
import numpy as np

f = "5080_54400"
name = "dales_ply/test/" + f + ".ply"
plydata = PlyData.read(name)
print(plydata.elements[0].data[0])
print(plydata.elements[1].data[0])
data = np.stack((plydata['vertex'].data['x'],
                    plydata['vertex'].data['y'],
                    plydata['vertex'].data['z'],
                    plydata['vertex'].data['class']), axis=1)

out = "dales_ply/test/" + f + "_edit.ply"
