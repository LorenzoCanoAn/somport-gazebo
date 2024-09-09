import os
import collada

folder = "/home/lorenzo/catkin_ws/src/somport-gazebo/models"
subfolders = os.listdir(folder)
subfolders.remove("somport_complete")
subfolders.remove("flip_normals.py")

for subfolder in subfolders:
    path_to_subfolder = os.path.join(folder, subfolder)
    elements_in_subfolder = os.listdir(path_to_subfolder)
    filename = None
    for element in elements_in_subfolder:
        if ".dae" in element:
            filename = element
    if filename is None:
        exit()
    path_to_file = os.path.join(path_to_subfolder, filename)
    print(path_to_file)
    mesh = collada.Collada(path_to_file)
    geometry = mesh.geometries[0]
    assert isinstance(geometry, collada.geometry.Geometry)
    print(geometry.primitives)
