import pykitti
import os
import numpy as np

graph_type = "mayavi"
#graph_type = "matplotlib"

basedir = 'test_datasets'
date = '2011_09_26'
drive = '0048'


frame_range = range(1)

dataset = pykitti.raw(basedir, date, drive, frames = frame_range)

i = 0
velo = dataset.get_velo(i)

if graph_type == "mayavi":
    import mayavi.mlab
    
    fig = mayavi.mlab.figure(bgcolor=(0, 0, 0), size=(640, 360))
    mayavi.mlab.points3d(
        velo[:, 0],   # x
        velo[:, 1],   # y
        velo[:, 2],   # z
        velo[:, 2],   # Height data used for shading
        mode="point", 
        colormap='copper',  # 'bone', 'copper',

        scale_factor=100,  
        line_width=10,       
        figure=fig,
    )
    # velo[:, 3], # reflectance values
    mayavi.mlab.show()

else:

    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    
    skip = 50 

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    velo_range = range(0, velo.shape[0], skip) 
    ax.scatter(velo[velo_range, 0],   # x
               velo[velo_range, 1],   # y
               velo[velo_range, 2],   # z
               c=velo[velo_range, 3], # reflectance
               cmap='gray')

    ax.set_title('Skip', skip,'LIDAR Scan')
    plt.show()