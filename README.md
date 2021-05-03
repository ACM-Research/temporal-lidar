# Improving the Utility of Temporal LIDAR Data In Semantic Segmentation

![Research Poster](researchposter.jpg)

## Introduction

Over the past several years, LIDAR has become an increasingly important tool for mapping the environment as points in 3-dimensional space, especially in the context of autonomous driving. This trend has created a need to develop computer-based techniques that make sense of this data. Similar to object detection in 2D images, many 3D object detection algorithms draw rough bounding boxes to label objects. Another approach, however, is to classify every point into a category (such as road, car, pedestrian, etc.) through a process known as semantic segmentation. 

![Segmentation Visualization](segmentvis.png)


In this repository we present a data augmentation technique that improves the density of point clouds using temporal LIDAR data by merging LIDAR data over time to solve the issue of sparsity.

## Motivation 

Traditional convolutional neural networks cannot be directly applied to LIDAR point clouds because the data is unstructured and irregular. 

To tackle this problem, researchers pivoted to Local Feature Aggregation Networks to segment and classify LIDAR data.

We researched several existing industry and research solutions that claimed to achieve effective semantic segmentation such as PointCNN, RangeNet, and VoxelNet. However, through our testing we found that these were outdated and had a smaller scope of application than we desired.

One recent solution, released in 2020, is RandLA-Net. This ML network satisfied requirements to propose and benchmark our solution.

Below is an brief architectural breakdown of 3 subsections of RandLA-Net.

![RandLA-Net](randlanetbreakdown.png)

Although RandLA-Net works quite well, all three sub-modules have a weakness: performance drops sharply when the density of the data is reduced. 

This leads us to propose a data augmentation process to improve semantic segmentation using temporal LIDAR data.


## Our Solution

Our pre-processor solution combines multiple consecutive LIDAR frames over time together to vastly improve point cloud density in two major ways:

1. An Iterative Closest Point algorithm estimates the drift change over multiple LIDAR frames.

2. Data from the integrated inertial measurement unit (IMU) is used to compensate for changes in acceleration across frames.


## Visualization of Solution




### Directory Overview

    ├── RandLA-Net   # Dynamic Link to active segmentation github repository
    ├── Stable-RandLA-Net # Archived stable functioning LIDAR segmentation       
    └── ICP.cpp # Iterative Closest Point Algorithm Implementation
    └── Eigen # C++ Linear Algebra Library
    └── DynamicVisualizer.py # LIDAR data visualization 
    └── README.md # You are viewing this right now


