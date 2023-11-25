# Geometry_Tools
Some geometry tools. Maintained by [Frank Zhiyang Dou](https://frank-zy-dou.github.io/index.html).

A list of our research work on Geometry Modeling and Processing.
- **[Medial Axis Approximation/Skeletonization]** 
  - Coverage Axis++: Efficient Skeletal Points Selection for 3D Shape Skeletionization, coming soon.
  - Coverage Axis: Inner Point Selection for 3D Shape Skeletonization, EUROGRAPHICS 2020. [[paper]](https://frank-zy-dou.github.io/projects/CoverageAxis/index.html)
- **[Point Cloud Orientation]** 
  - Globally Consistent Normal Orientation for Point Clouds by Regularizing the Winding-Number Field, SIGGRAPH 2023. [[paper]](https://xrvitd.github.io/Projects/GCNO/index.html)
- **[Surface Reconstruction]** 
  - RFEPS: Reconstructing Feature-line Equipped Polygonal Surface, SIGGRAPH Asia 2022. [[paper]](https://xrvitd.github.io/Projects/RFEPS/index.html)
- **[Shape Abstraction]** 
  - Top-Down Shape Abstraction Based on Greedy Pole Selection, TVCG 2020. [[paper]](https://ieeexplore.ieee.org/document/9095378) 
# Requirements
```angular2html
pip install trimesh
pip install scipy
```

# Mesh Reconstruction from MA
- Lazy shape reconstruction from MA file: [MAT_Mesh.py](MAT_Mesh.py).
![snapshot00.png](assets%2Fsnapshot00.png)
- Lazy shape reconstruction from MA file produced by QMAT:[MAT_Mesh_MA.py](MAT_Mesh_MA.py).

- Mesh Voxelization.
![MA_reconstruction.jpg](assets%2FMA_reconstruction.jpg)_


# Metrics
[metrics.py](metrics.py)

# 2D tools
## Power Diagram & Voronoi Diagram
[2D_PD_VD.py](2D_PD_VD.py)

(Note we have VD == PD when all radii are zero.)

From repo: https://gist.github.com/marmakoide/45d5389252683ae09c2df49d0548a627

