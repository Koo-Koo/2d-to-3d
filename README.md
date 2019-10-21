
# 2D-to-3D

2019 Graduation Project

Convert multi-person pose from video to .blend with Jupyter Notebook


## Process
1. Conversion of video to images
2. 2d pose estimation from images [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) is used for estimation.
3. 3d pose estimation. [Fork](https://github.com/Koo-Koo/hmr) of [End-to-end Recovery of Human Shape and Pose](https://github.com/akanazawa/hmr)
4. Conversion of estimated .csv files to .bvh with additional *ground position of human.* [Fork](https://github.com/Koo-Koo/hmr) of [video_to_bvh](https://github.com/Dene33/video_to_bvh)
5. Conversion of *multiple .bvh files to single .blend files* with help of python script and .blend file.


## Installation
1. Get and build [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose) at `openpose` directory
   -  Refer requirements and installation guide at [Openpose](https://github.com/CMU-Perceptual-Computing-Lab/openpose)
2. Get our [Fork](https://github.com/Koo-Koo/hmr) of HMR at `hmr` directory
   -  Refer requirements and installation guide at [HMR](https://github.com/akanazawa/hmr)
3. Get [Blender](https://www.blender.org/) and [Makehuman](http://www.makehumancommunity.org)
    - You should install `MakeHuman plugin for blender` and `Mhx2 - MakeHuman eXchange` to use .mhx2 model
    - You can use your own .mhx2 file instead of .mhx2 files in `sample_model`  
4. Please make additional directories for outputs.      
    - `bash setting.sh` will create all the directories needed for our project. 

After setting, directory should look like this:  
```
graduation-project
└─ cali
  └─ center
└─ openpose
   └─ sample_videos
   └─ sample_jsons
   └─ sample_images
└─ hmr
  └─ output
    └─ bvh_animation
    └─ csv
    └─ csv_joined
└─ ...  
```  

## Usage
After installation just follow explantory text of `2d_to_3d.ipynb` Jupyter Notebook.


## result

* input video

![img1](https://github.com/Koo-Koo/graduation-project/blob/master/result_image/sq2_original.gif)

* bvh file

![img2](https://github.com/Koo-Koo/graduation-project/blob/master/result_image/squash2-final.gif)

* input video2

![img3](https://github.com/Koo-Koo/graduation-project/blob/master/result_image/{}.gif)

* bvh file

![img4](https://github.com/Koo-Koo/graduation-project/blob/master/result_image/badminton-final.gif)

* blend file rendered with Makehuman model

![img5](https://github.com/Koo-Koo/graduation-project/blob/master/result_image/badminton-final-model.gif)
