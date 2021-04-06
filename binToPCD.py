# implementation for conversion of LiDAR data in Velodyne-128 .bin to .pcd
import numpy as np
import open3d as o3d

# Load binary point cloud
bin_pcd = np.fromfile("binary_file_name.bin", dtype=np.float32)

# Reshape and drop reflection values
points = bin_pcd.reshape((-1, 4))[:, 0:3]

# Convert to Open3D point cloud
o3d_pcd = o3d.geometry.PointCloud(o3d.utility.Vector3dVector(points))

# Save to whatever format you like
o3d.io.write_point_cloud("pointcloud.pcd", o3d_pcd)