# Improving the Utility of Temporal LIDAR Data In Semantic Segmentation

![Research Poster](researchposter.jpg)

Over the past several years, LIDAR has become an increasingly important tool for mapping the environment as points in 3-dimensional space, especially in the context of autonomous driving. This trend has created a need to develop computer-based techniques that make sense of this data. Similar to object detection in 2D images, many 3D object detection algorithms draw rough bounding boxes to label objects. Another approach, however, is to classify every point into a category (such as road, car, pedestrian, etc.) through a process known as semantic segmentation. 

In this repository we present a data augmentation technique that improves the density of point clouds using temporal LIDAR data by merging LIDAR data over time to solve the issue of sparsity.

### Directory Overview

    ├── RandLA-Net   # Dynamic Link to active segmentation github repository
    ├── Stable-RandLA-Net # Archived stable functioning LIDAR segmentation       
    └── ICP.cpp # Iterative Closest Point Algorithm Implementation
    └── Eigen # C++ Linear Algebra Library
    └── DynamicVisualizer.py # LIDAR data visualization 
    └── README.md # You are viewing this right now


