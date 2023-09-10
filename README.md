# yolov5
使用Pytorch框架和yolov5模型进行深度学习，并在Linux和Windows环境进行预测
## 项目简介

- 基于**pytorch**框架进行训练
- 基于**Tensorrt**加速**Yolov5 7.0**
- 支持**Windows10**和**Linux**
- 支持**Python/C++**

## 环境说明
### Windows10
- Tensorrt 8.2.5.1
- Cuda 10.2 Cudnn 8.2.1(**特别注意需安装两个cuda10.2补丁**)
- Opencv 3.4.6
- Cmake 3.17.1
- VS 2017
- RTX3050

### Linux(Jetson Nano)
- Tensorrt 8.2.1.1
- Cuda 10.2 Cudnn 8.2.1
- Opencv 3.4.6
- Cmake 3.10.2
#### 查看自己的版本
- Cuda      ```nvcc -V```
- Cudnn     查看cudnn_version.h文件
- TensorRT(Linux)  ```dpkg -l | grep TensorRT```
- Cmake     ```cmake --version```
- OpenCV(Linux C++)    ```pkg-config --modversion opencv```

